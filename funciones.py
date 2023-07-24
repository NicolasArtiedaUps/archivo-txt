# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 14:12:06 2023

@author: lab
"""
import script_manejo_archivos

##funciones 
def insertar_texto():
    contenido=script_manejo_archivos.txt_entrada.get()
    script_manejo_archivos.scroll_text.insert(script_manejo_archivos.tk.end,contenido)