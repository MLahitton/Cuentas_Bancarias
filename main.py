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
contador_id={}
def crear_cliente():
    cc = input("Ingrese número de cédula: ")
    if not cc.isdigit or len(cc)<6:
        print("La cedula debe ser numerica y tener al menos 7 dígitos.")
        return
    if cc in clientes:
        print("Cliente ya existe.")
        return  # Evitar sobreescribir

    nombre = input("Nombre completo: ")
    email = input("Email: ")
    edad = int(input("Edad: "))
    movil = input("Contacto móvil: ")
    if not movil.isdigit() or len(movil) < 10:
        print("El número de móvil debe ser numérico y tener al menos 10 dígitos.")
        return
    fijo = input("Contacto fijo: ")
    if not fijo.isdigit() or len(fijo) < 7:
        print("El número de fijo debe ser numérico y tener al menos 7 dígitos.")
        return
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
def generarId(cc, tipo_cuenta):
    if cc not in contador_id:
        contador_id[cc] = {"cuenta": 0, "credito": 0}
        contador_id[cc]["cuenta"] += 1
        return f'{tipo_cuenta}_{cc}_{contador_id[cc]["cuenta"]}'
def depositar_dinero():
    cc = input("Ingrese número de cédula del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return

    cuenta = input("Ingrese nombre de la cuenta (ej: ahorros, corriente): ")

    cuentas_existentes = [nombre for nombre in clientes[cc]["cuentas"] if nombre.startswith(cuenta)]
    if cuentas_existentes:
        # Usar la última cuenta creada con ese nombre
        cuenta_nombre = cuentas_existentes[-1]
    else:
        cuenta_nombre = f"{cuenta}_{len(clientes[cc]['cuentas']) + 1}"
        cuenta_id = generarId("cuenta", cc)
        nombreCuenta = f"{cuenta}_{len(clientes[cc]['cuentas']) + 1}"
        clientes[cc]["cuentas"][nombreCuenta] = {
            "id": cuenta_id,
            "saldo": 0.0,
            "historial": [f"Cuenta creada con ID {cuenta_id}"]
        }
        print(f"Cuenta '{nombreCuenta}' creada con ID {cuenta_id}.")
    monto = float(input("Ingrese monto a depositar: "))
    clientes[cc]["cuentas"][nombreCuenta]["saldo"] += monto
    clientes[cc]["cuentas"][nombreCuenta]["historial"].append(f"Depósito de {monto}")
    print(f"Depósito de {monto} realizado exitosamente. Nuevo saldo en '{cuenta}': {clientes[cc]["cuentas"][cuenta_nombre]['saldo']}")

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
def crear_credito(cc, tipo_credito):
    monto=float(input("Ingrese monto del crédito: "))
    plazo=int(input("Ingrese plazo en meses: "))
    cuota_mensual = monto/ plazo
    clientes[cc]["creditos"][f"credito_{len(clientes[cc]['creditos']) + 1}"] = {
        "tipo": tipo_credito,
        "monto": monto,
        "plazo": plazo,
        "cuota_mensual": cuota_mensual,
        "pagado": 0.0
    }
    print(f"Crédito creado exitosamente. Cuota mensual: {cuota_mensual}")

def pagar_credito():
    cc = input("Ingrese número de cédula del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return
    
    creditopago=int(input("Ingrese el credito al cual desea realizar un abono(1. Libre inversión, 2. Vivienda, 3. Compra de auto): "))
    pago=float(input("Ingrese el monto que desea pagar: "))
    credito_Apagar=clientes[cc]["creditos"]
    for credito in credito_Apagar.values():
        if credito["tipo"]==creditopago:
            if pago > credito["monto"] - credito["pagado"]:
                print("El monto a pagar excede el saldo del crédito.")
                return
            credito["pagado"] += pago
            print(f"Pago de {pago} realizado exitosamente. Saldo restante: {credito['monto'] - credito['pagado']}")
            return
        
def cancelar_cuenta():
    cc = input("Ingrese número de cédula del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return

    clientes[cc]["cuentas"].clear()
    clientes[cc]["creditos"].clear()
    print(f"Cuenta del cliente {clientes[cc]['nombre']} cancelada exitosamente.")
    del clientes[cc]  
            
            

    


def solicitar_credito():
    cc = input("Ingrese número de cédula del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return

    tipo_credito = int(input("¿Qué tipo de crédito desea solicitar? (1. Libre inversión, 2. Vivienda, 3. Compra de auto): "))

    creditos_cliente = clientes[cc]["creditos"]
    for credito in creditos_cliente.values():
        if credito["tipo"] == tipo_credito:
            print("El cliente ya cuenta con un crédito de este tipo.")
            return

    match tipo_credito:
        case 1:
            crear_credito(cc, tipo_credito)
        case 2:
            crear_credito(cc, tipo_credito)
        case 3:
            crear_credito(cc, tipo_credito)
        case _:
            print("Tipo de crédito no válido.")

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
                solicitar_credito()
            case "4":
                retirar_dinero()
            case "5":
                pagar_credito()
            case "6":
                print(clientes)
            case "7":
                print("Saliendo del programa...")
                break
            case "8":
                cancelar_cuenta()
            case "9":
                print("Clientes registrados:")
                for cc, datos in clientes.items():
                    print(f"Cédula: {cc}, Nombre: {datos['nombre']}, Email: {datos['email']}, Edad: {datos['edad']}, Cuentas: {datos['cuentas']}, Créditos: {datos['creditos']}")


main_Menu()
