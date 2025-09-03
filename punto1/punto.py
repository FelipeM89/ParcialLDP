def afd_a_b_c(cadena: str) -> bool:
    estado = 0
    for c in cadena:
        if estado == 0:  
            if c == 'a':
                estado = 0
            elif c == 'b':
                estado = 1
            elif c == 'c':
                estado = 2
            else:
                return False
        elif estado == 1:  
            if c == 'b':
                estado = 1
            elif c == 'c':
                estado = 2
            else:
                return False
        elif estado == 2:  
            if c == 'c':
                estado = 2
            else:
                return False
    return True


pruebas = ["", "aaa", "aabbc", "bbccc", "cc", "cab", "bac", "acb"]
for p in pruebas:
    print(f"{p!r:6} -> {'ACEPTA' if afd_a_b_c(p) else 'NO ACEPTA'}")
