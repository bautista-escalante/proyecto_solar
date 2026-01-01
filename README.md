# proyecto_solar
El programa busca brindar al usuario una solución eficiente y personalizada para su sistema de energía solar.

## 🎯 Objetivo

Calcular y devolver, en una única llamada, una propuesta técnica de sistema fotovoltaico que incluya:

Cantidad y potencia de paneles solares

Potencia mínima requerida del inversor

Capacidad de batería necesaria (si aplica)

Datos base utilizados para el cálculo

## 📥 Inputs

La API recibe los siguientes parámetros:

```json
{
  "consumo_watts": 3500,
  "horas_uso_diarias": 6,
  "provincia": "Buenos Aires",
  "tipo_sistema": "aislado",
  "horas_autonomia": 12
}
 ```
| Campo	| Descripción |
 :------|-------------:
| consumo_watts | Consumo eléctrico simultáneo promedio|
| horas_uso_diarias | Horas diarias de uso del consumo indicado|
| provincia | Provincia de Argentina (define HSP)|
| tipo_sistema | aislado, interconectado o hibrido|
| horas_autonomia | Horas de autonomía requeridas (solo sistemas con batería)|

## 📥 Outputs

La API devuelve un objeto JSON con el sistema dimensionado:

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
    "necesaria": true,
    "capacidad_ah": 400,
    "voltaje_banco": 24
  }
}
 ```


# fuentes
* https://datos.gob.ar/ar/dataset/jgm-servicio-normalizacion-datos-geograficos/archivo/jgm_8.9
* https://www.argentina.gob.ar/sites/default/files/guia_del_recurso_solar_anexos_final.pdf
