import ssl
import smtplib
import tkinter
import customtkinter
import pandas as pd

from email.message import EmailMessage
from tkinter import filedialog, messagebox


#FUNCION READ EXCEL
def readExcel(file_path):
    #Extract Database
    excelData = pd.read_excel(file_path)
    return excelData

#FUNCION LOGGEAR CORREO Y ENVIAR CORREO
def signInEmail(email_list, asunto, cuerpo):

    # CUENTA GOOGLE EMISOR
    email_emisor = 'testsendvcp1@gmail.com'
    email_contrasena_ia = 'ytfgrmnsbfxnhvgp'
    # CONTRASEÑA EMAIL USUARIO = rejfxjufnvrl

    # CHEQUEO DE SEGURIDAD
    contexto = ssl.create_default_context()

    # CICLO PARA ENVIAR CORREOS
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

#GUI CHECKBOX
class ScrollableCheckBoxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.checkbox_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        checkbox = customtkinter.CTkCheckBox(self, text=item)
        checkbox.select()
        if self.command is not None:
            checkbox.configure(command=self.command)
        checkbox.grid(row=len(self.checkbox_list), column=0, pady=(0, 10), padx=10, sticky="w")
        self.checkbox_list.append(checkbox)

    def get_checked_items(self):
        return [checkbox.cget("text") for checkbox in self.checkbox_list if checkbox.get() == 1]

#GUI MAIN
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window appearance
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        # configure window title
        self.title("SpamBot by-MauroPepa.py")

        # configure window size
        self.geometry(f"{400}x{450}")
        self.resizable(False, False)

        # create canvas
        self.frame = customtkinter.CTkFrame(master=self, corner_radius=30)
        self.frame.pack(fill="both", expand=True)
        self.frame.place(relx=0.07, rely=0.07, relwidth=0.87, relheight=0.87)

        # TEXT-LABEL
        self.label = customtkinter.CTkLabel(master=self.frame, text="_____SPAM-BOT_____", font=("Arial Black", 24, "underline"))
        self.label.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.frame, width=300, height=280, wrap="word")
        self.textbox.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # print loremText in textbox
        README = "Este script es un 'SpamBot' desarrollado en Python, que permite enviar correos electrónicos masivamente a una lista de destinatarios." \
                 "\nAdjuntamos un archivo file.txt con un breve texto a modo de presentacion junto con un link de drive para enviar por correo nuestro portafolio digital y curriculum." \
                 "\nDespues adjuntamos un archivo excel con los datos de la empresas a las que deseamos enviar el curriculum." \
                 "\nEste script permite enviar correos a varias empresas en una sola transaccion." \
                 "\nEste script fue desarrollado con el fin de simplificar el proceso de enviar curriculums a varias empresas. creado por Mauro Pepa con el fin de simplificar el proceso."
        self.textbox.insert("0.0", README)

        # make textbox read-only
        self.textbox.configure(state='disabled')

        # create button Add CV
        self.select_button = customtkinter.CTkButton(self.frame, width=300 ,text="ADD CV", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.select_CV)
        self.select_button.place(relx=0.5, rely=0.92, anchor=tkinter.CENTER)

    def checkbox_frame_event(self):
        self.scrollable_checkbox_frame.get_checked_items()

    def select_CV(self):

        file_pathTextFile = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        with open(file_pathTextFile, "r", encoding="utf-8") as file:
            blogFileFirstLine_Text = file.readline().rstrip()
            blogFileText = file.read()

        #DESTROY MainTextBox
        self.textbox.destroy()

        # create Input Textbox A
        self.textbox = customtkinter.CTkTextbox(self.frame,  width=300, height=20)
        self.textbox.place(relx=0.5, rely=0.18, anchor=tkinter.CENTER)
        self.textbox.insert("1.0", blogFileFirstLine_Text)

        # create textbox
        self.textbox2 = customtkinter.CTkTextbox(self.frame, width=300, height=250, wrap="word")
        self.textbox2.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
        self.textbox2.insert("1.0", blogFileText)

        # print loremText in textbox
        README = ""
        self.textbox.insert("0.0", README)

        # create button Add excel
        self.select_button.destroy()
        self.select_button = customtkinter.CTkButton(self.frame, width=300 ,text="ADD EMAILS", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.select_excel)
        self.select_button.place(relx=0.5, rely=0.92, anchor=tkinter.CENTER)

    def select_excel(self):
        # open file dialog and get file path
        file_pathEMAILS = filedialog.askopenfilename(filetypes=[("EXCEL Files", "*.xlsx")])
        dataExcel = readExcel(file_pathEMAILS)
        dataEmail = dataExcel['Dirección de correo eléctronico']

        # create scrollable checkbox frame
        self.scrollable_checkbox_frame = ScrollableCheckBoxFrame(master=self, width=300,  height=280, command=self.checkbox_frame_event,
                                                                 item_list=[dataEmail[i] for i in range(len(dataExcel))])
        self.scrollable_checkbox_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # create button send Spam
        self.select_button = customtkinter.CTkButton(self.frame, width=300, text="SEND SPAM", command=self.sendSpam)
        self.select_button.place(relx=0.5, rely=0.92, anchor=tkinter.CENTER)

    def sendSpam(self):
        dataEmail = self.scrollable_checkbox_frame.get_checked_items()
        Asunto = self.textbox.get("1.0", "end-1c")
        MainText = self.textbox2.get("1.0", "end-1c")

        if dataEmail == []:
            messagebox.showerror("ERROR", "NO HA SELECCIONADO NINGUN CORREO")
        else:
            signInEmail(dataEmail, Asunto, MainText)
            messagebox.showinfo("SpamerBot", "Correos enviados!!!")
            exit()


#EXECUTE CODE
if __name__ == "__main__":
    app = App()
    app.mainloop()