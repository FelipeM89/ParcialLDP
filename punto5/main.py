import sys
from antlr4 import *
from FiboLexer import FiboLexer
from FiboParser import FiboParser
from EvalVisitor import EvalVisitor

def main():
    
    entrada = input("Escribe un numero con el formato FIBO(XX) ")

    input_stream = InputStream(entrada)
    lexer = FiboLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FiboParser(stream)
    tree = parser.prog()

    visitor = EvalVisitor()
    resultado = visitor.visit(tree)

    print("Resultado:", ", ".join(map(str, resultado)))

if __name__ == '__main__':
    main()
