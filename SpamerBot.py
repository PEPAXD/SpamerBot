from email.message import EmailMessage  #LIBRERIA GMAIL
import ssl                              #SEGURIDAD
import smtplib                          #COMANDOS ENVIO

#FUNCION IMPRIMIR CREDITOS AL PROGRAMADOR
def printCodeMaster():

    RED = '\033[31m'
    RESET = '\033[39m'

    print(RED + "\n EMAIL-SEND BY MAURO PEPA. V0.2"+ "\n--------------------------------" + RESET)

#FUNCION ADD TARGET EMAILS USERS
def targetUser():

    name_list = []
    email_list = []
    name = None

    print("PRESS X TO FINISH AND SEND EMAILS")
    while name != "x":

        name = input("\nNombre usuario: ")

        if(name == "x"):
            break
        else:
            name_list.append(name)

        email = input("Email usuario: ")
        email_list.append(email)

    return email_list

#FUNCION LOGGEAR CORREO Y ENVIAR CORREO
def signInEmail(email_list):

    # CUENTA GOOGLE EMISOR
    email_emisor = 'testsendvcp1@gmail.com'
    email_contrasena_ia = 'ytfgrmnsbfxnhvgp'
    # CONTRASEÑA EMAIL USUARIO = rejfxjufnvrl

    # DOCUMENTOS A ENVIAR
    asunto = 'FUNCIONA!!!'
    cuerpo = """INGRESE AL SIGUIENTE LINK ---> https://www.instagram.com/ambientevcp/?hl=es"""

    # CHEQUEO DE SEGURIDAD
    contexto = ssl.create_default_context()

    count = 0
    while count<len(email_list):

        # CREO OBJETO
        em = EmailMessage()
        em['From'] = email_emisor   # EMISOR
        em['Subject'] = asunto      # ASUNTO
        em.set_content(cuerpo)      # CUERPO DEL CORREO

        # CUENTAS GOOGLE RECEPTOR
        email_receptor = email_list[count]
        em['To'] = email_receptor   # RECEPTOR

        # CONECCION PYTHON CON CORREO EMISOR, N°PUERTO, PARAMETRO SEGURIDAD
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
            smtp.login(email_emisor, email_contrasena_ia)  # FUNCION LOGEARSE
            smtp.sendmail(email_emisor, email_receptor, em.as_string())  # FUNCION ENVIAR CORREO

        count += 1


#FUNCION MAIN
def main():
    printCodeMaster()
    email_list = targetUser()
    signInEmail(email_list)

#EJECUTAR SCRIPT
if __name__ == '__main__':
    main()