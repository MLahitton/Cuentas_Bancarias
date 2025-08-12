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
clientes[cc] = {
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "contacto": {"movil": movil, "fijo": fijo},
        "ubicacion": {"pais": pais, "departamento": departamento, "ciudad": ciudad},
        "cuentas": {},      # diccionario vacío para cuentas
        "creditos": {},      # diccionario vacío para créditos
        "saldo":saldo
    }

def crear_cliente():
    cc = input("Ingrese número de cédula: ")
    if cc in clientes:
        print("Cliente ya existe.")
    else:
        nombre = input ("Nombre completo: ")

        email = input("Email: ")

        edad = int(input ("Edad: "))

        movil = input ("Contacto móvil: ")

        fijo = input ("Contacto fijo: ")

        pais = input ("País: ")

        departamento = input ("Departamento: ")

        ciudad = input ("Ciudad: ")

    clientes [cc] = {
    "nombre": nombre,
    "email": email,
    "edad": edad,
    "contacto": {"movil": movil, "fijo": fijo},
    "ubicacion": {"pais": pais, "departamento": departamento, "ciudad": ciudad},
    }
    print(f"El cliente {nombre} creado exitosamente.")

def depositar_dinero():
    cc = input ("Ingrese número de cédula del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
       
    monto= float(input("Ingrese monto a depositar: "))

    if "saldo" not in clientes[cc]:
        clientes[cc]["saldo"] = 0.0

    clientes[cc]["saldo"] += monto
    print(f"Depósito de {monto} realizado exitosamente. Nuevo saldo: {clientes[cc]['saldo']}")
          
def retirar_dinero():
    cc = input("Ingrese número de cédula del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return

    monto = float(input("Ingrese monto a retirar: "))
    if monto > clientes[cc]["saldo"]:
        print("Fondos insuficientes.")
        return

    clientes[cc]["saldo"] -= monto
    print(f"Retiro de {monto} realizado exitosamente. Saldo restante: {clientes[cc]['saldo']}")

def main_Menu():
    while True:
        print("Menu Principal: ")
        print("Que accion desea realizar?")
        print("1. Crear cliente")
        print("2. Depositar dinero")
        print("3. Solicitar credito")
        print("4. Retirar dinero")
        print("5. Pago cuota credito")
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