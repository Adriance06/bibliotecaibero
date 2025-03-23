import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

users = [{"Nombre": "Manuel", "Correo": "manuel@gmail.com", "Celular": "3224455678"}]
books = [{"Titulo":"Cien años de soledad","Autor": "Gabriel Garcia","Genero":"Novela"}]
loans = [{"Nombre usuario": "Juan","Titulo libro":"La leyenda de yuripari","Fecha de prestamo": "2025-03-23"}]

#registrar usuario--------------------------------------------------------------------------------------
def windowuser():
    global window2
    window2 = tk.Toplevel()
    window2.geometry("600x600")
    window2.title("Registrar usuario")
    global txtname,txtmail,txtcell
    
    lbltl2 = tk.Label(window2, text="Digite los siguientes datos para hacer el registro")
    lbltl2.grid(row=0,column=1, pady=20, padx=20)
    lbl2_1 = tk.Label(window2, text="Nombre:")
    lbl2_1.grid(row=1,column=0, pady=20, padx=20)
    txtname = tk.Entry(window2)
    txtname.grid(row=1, column=1, pady=20, padx=20) 
    lbl2_2 = tk.Label(window2, text="Correo:")
    lbl2_2.grid(row=2,column=0, pady=20, padx=20)
    txtmail = tk.Entry(window2)
    txtmail.grid(row=2, column=1, pady=20, padx=20) 
    lbl2_3 = tk.Label(window2, text="Celular:")
    lbl2_3.grid(row=3,column=0, pady=20, padx=20)
    txtcell = tk.Entry(window2)
    txtcell.grid(row=3, column=1, pady=20, padx=20) 
    btnuser = tk.Button(window2, text="Registrar usuario", command=createuser)
    btnuser.grid(row=4, column=0, columnspan=2, pady=20, padx=20)
    btnvolver1 = tk.Button(window2, text="Volver al menu principal"command=lambda:window2.destroy())
    btnvolver1.grid(row=0,column=5,pady=20,padx=20)
    
    window2.mainloop()
#funcion creadora de usuario--------------------------------------------------------------------------------------
def createuser():
    regisuser = {"Nombre": txtname.get(), "Correo": txtmail.get(),"Celular": txtcell.get()}
    users.append(regisuser)
    messagebox.showinfo("Registro exitoso","Usuario registrado con exito")
    window2.lift()


#2- Registrar libro--------------------------------------------------------------------------------------
def windowbooks():
    global window3
    window3 = tk.Toplevel()
    window3.geometry("600x600")
    window3.title("Registrar libro")
    global txttitle,txtautor,txtgenero
    
    lbltl3 = tk.Label(window3, text="Digite los siguientes datos para hacer el registro del libro")
    lbltl3.grid(row=0,column=1, pady=20, padx=20)
    lbl3_1 = tk.Label(window3, text="Titulo:")
    lbl3_1.grid(row=1,column=0, pady=20, padx=20)
    txttitle = tk.Entry(window3)
    txttitle.grid(row=1, column=1, pady=20, padx=20) 
    lbl3_2 = tk.Label(window3, text="Autor:")
    lbl3_2.grid(row=2,column=0, pady=20, padx=20)
    txtautor = tk.Entry(window3)
    txtautor.grid(row=2, column=1, pady=20, padx=20) 
    lbl3_3 = tk.Label(window3, text="Genero:")
    lbl3_3.grid(row=3,column=0, pady=20, padx=20)
    txtgenero = tk.Entry(window3)
    txtgenero.grid(row=3, column=1, pady=20, padx=20) 
    btnbook = tk.Button(window3, text="Registrar Libro", command=createbook)
    btnbook.grid(row=4, column=0, columnspan=2, pady=20, padx=20)
    btnvolver2 = tk.Button(window3, text="Volver al menu principal"command=lambda:window3.destroy())
    btnvolver2.grid(row=0,column=5,pady=20,padx=20)
    
    window3.mainloop()
#funcion creadora de libro--------------------------------------------------------------------------------------
def createbook():
    regisbook = {"Titulo": txttitle.get(), "Autor": txtautor.get(),"Genero": txtgenero.get()}
    books.append(regisbook)
    messagebox.showinfo("Registro exitoso","Libro registrado con exito")
    window2.lift()

#--------------------------------------------------------------------------------------

#3-listar usuarios--------------------------------------------------------------------------------------
def listuser():
    window4 = tk.Toplevel()
    #window4.geometry("600x600")
    window4.title("Lista de usuarios")

    lbllistu = tk.Label(window4,text="Esta es la lista de usuarios registrados")
    lbllistu.grid(row=0,column=0,pady=20,padx=20)
    tableu = ttk.Treeview(window4,columns=("Nombre","Correo","Celular"),show="headings")
    tableu.heading("Nombre",text="Nombre") 
    tableu.heading("Correo",text="Correo") 
    tableu.heading("Celular",text="Celular") 
    
    for luser in users:
        tableu.insert("","end",values=(luser["Nombre"],luser["Correo"],luser["Celular"]))

    tableu.grid(row=1,column=0,pady=20,padx=20)
    btnvolver = tk.Button(window4, )
    window4.mainloop()

