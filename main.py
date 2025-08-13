"""
cc=""
nombre=""
email=""
edad=""
movil=""
fijo=""
pais=""
departamento=""
ciudad=""
saldo=0.0
clientes = {}
"""
clientes = {}  # Diccionario vacío al inicio

def crear_cliente():
    cc = input("Ingrese número de cédula: ")
    if cc in clientes:
        print("Cliente ya existe.")
        return  # Evitar sobreescribir

    nombre = input("Nombre completo: ")
    email = input("Email: ")
    edad = int(input("Edad: "))
    movil = input("Contacto móvil: ")
    fijo = input("Contacto fijo: ")
    pais = input("País: ")
    departamento = input("Departamento: ")
    ciudad = input("Ciudad: ")

    clientes[cc] = {
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "contacto": {"movil": movil, "fijo": fijo},
        "ubicacion": {"pais": pais, "departamento": departamento, "ciudad": ciudad},
        "cuentas": {},  # Aquí se guardan todas las cuentas con sus saldos
        "creditos": {}
    }

    print(f"El cliente {nombre} creado exitosamente.")

def depositar_dinero():
    cc = input("Ingrese número de cédula del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return

    cuenta = input("Ingrese nombre de la cuenta (ej: ahorros, corriente): ")
    if cuenta not in clientes[cc]["cuentas"]:
        clientes[cc]["cuentas"][cuenta] = 0.0
        print(f"Cuenta '{cuenta}' creada.")

    monto = float(input("Ingrese monto a depositar: "))
    clientes[cc]["cuentas"][cuenta] += monto
    print(f"Depósito de {monto} realizado exitosamente. Nuevo saldo en '{cuenta}': {clientes[cc]['cuentas'][cuenta]}")

def retirar_dinero():
    cc = input("Ingrese número de cédula del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return

    cuenta = input("Ingrese nombre de la cuenta: ")
    if cuenta not in clientes[cc]["cuentas"]:
        print(f"El cliente no tiene la cuenta '{cuenta}'.")
        return

    monto = float(input("Ingrese monto a retirar: "))
    if monto > clientes[cc]["cuentas"][cuenta]:
        print("Fondos insuficientes.")
        return

    clientes[cc]["cuentas"][cuenta] -= monto
    print(f"Retiro de {monto} realizado exitosamente. Saldo restante en '{cuenta}': {clientes[cc]['cuentas'][cuenta]}")

def main_Menu():
    while True:
        print("\nMenu Principal: ")
        print("1. Crear cliente")
        print("2. Depositar dinero")
        print("3. Solicitar crédito")
        print("4. Retirar dinero")
        print("5. Pago cuota crédito")
        print("6. Cancelar cuenta")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                crear_cliente()
            case "2":
                depositar_dinero()
            case "3":
                pass
            case "4":
                retirar_dinero()
            case "5":
                pass
            case "6":
                pass
            case "7":
                print("Saliendo del programa...")
                break

main_Menu()
