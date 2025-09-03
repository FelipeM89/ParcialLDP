# Descripción

Este proyecto implementa una calculadora en C usando Flex y Bison que puede:

- Calcular la raíz cuadrada de números reales con sqrt().

- Resolver expresiones aritméticas con +, -, *, /.

- Leer expresiones desde un archivo de texto.

- Mostrar los resultados en la consola.

## Compilacion 
```
bison -d punto3.y
flex punto3.l
gcc punto3.tab.c lex.yy.c main.c -lfl -lm -o punto3
```
### Ejecucion
```
./punto3 entrada.txt

```
## Resultado
<img width="371" height="211" alt="image" src="https://github.com/user-attachments/assets/0eeb3c1d-351a-468f-b895-4dc3495aa43a" />
