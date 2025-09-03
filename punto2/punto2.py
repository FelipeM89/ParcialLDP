import sys

def afd_id(cadena: str) -> bool:
    if not cadena:
        return False
    if not cadena[0].isalpha():
        return False
    for c in cadena[1:]:
        if not (c.isalpha() or c.isdigit()):
            return False
    return True

def main():
    if len(sys.argv) != 2:
        print("Uso: python punto2.py archivo.txt")
        return
    archivo = sys.argv[1]
    with open(archivo, "r") as f:
        for linea in f:
            palabra = linea.strip()
            if afd_id(palabra):
                print(f"{palabra} -> ACEPTA")
            else:
                print(f"{palabra} -> NO ACEPTA")

if __name__ == "__main__":
    main()
