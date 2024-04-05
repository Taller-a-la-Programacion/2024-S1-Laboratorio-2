# 2024 S1 Laboratorio 2

## Instrucciones Generales
- El archivo **debe** llamarse **Laboratorio2.py**
- Debe realizar la siguiente función con iteración


## Ejercicio 1. Valor 10 puntos.
Escriba una función sumaImparesPares (lista1 , lista2) que reciba dos lista de números, y retorne una lista que contenga la suma de los índices pares de las dos listas de la misma manera con los índices impares. No puede usar len (), solo puede recorrer la lista una vez. La función debe comportarse de la siguiente manera:

```python
>>> sumaImparesPares([0,2,3,4], [4, 8, 6, 0])
[13, 14]
>>> sumaImparesPares([10, 0], [100, 2])
[110, 2]
 >>> sumaImparesPares([1,2], "dos")
 "Error: segundo argumento debe ser entero"
 ```

## Ejercicio 2. Valor 10 puntos.
Escribir una función en pyhon llamado **descomponerNumeros(lista)**, recibirá una lista no vacia con valores numéricos enteros. Debe retornar una lista compuesta con más listas dentro de este que contengo cada uno de los dígitos pares del número descompuesto

```python
>>> descomponerNumeros([8524,256,1023,3698,-204,139])
[[8,2,4],[2,6],[0,2],[6,8],[-2,0,-4]]

 >>> descomponerNumeros([])
"Error Lista vacia"
```

## Ejercicio 3. Valor 10 puntos.
Escribir una función en pyhon llamado **construirNumeros(lista)**, recibirá una lista no vacia con listas de números enteros. Debe retornar una lista con la construcción de nuevos números dado la sublista

```python
>>> construirNumeros( [[8,2,4], [2,6],[2],[6,8],[-2,0,-4]] )
[824, 26, 2, 68, -204]

>>> construirNumeros( [[18,2,4], [2,6],[60,800]] )
[1824, 26, 60800]

```
