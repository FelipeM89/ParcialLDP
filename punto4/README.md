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
gcc punto4.c 
```
Ejecutar:

```
./a.out cadenas.txt
```

2. En Python (lenguaje interpretado)
Ejecutar:
```
python3 punto4.py cadenas.txt
```

## Ejemplo y Resultados 

a continucacionse presenta las ejecuciones de los codigos con los resultados correspondientes 

Estos fueron los resultados de python:

<img width="416" height="109" alt="image" src="https://github.com/user-attachments/assets/4303491e-38fa-495c-8726-0a106675bd06" />

Estos fueron los resultados para c

<img width="404" height="161" alt="image" src="https://github.com/user-attachments/assets/961e3cab-f2c4-4064-a046-3242a2567cda" />

**Si bien los tiempos fueron cortos, que fue debido a que las cadenas a texto a realzar ern demasiada pequeñas, se nota una diferencia de timepo, para eso vamos a poner una cadena mucho más larga, ppara que ambos se demoren mas tiempo en analizarla**

