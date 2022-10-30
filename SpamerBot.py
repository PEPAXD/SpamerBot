from email.message import EmailMessage  #LIBRERIA GMAIL
import ssl                              #SEGURIDAD
import smtplib                          #COMANDOS ENVIO

#FUNCION IMPRIMIR CREDITOS AL PROGRAMADOR
def printCodeMaster():

    RED = '\033[31m'
    RESET = '\033[39m'

    print(RED + "\n EMAIL-SEND BY MAURO PEPA. V0.1"+ "\n--------------------------------" + RESET)

#FUNCION LOGGEAR CORREO Y ENVIAR CORREO
def signInEmail():

    # CUENTA GOOGLE EMISOR
    email_emisor = 'testsendvcp1@gmail.com'
    email_contrasena_ia = 'ytfgrmnsbfxnhvgp'
    # CONTRASEÑA EMAIL USUARIO = rejfxjufnvrl

    # CUENTAS GOOGLE RECEPTOR
    email_receptor = '' #EMAIL TARGET

    # DOCUMENTOS A ENVIAR
    asunto = 'FUNCIONA!!!'
    cuerpo = """El codigo funciona, INGRESE AL SIGUIENTE LINK ---> https://www.instagram.com/ambientevcp/?hl=es"""

    em = EmailMessage()         # CREO OBJETO
    em['From'] = email_emisor   # EMISOR
    em['To'] = email_receptor   # RECEPTOR
    em['Subject'] = asunto      # ASUNTO
    em.set_content(cuerpo)      # CUERPO DEL CORREO

    # CHEQUEO DE SEGURIDAD
    contexto = ssl.create_default_context()

    # CONECCION PYTHON CON CORREO EMISOR, N°PUERTO, PARAMETRO SEGURIDAD
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
        smtp.login(email_emisor, email_contrasena_ia)  # FUNCION LOGEARSE
        smtp.sendmail(email_emisor, email_receptor, em.as_string())  # FUNCION ENVIAR CORREO


#FUNCION MAIN
def main():
    printCodeMaster()
    signInEmail()

#EJECUTAR SCRIPT
if __name__ == '__main__':
    main()