#--------------------------------------------------------------------------------------
#5- Listar libros--------------------------------------------------------------------------------------
def listbook():
    window6 = tk.Toplevel()
    #window4.geometry("600x600")
    window6.title("Lista de libros")

    lbllistu = tk.Label(window6,text="Esta es la lista de libros registrados")
    lbllistu.grid(row=0,column=0,pady=20,padx=20)
    tableu = ttk.Treeview(window6,columns=("Titulo","Autor","Genero"),show="headings")
    tableu.heading("Titulo",text="Titulo") 
    tableu.heading("Autor",text="Autor") 
    tableu.heading("Genero",text="Genero") 
    
    for lbook in books:
        tableu.insert("","end",values=(lbook["Titulo"],lbook["Autor"],lbook["Genero"]))

    tableu.grid(row=1,column=0,pady=20,padx=20)
    btnvolver = tk.Button(window6, )
    window6.mainloop()

#7- Registrar prestamo--------------------------------------------------------------------------------------
def windowloan():
    global window8, tablep
    window8 = tk.Toplevel()
    #window4.geometry("600x600")
    window8.title("Registrar prestamos")
    
    global txtnamepres,txttitlepres,txtfechapres
    
    lbl1p = tk.Label(window8, text="Digite los siguientes datos para hacer el registro del prestamo")
    lbl1p.grid(row=0,column=0, pady=20, padx=20)
    lbl2p = tk.Label(window8, text="Nombre del usuario:")
    lbl2p.grid(row=1,column=0, pady=20, padx=20)
    txtnamepres = tk.Entry(window8)
    txtnamepres.grid(row=1, column=1, pady=20, padx=20) 
    lbl3p = tk.Label(window8, text="Titulo del libro:")
    lbl3p.grid(row=2,column=0, pady=20, padx=20)
    txttitlepres = tk.Entry(window8)
    txttitlepres.grid(row=2, column=1, pady=20, padx=20) 
    lbl4p = tk.Label(window8, text="Fecha de prestamo:")
    lbl4p.grid(row=3,column=0, pady=20, padx=20)
    txtfechapres = tk.Entry(window8)
    txtfechapres.grid(row=3, column=1, pady=20, padx=20) 
    btnpres = tk.Button(window8, text="Registrar Prestamo", command=createloan)
    btnpres.grid(row=4, column=0, columnspan=2, pady=20, padx=20)
    btnvolverp = tk.Button(window8, text="Volver al menu principal", command=lambda:window8.destroy())
    btnvolverp.grid(row=4,column=1,pady=20,padx=20)
 
    lbllistu = tk.Label(window8,text="Esta es la lista de prestamos registrados")
    lbllistu.grid(row=5,column=0,pady=20,padx=20)
    tablep = ttk.Treeview(window8,columns=("Nombre usuario","Titulo libro","Fecha de prestamo"),show="headings")
    tablep.heading("Nombre usuario",text="Nombre usuario") 
    tablep.heading("Titulo libro",text="Titulo libro") 
    tablep.heading("Fecha de prestamo",text="Fecha de prestamo") 
    
    for lloan in loans:
        tablep.insert("","end",values=(lloan["Nombre usuario"],lloan["Titulo libro"],lloan["Fecha de prestamo"]))

    tablep.grid(row=6,column=0,pady=20,padx=20)
   
    window8.mainloop()

#funcion creadora de prestamo--------------------------------------------------------------------------------------
def createloan():
    regisloan = {"Nombre usuario": txtnamepres.get(), "Titulo libro": txttitlepres.get(),"Fecha de prestamo": txtfechapres.get()}
    loans.append(regisloan)
    messagebox.showinfo("Registro exitoso","Prestamo registrado con exito")
    window8.lift()
    reloadtablepres()
    
#funcion que recarga la tabla de prestamos--------------------------------------------------------------------------------------
def reloadtablepres():
    tablep.delete(*tablep.get_children())
    for lloan in loans:
        tablep.insert("","end",values=(lloan["Nombre usuario"],lloan["Titulo libro"],lloan["Fecha de prestamo"]))
#--------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------
#-Menu principal-------------------------------------------------------------------------------------

window = tk.Tk()
window.geometry("600x700")
window.title("Menu biblioteca")
    
lbl1 = tk.Label(window, text="Opciones")
lbl1.grid(row=0,column=0, pady=20, padx=20)
#-----------------------------------------------
btn1 = tk.Button(window, text="Registrar usuarios", command=windowuser)
btn1.grid(row=1,column=0,pady=20,padx=20)
#-----------------------------------------------
btn2 = tk.Button(window, text="Registrar libros", command=windowbooks)
btn2.grid(row=2,column=0,pady=20,padx=20)
#-----------------------------------------------
btn3 = tk.Button(window, text="Listar usuarios", command=listuser)
btn3.grid(row=3,column=0,pady=20,padx=20)
#-----------------------------------------------
btn4 = tk.Button(window, text="Buscar usuarios", command=createuser)
btn4.grid(row=4,column=0,pady=20,padx=20)
#-----------------------------------------------
btn5 = tk.Button(window, text="Listar libros", command=listbook)
btn5.grid(row=5,column=0,pady=20,padx=20)
#-----------------------------------------------
btn6 = tk.Button(window, text="Buscar libros", command=createuser)
btn6.grid(row=6,column=0,pady=20,padx=20)
#-----------------------------------------------
btn7 = tk.Button(window, text="Registrar prestamos", command=windowloan)
btn7.grid(row=7,column=0,pady=20,padx=20)
#-----------------------------------------------
btn8 = tk.Button(window, text="Registrar devoluciones", command=createuser)
btn8.grid(row=8,column=0,pady=20,padx=20)
#-----------------------------------------------
btn9 = tk.Button(window, text="Salir", command=window.quit)
btn9.grid(row=9,column=0,pady=20,padx=20)    
    
window.mainloop()    
    
