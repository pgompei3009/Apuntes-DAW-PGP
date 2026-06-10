hay_caracteres = hay_numeros = hay_simbolos = False

password = input('Introduce contraseña: ')

if len(password) > 7:
    for c in password:
        match c:
            case c if c.isalpha():
                hay_caracteres = True
            case c if c.isdigit():
                hay_numeros = True
            case c if not (c.isalnum() or c.isspace()):
                hay_simbolos = True

    if hay_caracteres == True and hay_numeros == False and hay_simbolos == False:
        print('Solo hay caracteres alfabéticos.')
    elif hay_caracteres == False and hay_numeros == True and hay_simbolos == False:
        print('Solo hay dígitos.')
    elif hay_caracteres == True and hay_numeros == True and hay_simbolos == False:
        print('La contraseña no tiene simbolos.')
    elif hay_caracteres == False and hay_numeros == False and hay_simbolos == True:
        print('Solo hay símbolos.')
    elif hay_caracteres == True and hay_numeros == False and hay_simbolos == True:
        print('La contraseña no tiene dígitos.')
    elif hay_caracteres == False and hay_numeros == True and hay_simbolos == True:
        print('Hay dígitos y símbolos.')
    elif hay_caracteres == True and hay_numeros == True and hay_simbolos == True:
        print('La contraseña es segura!')
else:
    print('La contraseña debe tener más de 7 caracteres')