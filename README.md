Autor
Manuel José Gómez Laiton

Descripción
Este proyecto es un sistema bancario básico en Python que permite la gestión de clientes, cuentas, depósitos, retiros, créditos y certificados de depósito a término (CDT).  
Se ejecuta en consola y guarda los datos en memoria usando diccionarios.

Stack Tecnologico
Lenguaje: Python 3.x
Entorno: Consola
Paradigma: Programación estructurada

Requerimientos
-Python 3.x instalado.
-Sistema operativo compatible: Linux o Windows.
-Editor de texto o IDE (ej. VS Code, PyCharm).

Ejecución : Como se ejecuta su proyecto

Linux
bash
python3 main.py


Windows

bash
python main.py


Estructura de Archivos


proyecto/

main.py             # Código principal del sistema bancario
README.md           # Documentación del proyecto


Librerias Externas

No requiere librerías externas, todo funciona con módulos estándar de Python.

---

Funcionalidades Principales

Crear cliente
  Registra un nuevo cliente solicitando cédula, nombre, email, edad, contactos y ubicación.

Crear cuenta
  Genera una cuenta con tipo (ahorros, corriente) y registra el primer movimiento de creación.

Depositar dinero
  Permite agregar saldo a una cuenta existente, o crearla si no existe.

Retirar dinero
  Descuenta saldo de la cuenta, validando fondos suficientes.

Solicitar crédito
  Asigna un crédito a un cliente, calculando cuota mensual.

Pagar crédito
  Realiza abonos al crédito y elimina el registro si se paga en su totalidad.

Solicitar CD
  Crea un certificado de depósito con monto, plazo y tasa predefinida.

Visualizar clientes
  Muestra todos los datos y movimientos de cada cliente registrado.

