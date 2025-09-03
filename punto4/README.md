# Expicacion

Este proyecto compara el rendimiento de un lenguaje compilado (C) y un lenguaje interpretado (Python) implementando exactamente el mismo algoritmo: un Autómata Finito Determinista (AFD).

El AFD que usamos reconoce cadenas del lenguaje:

L = {a^b | n >= 0}

Es decir, cualquier número de a seguidas de exactamente una b.

Ejemplos aceptados: b, ab, aaaab

Ejemplos rechazados: a, ba, abb, abc

La idea es procesar un archivo con muchas cadenas y medir cuánto tarda cada implementación. Esto nos permite demostrar experimentalmente la diferencia entre un lenguaje compilado y uno interpretado.

### Compilación y ejecución

1. En C (lenguaje compilado)
Compilar:
```
gcc afd.c -o afd
```
Ejecutar:

```
./afd cadenas.txt
```

2. En Python (lenguaje interpretado)
Ejecutar:
```
python3 afd.py cadenas.txt
```

## Ejemplo y Resultados 

a continucacionse presenta las ejecuciones de los codigos con los resultados correspondientes 
