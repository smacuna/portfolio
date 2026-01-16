# Portafolio de acciones

Este proyecto permite mantener portafolios de acciones balanceados en base a sus distribuciones de porcentajes.

## Descripción

El programa consiste en una simulación de tres portafolios, con sus respectivas distribuciones de porcentajes. Se parte desde el 15 de diciembre de 2025 y se simula hasta el 15 de enero de 2026.

Los portafolios son:

- Portfolio A: 20% META, 20% AAPL, 20% GOOGL, 20% MSFT, 20% NVDA, con un valor de 1000 USD
- Portfolio B: 10% META, 30% AAPL, 30% GOOGL, 10% MSFT, 10% AMZN, 10% NVDA, con un valor de 1000 USD
- Portfolio C: 10% META, 30% AAPL, 30% GOOGL, 10% MSFT, 10% AMZN, 10% NVDA, con un valor de 2000 USD

El programa creará un archivo que contiene todas las acciones que se deben tomar para mantener los portafolios balanceados.

## Requisitos

1. Python 3.9.6 o superior
2. Instalar dependencias: 
```
pip install -r requirements.txt
```

## Ejecución
Para ejecutar el programa se debe ejecutar el siguiente comando:
```
python main.py
```

## Origen de datos

Los datos de los precios de acciones por día se obtienen de un csv (ubicado en `data/stock_prices.csv`) creado en base a un [Google Sheet](https://docs.google.com/spreadsheets/d/1SJbRo6FwzH0JZ8Vvf3I0DjSZzPQCFcdBZ13iw9Gcsmc/edit?usp=sharing), inspirado por una [conversación con Gemini.](https://gemini.google.com/share/e0ee44bbfbd4)

## Resultados

Los resultados se guardan en el archivo `results/results.csv` que tiene la siguiente estructura:

```
Portfolio,Date,Action,Stock,Quantity
```

Donde:
- `Portfolio`: Nombre del portafolio
- `Date`: Fecha en formato `dd/mm/yyyy`
- `Action`: `Buy` si se debe comprar acciones o `Sell` si se debe vender acciones
- `Stock`: Símbolo de la acción
- `Quantity`: Cantidad de acciones a comprar o vender



## Comentarios adicionales

- Con el objetivo de poder simular más de un día, se agrega el parámetro `date` a los métodos `current_price` y `rebalance`.
