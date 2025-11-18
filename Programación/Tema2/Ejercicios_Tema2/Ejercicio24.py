usuario = input("Introduce el usuario: ")
contrasenhaConfirmada = False

while not contrasenhaConfirmada:
    contrasenha = input("Introduce la contraseña: ")
    confirmacionContrasenha = input("Introduce la contraseña de nuevo: ")
    if confirmacionContrasenha != contrasenha:
        print("Las contraseñas no coinciden")
    else:
        confirmacionContrasenha = True

print("Usuario creado correctamente")