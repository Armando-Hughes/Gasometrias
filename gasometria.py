"""
Creado por Armando Hughes
28/09/210
bibliografía: http://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S2448-89092018000300156
"""
import tkinter as tk
from tkinter import messagebox
def inicio ():
    """
    :return: iNTERFAZ GRÁFICA
    """
    ventana = tk.Tk()
    ventana.title('Interpretación de gasometrías')
    ventana.resizable(0, 0)
    ventana.geometry("500x400+350+100")
    ################# LABELS #####################
    LabelIND = tk.Label(ventana, text='Introduce los valores que se solicitan : ', fg="black",
                       font=("Arial black", 12))
    LabelIND.place(relx=0.07, rely=0.1)
    Labelph = tk.Label(ventana, text='pH : ', fg="black",
                        font=("Arial black", 12))
    Labelph.place(relx=0.10, rely=0.25)
    Labelpco2 = tk.Label(ventana, text='PCO2 : ', fg="black",
                       font=("Arial black", 12))
    Labelpco2.place(relx=0.10, rely=0.35)
    Labelbase = tk.Label(ventana, text='B(E) : ', fg="black",
                       font=("Arial black", 12))
    Labelbase.place(relx=0.10, rely=0.45)
    ######################## ENTRADAS ######################
    entradaph = tk.StringVar()
    entrada_entradaph = tk.Entry(ventana, textvar=entradaph, width=12, font=('Arial Black', 10),
                                  cursor='hand2', bg='light gray')
    entrada_entradaph.place(relx=0.4, rely=0.25)
    entradapco2 = tk.StringVar()
    entrada_entradapco2 = tk.Entry(ventana, textvar=entradapco2, width=12, font=('Arial Black', 10),
                                 cursor='hand2', bg='light gray')
    entrada_entradapco2.place(relx=0.4, rely=0.35)
    entradabase = tk.StringVar()
    entrada_entradabase = tk.Entry(ventana, textvar=entradabase, width=12, font=('Arial Black', 10),
                                 cursor='hand2', bg='light gray')
    entrada_entradabase.place(relx=0.4, rely=0.45)

    ############## FUNCIONES ######################
    def gasometria(ph, pco2, base):
        if ph >= 7.35 and ph <= 7.45:
            if pco2 >= 35 and pco2 <= 45:
                if base >= -2 and base <= 2:
                    return 'Gasometría normal'
                else:
                    if base < -2:
                        return 'Acidosis metabólica'
                    else:
                        return 'Alcalosis metabólica'
            else:
                if pco2 > 45 and base >= -2 and base <= 2:
                    return 'Acidosis respiratoria aguda'
                elif pco2 > 45 and (base < -2 or base > 2):
                    return 'Acidosis respiratoria crónica'
                else:
                    if base >= -2 and base <= 2:
                        return 'Alcalosis respiratoria aguda'
                    elif base < -2 or base > 2:
                        return 'Alcalosis respiratoria crónica'
        else:
            if ph > 7.45:
                if pco2 >= 35 and pco2 <= 45:
                    if base >= -2 and base <= 2:
                        return 'Alcalemia \n(probable \ncontaminación de \nmuestra)'
                    else:
                        return 'Alcalosis metabólica'
                elif pco2 < 35:
                    return 'Alcalosis respiratoria'
                elif pco2 > 45:
                    return 'Alcalosis mixta'
            elif ph < 7.35:
                if pco2 >= 35 and pco2 <= 45:
                    if base >= -2 and base <= 2:
                        return 'Acidemia \n(probable \ncontaminación de \nmuestra)'
                    else:
                        return 'Acidosis metabólica'
                elif pco2 > 45:
                    return 'Acidosis respiratoria'
                elif pco2 < 35:
                    return 'Acidosis mixta'
    def cerrar():
        ventana.destroy()
    def valores_normales():
        ventana1 = tk.Frame(ventana)
        ventana1.pack()
        ventana1.config(width=450, heigh=350)
        ventana1.place(relx=0, rely=0.1)

        def cerrar1():
            ventana1.destroy()

        l = """Valores normales de pH: de 7.35 a 7.45

                   Valores normales de PCO2: de 35 a 45 mmHg

                   Valores normales de B(E): de -2 a 2"""
        LabelIND = tk.Label(ventana1, text=l, fg="black",
                            font=("Arial black", 10))
        LabelIND.place(relx=0.07, rely=0.1)
        ################### botón ##################
        boton_salir1 = tk.Button(ventana1, cursor='hand2', text="REGRESAR", bg='light green',
                                 font=("Arial black", 10), width=10, height=2, command=cerrar1)
        boton_salir1.pack()
        boton_salir1.place(relx=0.4, rely=0.75)
        ventana1.mainloop()
    def programa():
        x = entradaph.get(); y = entradapco2.get(); z = entradabase.get()
        m = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w',
             'x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S',
             'T','U','V','W','X','Y','Z']
        m1 = x + y + z
        k = []
        for i in m1:
            if i in m:
                k.append(i)
        if x == '' or y=='' or z=='':
            messagebox.showwarning("Error", "TODOS LOS CAMPOS DEBEN ESTAR LLENOS")
        elif k != []:
            messagebox.showwarning("Error", "EL PROGRAMA NO ACEPTA LETRAS, \nSOLO NÚMEROS")
        else:
            x1 = float(entradaph.get())
            y1 = float(entradapco2.get())
            z1 = float(entradabase.get())

            l = gasometria(x1, y1, z1)

            ventana1 = tk.Frame(ventana)
            ventana1.pack()
            ventana1.config(width=450, heigh=350)
            ventana1.place(relx=0, rely=0.1)

            def cerrar1():
                ventana1.destroy()

            LabelIND = tk.Label(ventana1, text=l, fg="black",
                                font=("Arial black", 16))
            LabelIND.place(relx=0.25, rely=0.3)
            ################### botón ##################
            boton_salir1 = tk.Button(ventana1, cursor='hand2', text="ACEPTAR", bg='light green',
                                     font=("Arial black", 10), width=10, height=2, command=cerrar1)
            boton_salir1.pack()
            boton_salir1.place(relx=0.4, rely=0.75)
            ventana1.mainloop()
    def limpiar():
        entrada_entradaph.delete(0, 'end')
        entrada_entradapco2.delete(0, 'end')
        entrada_entradabase.delete(0, 'end')
    ###########  BOTONES ######################
    boton_salir = tk.Button(ventana, cursor='hand2', text="SALIR", bg='light green',
                              font=("Arial black", 10), width=10, height=2, command = cerrar)
    boton_salir.pack()
    boton_salir.place(relx=0.6, rely=0.75)

    boton_valores = tk.Button(ventana, cursor='hand2', text="VALORES \nNORMALES", bg='light yellow',
                            font=("Arial black", 8), width=10, height=2, command=valores_normales)
    boton_valores.pack()
    boton_valores.place(relx=0.7, rely=0.25)

    boton_aceptar = tk.Button(ventana, cursor='hand2', text="ACEPTAR", bg='light blue',
                                font=("Arial black", 10), width=10, height=2, command = programa)
    boton_aceptar.pack()
    boton_aceptar.place(relx=0.2, rely=0.75)

    boton_valores = tk.Button(ventana, cursor='hand2', text="LIMPIAR", bg='light yellow',
                              font=("Arial black", 8), width=10, height=2, command=limpiar)
    boton_valores.pack()
    boton_valores.place(relx=0.7, rely=0.45)

    ventana.mainloop()

inicio()