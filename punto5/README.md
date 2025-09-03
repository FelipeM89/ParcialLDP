# Descripción


Este proyecto implementa un intérprete en Python usando ANTLR4 que reconoce instrucciones del tipo:
```
FIBO(20)
```
y genera como salida la secuencia de Fibonacci hasta el número indicado.

## Instalación y preparación

Crear un entorno virtual:
```
python3 -m venv venv
source venv/bin/activate
```

Instalar la librería de ANTLR para Python:
```
pip install antlr4-python3-runtime
```

Descargar ANTLR
```
wget https://www.antlr.org/download/antlr-4.13.2-complete.jar
```

Compila con:
```
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor punto5.g4
```
Ejecuta el programa principal:
```
python main.py
```

