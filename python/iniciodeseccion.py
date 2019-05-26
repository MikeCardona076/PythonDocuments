#Inicio de seccion 
users=['alberto','monica','carlos','santiago','alexandra']
contra=['13341','55031','23399','74542','88921']
correr=True

while correr:
    print("Ingresar sus credenciales")
    usuario=input("Ingresa el usuario  ")
    contrausuario=input("Ingresa la contrasena  ")

    if usuario in users and contrausuario in contra:
        print("Bien puede avanzar")

    else:
        print("Mal, vuelva a intentar")