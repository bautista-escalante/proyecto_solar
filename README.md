# API de Dimensionamiento Solar

Sistema de cálculo automático para propuestas técnicas de instalaciones fotovoltaicas en Argentina.

---

## Objetivo

Calcular y devolver, en una única llamada HTTP, una propuesta técnica completa de sistema fotovoltaico que incluye cantidad y potencia de paneles solares, potencia mínima del inversor, configuración de baterías (si aplica) y datos base utilizados para el cálculo.

---

## Arquitectura

El proyecto sigue los principios de **Clean Architecture** con separación estricta en capas:

```
POST /calculo
    │
    ▼
api/routes/calculo.py         → Recibe la request HTTP, devuelve JSONResponse
    │
    ▼
core/use_cases/               → Orquesta validación y construcción del sistema
CalcularSistemaUseCase
    │
    ▼
factory/SistemaFactory        → Decide si construir sistema On-Grid u Off-Grid
    │
    ├── services/ongrid_builder   → Arma el dict de respuesta On-Grid
    └── services/offgrid_builder  → Arma el dict de respuesta Off-Grid
```

### Estructura de carpetas

```
proyecto_solar/
├── main.py                          # Entry point, registra routers
├── api/
│   ├── routes/
│   │   └── calculo.py               # Endpoint POST /calculo
│   └── schemas/
│       └── CalculoSolarRequest.py   # Pydantic
├── core/
│   ├── models/
│   │   ├── Ongrid.py
│   │   └── Offgrid.py
│   ├── rules/
|   |   └──angulo.py
|   |   └──inversor.py
│   └── use_cases/
│       └── CalcularSistemaUseCase.py
│   │   ├── inversor.py
│   │   └── angulo.py
│   └── validators/
│       └── RequestValidator.py
├── factory/
│   └── Sistema_Factory.py
├── services/
│   ├── ongrid_builder.py
│   ├── offgrid_builder.py
│   └── propiedad_Solar.py
└── infrastructure/
    └── radiacion.py
```

---

## Endpoints

### `POST /calculo`

Calcula el dimensionamiento de un sistema fotovoltaico según los parámetros de consumo y ubicación.

#### Request Body

```json
{
  "tipo": "offgrid",
  "consumo_watts": 3500,
  "watts_panel": 550,
  "capacidad_elegida": 200,
  "tiempo": 6,
  "provincia": "Buenos Aires"
}
```

| Campo | Tipo | Requerido | Descripción |
|---|---|---|---|
| `tipo` | string | ✅ | Tipo de sistema: `"ongrid"` u `"offgrid"` |
| `consumo_watts` | float | ✅ | Consumo eléctrico simultáneo promedio en watts |
| `watts_panel` | int | ✅ | Potencia unitaria del panel fotovoltaico en Wp |
| `capacidad_elegida` | float | Solo offgrid | Capacidad unitaria de la batería en Ah |
| `tiempo` | float | Solo offgrid | Horas diarias de uso del consumo indicado |
| `provincia` | string | ✅ | Provincia argentina (determina HSP y factor de corrección) |

#### Response — On-Grid (`200 OK`)

```json
{
  "paneles": {
    "cantidad": 6,
    "potencia_unitaria_w": 550,
    "potencia_total_w": 3300
  },
  "inversor": {
    "potencia_minima_w": 4000,
    "tipo": "onda pura"
  },
  "bateria": {
    "necesaria": false,
    "capacidad_ah": null,
    "voltaje_banco": null
  },
  "angulo_inclinacion": 34
}
```

#### Response — Off-Grid (`200 OK`)

```json
{
  "paneles": {
    "cantidad": 8,
    "potencia_unitaria_w": 550,
    "potencia_total_w": 4400
  },
  "inversor": {
    "potencia_w": 4000,
    "tension_v": 24,
    "tipo": "onda pura"
  },
  "bateria": {
    "necesaria": true,
    "cantidad": 4,
    "capacidad_unitaria_ah": 200,
    "configuracion": {
      "serie": 2,
      "paralelo": 2
    },
    "voltaje_banco": 24
  }
}
```

#### Errores

| Código | Causa |
|---|---|
| `400 Bad Request` | Datos de entrada inválidos (tipo incorrecto, valores negativos, provincia vacía) |
| `500 Internal Server Error` | Error inesperado en el servidor |

```json
{ "error": "El consumo en watts debe ser un número positivo." }
```

---

## Lógica de cálculo

### On-Grid

| Variable | Fórmula |
|---|---|
| Potencia necesaria (kWp) | `consumo / (radiacion × factor)` |
| Cantidad de paneles | `ceil((kWp × 1000) / watts_panel)` |
| Inversor | Basado en tabla de consumo |
| Ángulo de inclinación | Según latitud de la provincia |

### Off-Grid

| Variable | Fórmula |
|---|---|
| Trabajo diario (Wh) | `consumo × tiempo` |
| Watts necesarios (paneles) | `trabajo × 0.75 / radiacion` |
| Capacidad banco baterías (Ah) | `trabajo / (profundidad_descarga × tension)` |
| Cantidad de baterías | `ceil(capacidad_necesaria / capacidad_bateria)` |
| Configuración serie | Depende de la tensión del inversor (12V→1, 24V→2, 48V→4) |

---

## Validaciones

El sistema valida los datos de entrada antes de realizar cualquier cálculo:

- `tipo` debe ser `"ongrid"` o `"offgrid"`
- `consumo_watts` debe ser mayor a 0
- `watts_panel` debe ser mayor a 0
- `capacidad_elegida` debe ser mayor a 0 (requerido solo para offgrid)
- `tiempo` debe ser mayor a 0 (requerido solo para offgrid)
- `provincia` debe ser un string no vacío

---

## Fuentes de datos

Los valores de **Horas Solar Pico (HSP)** y **factores de corrección** por provincia se obtienen de:

- [Servicio de Normalización de Datos Geográficos — datos.gob.ar](https://datos.gob.ar/ar/dataset/jgm-servicio-normalizacion-datos-geograficos/archivo/jgm_8.9)
- [Guía del Recurso Solar — Ministerio de Energía Argentina](https://www.argentina.gob.ar/sites/default/files/guia_del_recurso_solar_anexos_final.pdf)
