hora = int(input("Dame una hora: "))
minutosExtra = 24 * 5
hora += (minutosExtra//60)
minutosExtra %= 60
print(f"En 24h el reloj marcará las {hora}:{minutosExtra}")