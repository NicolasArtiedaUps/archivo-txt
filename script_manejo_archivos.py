# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
from tkinter import scrolledtext 

ventana=tk.Tk()
ventana.geometry("300x400")
txt_entrada=tk.Entry(ventana)
txt_entrada.pack()

def actualizar():
    contenido2=txt_entrada.get()
    scroll_text.insert(tk.END,contenido2)
    
    contenido2=scroll_text.get("1.0",tk.END)
    file=open("archivo.txt","w")
    file.write(contenido2)
    
btn_boton=tk.Button(ventana,text="GUARDAR",command=actualizar)
btn_boton.pack()



scroll_text=scrolledtext.ScrolledText(ventana,width=50,height=10)
scroll_text.pack()
documento="archivo.txt"
with open(documento,"r") as archivo:
    contenido=archivo.read()
scroll_text.insert("1.0", contenido)





ventana.mainloop()