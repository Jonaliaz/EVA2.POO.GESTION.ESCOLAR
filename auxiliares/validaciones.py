import re
from datetime import datetime


def validar_rut(rut):
    patron_rut = r'^\d{1,3}(?:\.\d{3})*-?[0-9kK]$'

    if re.match(patron_rut, rut):
        rut_limpio = rut.replace('.', '').replace('-', '')
        digito_verificador = rut_limpio[-1]
        numero_rut = rut_limpio[:-1]
        rut_invertido = numero_rut[::-1]

        multiplicador = 2
        suma = []

        for num in rut_invertido:
            multiplicacion = int(num) * multiplicador
            suma.append(multiplicacion)
            multiplicador += 1
            if multiplicador > 7:
                multiplicador = 2

        resto = sum(suma) % 11
        dig_ver_calc = 11 - resto

        if dig_ver_calc == 11:
            dig_ver_calc = '0'
        elif dig_ver_calc == 10:
            dig_ver_calc = 'K'
        else:
            dig_ver_calc = str(dig_ver_calc)

        if digito_verificador.lower() == dig_ver_calc.lower():
            mensaje = 'RUT válido'
            return rut, mensaje
        else:
            rut = ''
            mensaje = 'RUT inválido, ingrese nuevamente...\n'
    else:
        mensaje = 'Formato de RUT NO corresponde, ingrese nuevamente...\n'
        rut = ''
    return rut, mensaje


def validar_largo_string(valor, largo):
    if len(valor) > largo:
        mensaje = f'Su dato supera los {largo} caracteres permitidos, ingrese nuevamente...\n'
        valor = ''
    else:
        mensaje = 'Dato correcto\n'
    return valor, mensaje


def validar_correo(correo):
    patron_correo = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron_correo, correo):
        mensaje = 'Formato de correo válido.'
    else:
        mensaje = 'Formato de correo NO corresponde, ingrese nuevamente...'
        correo = ''
    return correo, mensaje


def validar_numero(valor):
    try:
        valor = int(valor)
        mensaje = 'Número Válido'
    except ValueError:
        valor = 0
        mensaje = 'Valor NO corresponde a un número, ingrese nuevamente...'
    return valor, mensaje


def validar_fecha(fecha_nacimiento):
    patron_fecha_nacimiento = r'^\b(0[1-9]|[12]\d|3[01])[/](0[1-9]|1[0-2])[/](19\d\d|20\d\d)\b$'
    if re.match(patron_fecha_nacimiento, fecha_nacimiento):
        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%d/%m/%Y')
            mensaje = 'Formato de fecha correcto'
        except ValueError:
            mensaje = 'Fecha Inválida, ingrese nuevamente...\n'
            fecha_nacimiento = ''
    else:
        mensaje = 'Fecha Inválida, ingrese nuevamente...\n'
        fecha_nacimiento = ''

    return fecha_nacimiento, mensaje


def validar_genero(genero):
    if genero not in ['1', '2', '3']:
        mensaje = 'Género Inválido'
        genero = ''
    else:
        mensaje = 'Género Válido'
    return genero, mensaje


def validar_contrasena(contrasena):
    errores = []

    if len(contrasena) < 8 or len(contrasena) > 15:
        errores.append("La contraseña debe tener entre 8 y 15 caracteres.")

    if not any(c.isupper() for c in contrasena):
        errores.append(
            "La contraseña debe contener al menos una letra mayúscula.")

    if not any(c.islower() for c in contrasena):
        errores.append(
            "La contraseña debe contener al menos una letra minúscula.")

    if not any(c.isdigit() for c in contrasena):
        errores.append("La contraseña debe contener al menos un número.")

    if not any(c in "!@#$%&/" for c in contrasena):
        errores.append(
            "La contraseña debe contener al menos uno de los siguientes caracteres especiales: !, @, #, $, %, &. /.")

    if len(errores) > 0:
        contrasena = ''

    return contrasena, errores