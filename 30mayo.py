import tkinter as tk

def nico():
    label.config(text='No lo se aun ajaajajaj, pero se que te va amaar muuchoo, tanto como yo a ti.')
    

#crear ventana
ventana = tk.Tk()

# creamos titulo
ventana.title('Valentina Perez')

#tamaño de la ventana
ventana.geometry('500x300')

label = tk.Label(ventana,text='Vas a ser la mejor mama del mundo, te amo mi vida.', font= ('Times New Roman', 16))
label.pack(pady= 20)
#Crear botn
boton = tk.Button(ventana, text='Quieres saber que dice Nico?', command= nico)
boton.pack(pady=50)




#crear ventana lllamar ventana
ventana.mainloop()
