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
globalId = 1
clientes = {}  # Diccionario vacío al inicio
globalCdtId = 1  # Contador global para IDs de CDT

#función para crear un cliente

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
        "creditos": {},
        "cdts": {}
    }

    print(f"El cliente {nombre} creado exitosamente.")


#Funcion para crear cuenta

def creacion_cuenta(cc,tipo_cuenta):
    global globalId
    dia=input("Ingrese el día de creación (1-31): ")
    mes=input("Ingrese el mes de creación (1-12): ")
    año=input("Ingrese el año de creación (e.g., 2025): ")
    fecha=dia+"/"+mes+"/"+año
    idCuenta=f'C{globalId:05d}'
    globalId += 1
    clientes[cc]["cuentas"][idCuenta]={
        "tipo":tipo_cuenta,
        "saldo":0.0,
        "movimientos": {}
    }
    idmov = 1
    clientes[cc]["cuentas"][idCuenta]["movimientos"][idmov] = {
        "tipo": "creacion",
        "monto": 0.0,
        "fecha": fecha
    }
    print(f"Cuenta '{tipo_cuenta}' fue creada con el id:{idCuenta}")

# función para depositar dinero en la cuenta de un cliente

def depositar_dinero():
    cc = input("Ingrese número de cédula del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return

    tipo_cuenta = input("Ingrese nombre de la cuenta (ej: ahorros, corriente): ")
    cuentas_cliente=clientes[cc]["cuentas"]
    idCuenta= None
    for cid,datos in cuentas_cliente.items():
        if datos["tipo"]==tipo_cuenta:
            idCuenta=cid
            break
    if not idCuenta:
        creacion_cuenta(cc,tipo_cuenta)
        for cid,datos in clientes[cc]["cuentas"].items():
            if datos["tipo"]==tipo_cuenta:
                idCuenta=cid

    monto = float(input("Ingrese monto a depositar: "))
    clientes[cc]["cuentas"][idCuenta]["saldo"] += monto
    print(f"Depósito de {monto} realizado exitosamente. Nuevo saldo en '{tipo_cuenta}' (ID: {idCuenta}): {clientes[cc]['cuentas'][idCuenta]['saldo']}")

#funcion para retirar dinero

def retirar_dinero():
    cc = input("Ingrese número de cédula del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return

    tipo_cuenta = input("Ingrese nombre de la cuenta (ej: ahorros, corriente): ")
    cuentas_cliente = clientes[cc]["cuentas"]
    idCuenta = None
    for cid, datos in cuentas_cliente.items():
        if datos["tipo"] == tipo_cuenta:
            idCuenta = cid
            break

    if not idCuenta:
        print(f"El cliente no tiene la cuenta '{tipo_cuenta}'.")
        return

    monto = float(input("Ingrese monto a retirar: "))
    if monto > clientes[cc]["cuentas"][idCuenta]["saldo"]:
        print("Fondos insuficientes.")
        return

    clientes[cc]["cuentas"][idCuenta]["saldo"] -= monto
    print(f"Retiro de {monto} realizado exitosamente. Saldo restante en '{tipo_cuenta}' (ID: {idCuenta}): {clientes[cc]['cuentas'][idCuenta]['saldo']}")

#funcion para crear un credito

def crear_credito(cc, tipo_credito):
    monto=float(input("Ingrese monto del crédito: "))
    plazo=int(input("Ingrese plazo en meses: "))
    cuota_mensual = monto/ plazo
    idCredito = f"credit{len(clientes[cc]['creditos']) + 1}"
    clientes[cc]["creditos"][idCredito] = {
        "tipo": tipo_credito,
        "monto": monto,
        "plazo": plazo,
        "cuota_mensual": cuota_mensual,
        "pagado": 0.0
    }
    print(f"Crédito creado exitosamente. Cuota mensual: {cuota_mensual}")

#Funcion para solicitar el credito

def solicitar_credito():
    cc = input("Ingrese número de cédula del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return

    tipo_credito = int(input("¿Qué tipo de crédito desea solicitar? (1. Libre inversión, 2. Vivienda, 3. Compra de auto): "))

    # Verificar si ya tiene un crédito de ese tipo
    creditos_cliente = clientes[cc]["creditos"]
    for credito in creditos_cliente.values():
        if credito["tipo"] == tipo_credito:
            print("El cliente ya cuenta con un crédito de este tipo.")
            return

    # Si no lo tiene, lo creamos
    match tipo_credito:
        case 1:
            crear_credito(cc, tipo_credito)
        case 2:
            crear_credito(cc, tipo_credito)
        case 3:
            crear_credito(cc, tipo_credito)
        case _:
            print("Tipo de crédito no válido.")

#Pago de cuota de credito
def pagar_credito():
    cc = input("Ingrese número de cédula del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return
    creditopago=int(input("Ingrese el tipo de credito al cual desea realizar un abono(1. Libre inversión, 2. Vivienda, 3. Compra de auto): "))
    creditos_cliente = clientes[cc]["creditos"]
    pago= float(input("Ingrese monto a pagar: "))
    for idcredito,credito in creditos_cliente.items():
        if credito["tipo"]== creditopago:
            if pago > credito["monto"]- credito["pagado"]:
                print("El monto a pagar excede el saldo del crédito.")
                return
            if pago <= 0:
                print("El monto a pagar debe ser mayor que cero.")
                return
            if pago == credito["monto"] - credito["pagado"]:
                print("El credito fue pagado en su totalidad.")
                del clientes[cc]["creditos"][idcredito]
                return
            if pago < credito["monto"] - credito["pagado"]:
                print("El pago fue realizado exitosamente.")
                credito["pagado"] += pago
                print(f"Saldo restante: {credito['monto'] - credito['pagado']}")
                return
                



    
#Solicitar CDT

def solicitar_cdt():
    cc = input("Ingrese número de cédula del cliente: ")
    if cc not in clientes:
        print("Cliente no encontrado.")
        return
    crear_cdt(cc)

#Crear CDT

def crear_cdt(cc):
    global globalCdtId
    cantidad = float(input("Ingrese monto del CDT: "))
    plazo = int(input("Ingrese plazo en meses: "))
    tasa = 0.09
    idCdt = f"CDT{globalCdtId:05d}"
    globalCdtId += 1
    clientes[cc]["cdts"][idCdt] = {
        "cantidad": cantidad,
        "plazo": plazo,
        "tasa": tasa,
    }
    print(f"CDT creado exitosamente con ID: {idCdt}")

#Menu principal

def main_Menu():
    while True:
        print("\nMenu Principal: ")
        print("1. Crear cliente")
        print("2. Depositar dinero")
        print("3. Solicitar crédito")
        print("4. Retirar dinero")
        print("5. Pago cuota crédito")
        print("6. Cancelar cuenta")
        print("7. Solicitar CDT")
        print("8. Salir")
        print("9. Mostrar información de cuentas")
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
                solicitar_cdt()
            case "8":
                print("Saliendo del programa...")
                break
            case "9":#prueba de visualizacion de clientes
                print("Clientes registrados:")
                for cc, datos in clientes.items():
                    print(f"Cédula: {cc}, Nombre: {datos['nombre']}, Email: {datos['email']}, Edad: {datos['edad']}, Cuentas: {datos['cuentas']}, Créditos: {datos['creditos']}, CDTs: {datos['cdts']}")

main_Menu()