# Dev Decision Engine Demo Repo

Proyecto Python minimo con errores intencionales para probar el analisis del Dev Decision Engine.

## Como reproducir

```bash
python app.py
```

Si defines `DEBUG=true`, saltas el primer bug de configuracion y llegas al error de negocio en `orders.py`.

## Errores intencionales

1. `src/config.py`
   Lee `DEBUG` desde entorno y llama `.lower()` sin validar si existe.

2. `src/orders.py`
   Asume que `order["items"]` siempre es iterable. Si viene `null` en el JSON, rompe al iterar.

3. `src/notifications.py`
   Llama `.lower()` sobre `customer["email"]` aunque puede ser `null`.

## Orden esperado de fallos

1. Sin variable `DEBUG`: `AttributeError` en `src/config.py`
2. Con `DEBUG=true`: `TypeError` en `src/orders.py`
3. Tras corregir `orders.py`: `AttributeError` en `src/notifications.py`

## Objetivo

Este repositorio esta hecho para que la IA detecte problemas reales de inicializacion de datos, validacion insuficiente y manejo deficiente de nulos.
