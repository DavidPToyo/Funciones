import sys

if len(sys.argv) < 2:
    print("Uso: python filtro.py 'precio' [mayor o menor]")
    sys.exit(1)

precio = int(sys.argv[1])
modo = str(sys.argv[2]).lower() if len(sys.argv) > 2 else "mayor"

precios = {
    'Notebook'         : 700000,
    'Teclado'          : 25000,
    'Mouse'            : 12000,
    'Monitor'          : 250000,
    'Escritorio'       : 135000,
    'Tarjeta de Video' : 1500000
}

def filtro(precios: dict[str, int], precio: int, modo: str = "mayor"):
    resultado = []

    if modo == "mayor":
        for k, v in precios.items():
            if v > precio:
                resultado.append(k)

    elif modo == "menor":
        for k, v in precios.items():
            if v < precio:
                resultado.append(k)
                
    else:
        print("Lo sentimos, no es una operación válida.")
        sys.exit(1)

    return resultado

resultado = filtro(precios, precio, modo)

print(f"Los productos {modo}es al precio {precio} son:")
for producto in resultado:
    print("-", producto)
