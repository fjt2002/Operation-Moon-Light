from tkinter import *


#########################################################################

def AnimacionRecursiva(contador,img,can,x): #Funcion recursiva que hace posible que la animacion funcione y se proyecte 
    if contador>12: 
        contador=1
    nombre=".\ImagenesAnimacion\\Img"+str(contador)+".gif"
    img = PhotoImage(file=nombre)
    can.create_image(x, 20, image=img, anchor=NW,tag="img")
    can.pack()
    can.update()

    contador+=1
    x=x+10
    if x>=900:
        x=10
    time.sleep(0.04) 
    can.delete("img")
    return AnimacionRecursiva(contador,img,can,x)

#########################################################################

def Animacion():
    win.minsize(900,450)
    win.resizable(width=NO,height=NO)
    win.title("Animacion")
    img = PhotoImage(file=".\ImagenesAnimacion\Img.gif")
    can = Canvas(win, width=900, height=450, bg="white")
    can.grid()
    contador=1
    x=20
    AnimacionRecursiva(contador,img,can,x)
    icon = PhotoImage(file='.\Imagenes\\Pixels.gif')
    win.mainloop()

#####################################################################

def About():
    a=Toplevel(bg="dark gray")#crea una ventana con fondo de color
    
    a.minsize(800,700)
    a.resizable(width=NO,height=NO)
    a.title("Info")
    instruccion=Label(a,text="En esta sección encontrará información de mi programador. ",bg="dark gray",justify="left",relief="flat") 
    instruccion.place(x=0,y=0)
    instruccion2=Label(a,text="El nombre completo y Carnet de mi programador es: Froylan Jimenez (2021436946).",bg="dark gray",justify="left",relief="flat")
    instruccion2.place(x=0,y=40)
    instruccion3=Label(a,text="La edad y el Genero de mi programador es:   18 años, Masculino. (Es mayor de edad y es Hombre)",bg="dark gray",justify="left",relief="flat") 
    instruccion3.place(x=0,y=80)
    instruccion4=Label(a,text="El deporte o juego preferido del programador:   Futbol, Juegos de Historia(The witcher)entre otros.",bg="dark gray",justify="left",relief="flat")
    instruccion4.place(x=0,y=120)
    instruccion5=Label(a,text="Direccion: Perez Zeledon/San Jose/ Costa Rica .",bg="dark gray",justify="left",relief="flat")
    instruccion5.place(x=0,y=160)
    instruccion6=Label(a,text="Ahora les mostraré una foto de mi programador.",bg="dark gray",justify="left", relief="flat")
    instruccion6.place(x=0,y=200)
    instrImg7=PhotoImage(file=".\Imagenes\\Yo.png")
    instruccion7=Label(a,image=instrImg7)
    instruccion7.place(x=0,y=235)
    instrImg8=PhotoImage(file=".\Imagenes\\Ubicación.png")
    instruccion8=Label(a,image=instrImg8)
    instruccion8.place(x=350,y=500)
    instruccion9=Label(a,text="Imagen de mi lugar donde vivo: es un poco caluroso pero es muy atractivo por su vegetación en exceso.",bg="dark gray",justify="left",relief="flat")
    instruccion9.place(x=305,y=465)
    instrImg10=PhotoImage(file=".\Imagenes\\Futbol.png")
    instruccion10=Label(a,image=instrImg10)
    instruccion10.place(x=400,y=250)
    instruccion11=Label(a,text="Futbol: Deporte mas hermoso del mundo y el mas visto por todos",bg="dark gray",justify="left",relief="flat")
    instruccion11.place(x=410,y=215)
    instruccion12=Label(a,text="Canción favorita:",bg="dark gray",justify="left",relief="flat")
    instruccion12.place(x=10,y=600)
    a.mainloop()# para que funcione la ventana



######################################################################    
ventana = Tk()
ventana.title("Interfaz Graficaa")
ventana.minsize(800,375)
ventana.resizable(width=NO,height=NO)
icon = PhotoImage(file='.\Imagenes\\Pixels.gif')
ventana.tk.call('wm', 'iconphoto', ventana._w, icon)
imagen1 = PhotoImage(file=".\Imagenes\\Fondo.png")
LabelFondo=Label(ventana,image=imagen1)
LabelFondo.place (x=0, y=0)
numero=Entry(ventana,width=25,bg="Yellow")
numero.place(x=150,y=100)
titulo=Label(ventana,text="INTRODUZCA CUALQUIER NUMERO FIBONACCI ENTRE '0' Y '144'",bg="white")
titulo.place(x=150,y=60)
######################################################################
menubar=Menu(ventana)
menubar.add_command(label="ID Personal",command=About)
menubar.add_command(label="Animacion",command=Animacion)
ventana.config(menu=menubar)
deleviaje=Button(ventana,text="Aceptar", bg="Yellow", fg="black")
deleviaje.place(x=165,y=220)
ventana.mainloop()

