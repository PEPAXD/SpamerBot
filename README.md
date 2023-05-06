SpamBot
This Python script allows you to send mass emails to a list of recipients. It includes a file named file.txt that contains a brief introduction text and a link to a drive to send our digital portfolio and resume. Additionally, an Excel file containing the data of the companies to which we wish to send the curriculum is attached.

This script simplifies the process of sending resumes to various companies. Developed by Mauro Pepa, the script enables you to send emails to multiple companies in a single transaction.

Dependencies
ssl
smtplib
tkinter
customtkinter
pandas
Functions
readExcel(file_path)
Extracts data from an Excel file and returns a pandas DataFrame.

signInEmail(email_list, asunto, cuerpo)
Logs into the email account and sends emails to the list of recipients provided as an argument.

GUI
The GUI has the following components:

Textbox with the description of the script.
Add CV button to select the file to attach to the email.
Checkbox frame to select the recipients.
Send button to send emails to the selected recipients.
Usage
Fill the file named file.txt with your brief introduction text and link to a drive to send your digital portfolio and resume.
Fill the Excel file with the data of the companies you want to send the curriculum to.
Run the SpamBot.py script and select the file.txt file and the Excel file.
Select the recipients in the Checkbox frame and click the Send button.
Note: Before running the script, ensure that the dependencies are installed on your system.
