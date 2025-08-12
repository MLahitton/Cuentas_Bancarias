cc=""
nombre=""
email=""
edad=""
movil=""
fijo=""
pais=""
departamento=""
ciudad=""
clientes = {
        "nombre": nombre,
        "email": email,
        "edad": edad,
        "contacto": {"movil": movil, "fijo": fijo},
        "ubicacion": {"pais": pais, "departamento": departamento, "ciudad": ciudad},
        "cuentas": {},      # diccionario vacío para cuentas
        "creditos": {}      # diccionario vacío para créditos
    }

def crear_cliente():
    cc = input("Ingrese número de cédula: ")
    if cc in clientes:
        print("Cliente ya existe.")
    return
    nombre - input ("Nombre completo: ")

    email = input("Email: ")

    edad = int(input ("Edad: "))

    movil = input ("Contacto móvil: ")

    fijo = input ("Contacto fijo: ")

    pais = input ("País: ")

    departamento = input ("Departamento: ")

    ciudad = input ("Ciudad: ")

    Clientes [cc] = {
    "nombre": nombre,
    "email": email,
    "edad": edad,
    "contacto": {"movil": movil, "fijo": fijo},
    "ubicacion": {"pais": pais, "departamento": departamento, "ciudad": ciudad},
    }
    print(f"El cliente {nombre} creado exitosamente.")