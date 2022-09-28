
from tkinter import ttk
import numpy as np
import tkinter
from tkinter import CENTER, END, RIGHT, W, Tk, filedialog
from tkinter.ttk import*
from tkinter.tix import*
from PIL import ImageTk,Image

'''   Nombre Funcion: openFile()
      Objetivo:       Permitir al usuario abrir una imagen de diferente tipo.
      Parametros:     file -> tipo de imagen
      Retorno:        No aplica
      Ejemplo:        Al momento de interactuar con el usuario, le preguntara que tipo de imagen quiere escoger, además abrirá y encontrará todos los 
                      tipos de imagen disponibles y compatibles dentro de la carpeta seleccionada
'''

#Función que explora el sistema de archivos además del tipo de archivo necesario.
#Retorna: Ruta del fichero seleccionado.
def openFile():
    file = filedialog.askopenfilename(filetypes=[
        ('Image Files JPG/JPEG', '*jpg'),
        ('Image Files JPG/JPEG', '*jpeg'),
        ('Image Files PNG', '*png'),
        ('Image Files GIF', '*gif')
    ])
    if (file != None and file != ""):
        txtImage.delete(0, END)
        txtImage.insert(0, file)
    return file

'''   Nombre Funcion:   uploadImage()
      Objetivo:         permitir a un usuario cargar una imagen al visor
      Parametros:       path -> recibe la funcion openImage() para obtener el formato
                        photo -> abre la imagen y la redimensiona
      Retorno:          No aplica
      Ejemplo:          Muestra la imagen en el visor cuando se llama la funcion.
'''

#Procedimiento para la carga de la imagen en la ventana tipo tk
def uploadImage():
    path = openFile()
    path = txtImage.get()
    photo = Image.open(path)
    photo = photo.resize((700, 500), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(photo)
    showImage.configure(image=photo)
    appVisor.mainloop()

'''   Nombre Funcion:   brightness()
      Objetivo:         ajusta brillo de la imagen dependiendo del valor dado por el usuario
      Parametros:       brightness -> variable que toma el valor que usuario manda
                        imgCopy -> se reliza una copia de la imagen subida, y sobre esa imagen se hacen los ajustes se redimensiona en el visor
      Retorno:          No aplica
      Ejemplo:          Muestra la imagen modoficada en el visor mientras se realizan los cambios cuando el usuario interactua con la variable brightness
'''

#Modificar Brillo de la imagen:
def brightness():
    brightness = 0
    brightness = float(brightnessControl.get())
    imgCopy = np.asarray(Image.open(txtImage.get()))
    imgCopy = imgCopy + brightness
    imgCopy = Image.fromarray(np.uint8(imgCopy))
    imgCopy = imgCopy.resize((700, 500), Image.ANTIALIAS)
    imgCopy = ImageTk.PhotoImage(imgCopy)
    showImage.configure(image=imgCopy)
    appVisor.mainloop()

'''   Nombre Funcion:   contrast()
      Objetivo:         ajusta contraste de la imagen dependiendo del valor dado por el usuario
      Parametros:       contrast -> variable que toma el valor que usuario manda
                        imgCopy -> se reliza una copia de la imagen subida, y sobre esa imagen se hacen los ajustes se redimensiona en el visor
      Retorno:          No aplica
      Ejemplo:          Muestra la imagen modoficada en el visor mientras se realizan los cambios cuando el usuario interactua con la variable contrast
'''

#Modificar Contraste de la imagen:
def contrast():
    contrast = 0
    contrast = float(contrastControl.get())
    img = np.asarray(Image.open(txtImage.get()))
    imgCopy = contrast*(np.log10(1+img))
    imgCopy = Image.fromarray(np.uint8(imgCopy))
    imgCopy = imgCopy.resize((700, 500), Image.ANTIALIAS)
    imgCopy = ImageTk.PhotoImage(imgCopy)
    showImage.configure(image=imgCopy)
    appVisor.mainloop()

'''   Nombre Funcion:   originalImage()
      Objetivo:         muestra al usuario como se ve la imagen original en caso de no querer cambios
      Parametros:       img -> abre nuevamente la imagen y la reemplaza por la imagen editada que estaba puesta al momento de darle en el boton de aplicar
      Retorno:          No aplica
      Ejemplo:          Muestra la imagen original al momento de que el usuario selecciona la opcion y le da en aplicar 
'''

#!Funciones tipos de Imagen:
#*Funcion para imagen original:
def originalImage():
    print('Estoy en la funcion ')
    img = np.asarray(Image.open(txtImage.get()))
    img = Image.fromarray(np.uint8(img))
    img = img.resize((700, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    showImage.configure(image=img)
    appVisor.mainloop()

'''   Nombre Funcion:   invertedImage()
      Objetivo:         mostrar al usuario una imagen invertida cuando se aplican los cambios
      Parametros:       img -> abre nuevamente la imagen original.
                        factor -> factor de conversion para la imagen invertida
                        InvImg -> captura y hace la conversion de la imagen. Además la reemplaza por la imagen que este en el espacio del visor
      Retorno:          No aplica
      Ejemplo:          Al momento del usuario seleccionar la opcion de imagen invertida y darle en el boton de aplicar, este le mostrara en pantalla como 
                        se veria la imagen con sus colores invertidos
'''

#*Funcion para imagen invertida:
def invertedImage():
    factor = 255
    img = np.asarray(Image.open(txtImage.get()))
    InvImg = np.copy(img)
    InvImg = factor - InvImg
    InvImg = Image.fromarray(np.uint8(InvImg))
    InvImg = InvImg.resize((700, 500), Image.ANTIALIAS)
    InvImg = ImageTk.PhotoImage(InvImg)
    showImage.configure(image=InvImg)
    appVisor.mainloop()

'''   Nombre Funcion:   grayScale()
      Objetivo:         mostrar al usuario la escala de grises de la imagen
      Parametros:       img -> abre nuevamente la imagen original.
                        grayImg -> copia la imagen dada y la divide en R, G, B para sacarle los colores, ademas de hacer su conversion y mostrarla en pantalla como queda
      Retorno:          No aplica
      Ejemplo:          Al momento del usuario seleccionar la opcion de escala de grises y darle en el boton de aplicar, este le mostrara en pantalla como 
                        se veria la imagen con su escala de grises 
'''

#*Funcion para la escala de grises:
def grayScale():
    img = np.asarray(Image.open(txtImage.get()))
    grayImg = np.copy(img)

    R = grayImg[:,:,0]
    G = grayImg[:,:,1]
    B = grayImg[:,:,2]

    grayImg = 0.2989 * R + 0.5870 * G + 0.1140 * B
    grayImg = Image.fromarray(np.uint8(grayImg))
    grayImg = grayImg.resize((700, 500), Image.ANTIALIAS)
    grayImg = ImageTk.PhotoImage(grayImg)
    showImage.configure(image=grayImg)
    appVisor.mainloop()

'''   Nombre Funcion:   binarized()
      Objetivo:         mostrar al usuario la imagen binarizada 
      Parametros:       img -> abre nuevamente la imagen original.
                        factor -> factor de conversion para la imagen binarizada
                        grayImg -> copia la imagen dada y la divide en R, G, B para sacarle los colores, ademas de hacer su conversion y mostrarla en pantalla como queda
      Retorno:          No aplica
      Ejemplo:          Al momento del usuario seleccionar la opcion de binarizada y darle en el boton de aplicar, este le mostrara en pantalla como 
                        se veria la imagen con su forma binarizada
'''

#*Funcion para imagen binarizada:
def binarized():
    factor = 20
    img = np.asarray(Image.open(txtImage.get()))
    grayImg = np.copy(img)

    R = grayImg[:,:,0]
    G = grayImg[:,:,1]
    B = grayImg[:,:,2]

    grayImg = 0.2989 * R + 0.5870 * G + 0.1140 * B
    binImg = (grayImg < factor) * 255
    binImg = Image.fromarray(np.uint8(binImg))
    binImg = binImg.resize((700, 500), Image.ANTIALIAS)
    binImg = ImageTk.PhotoImage(binImg)
    showImage.configure(image=binImg)
    appVisor.mainloop()

'''   Nombre Funcion:   colorRed(), colorGreen(), colorBlue()... etc
      Objetivo:         mostrar al usuario la imagen en sus diferentes tonos de colores RGB y CMYK
      Parametros:       img -> abre nuevamente la imagen original.
                        imgColor -> divide la imagen segun el color y lo muestra en el visor
      Retorno:          No aplica
      Ejemplo:          Al momento del usuario seleccionar la opcion de 'color' y darle en el boton de aplicar, este le mostrara en pantalla como 
                        se veria la imagen con su forma 'color' seleccionado
'''

#!Colores imagen:--------------------------------------------------------------------------------
def colorRed():
    print('Llego a funcion colores. ')
    img = np.asarray(Image.open(txtImage.get()))

    imgRed = np.copy(img)
    imgRed[:,:,1]=0
    imgRed[:,:,2]=0

    imgRed = Image.fromarray(np.uint8(imgRed))
    imgRed = imgRed.resize((700, 500), Image.ANTIALIAS)
    imgRed = ImageTk.PhotoImage(imgRed)
    showImage.configure(image=imgRed)
    appVisor.mainloop()

def colorGreen():
    print('Llego a funcion colores. ')
    img = np.asarray(Image.open(txtImage.get()))

    imgCopy = np.copy(img)
    imgCopy[:,:,0]=0
    imgCopy[:,:,2]=0

    imgCopy = Image.fromarray(np.uint8(imgCopy))
    imgCopy = imgCopy.resize((700, 500), Image.ANTIALIAS)
    imgCopy = ImageTk.PhotoImage(imgCopy)
    showImage.configure(image=imgCopy)
    appVisor.mainloop()

def colorBlue():
    print('Llego a funcion colores. ')
    img = np.asarray(Image.open(txtImage.get()))

    imgCopy = np.copy(img)
    imgCopy[:,:,0]=0
    imgCopy[:,:,1]=0

    imgCopy = Image.fromarray(np.uint8(imgCopy))
    imgCopy = imgCopy.resize((700, 500), Image.ANTIALIAS)
    imgCopy = ImageTk.PhotoImage(imgCopy)
    showImage.configure(image=imgCopy)
    appVisor.mainloop()

def colorCyan():
    print('Llego a funcion colores. ')
    img = np.asarray(Image.open(txtImage.get()))

    imgCopy = np.copy(img)
    imgCopy[:,:,0]=0

    imgCopy = Image.fromarray(np.uint8(imgCopy))
    imgCopy = imgCopy.resize((700, 500), Image.ANTIALIAS)
    imgCopy = ImageTk.PhotoImage(imgCopy)
    showImage.configure(image=imgCopy)
    appVisor.mainloop()

def colorMagenta():
    print('Llego a funcion colores. ')
    img = np.asarray(Image.open(txtImage.get()))

    imgCopy = np.copy(img)
    imgCopy[:,:,1]=0

    imgCopy = Image.fromarray(np.uint8(imgCopy))
    imgCopy = imgCopy.resize((700, 500), Image.ANTIALIAS)
    imgCopy = ImageTk.PhotoImage(imgCopy)
    showImage.configure(image=imgCopy)
    appVisor.mainloop()

def colorYellow():
    print('Llego a funcion colores. ')
    img = np.asarray(Image.open(txtImage.get()))

    imgCopy = np.copy(img)
    imgCopy[:,:,2]=0

    imgCopy = Image.fromarray(np.uint8(imgCopy))
    imgCopy = imgCopy.resize((700, 500), Image.ANTIALIAS)
    imgCopy = ImageTk.PhotoImage(imgCopy)
    showImage.configure(image=imgCopy)
    appVisor.mainloop()
#!------------------------------------------------------------------------------------------------

'''   Nombre Funcion:   updateImage()
      Objetivo:         editar la imagen acorde a lo solicitado por el usuario en el menu de opciones lateral
      Parametros:       num -> recibe un parametro tipo num, que es quien captura la opcion solicitada en el apartado de botones
      Retorno:          No aplica
      Ejemplo:          El usuario selecciona una opcion, esta opcion se guarda en num, y numescoge la opcion acorde al numero del if, asi, hace llamado a las funciones
                        descritas en la parte superior
'''


#Muestra la copia de la imagen creada con los cambios aplicados:
def updateImage(num):
    if num == 0:
        pass
    elif num == 1:
        brightness()
    elif num == 2:
        contrast()
    elif num == 3: 
        print('Funciono')
        print(imageTypeControl.get())
        selection = imageTypeControl.get()
        if selection == 'Original':
            print('Volvere la imagen Original...')
            originalImage()
        if selection == 'Invertida':
            print('Volvere la imagen Invertida...')
            invertedImage()
        if selection == 'Escala grises':
            print('Volvere la imagen Escala grises...')
            grayScale()
        if selection == 'Binarizada':
            print('Volvere la imagen Binarizada...')
            binarized()

#Creacion de la ventana tipo Tkinter:
appVisor = Tk()
appVisor.geometry('1210x620')
appVisor.title("Visor de imagenes. Programado por: Brandon David Palacio Alvarez.")
appVisor.configure(bg='#006')

labelTittle = tkinter.Label(appVisor, text='Visor de Imágenes', bg='#006', fg='#FFF', font=("Verdana", 30), anchor=CENTER, justify=CENTER)
labelTittle.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

###############################################################################################################################################################
#                                                                                                                                                             #
#                                                APARTADO DE BOTONES Y ACCESORIOS EN PANTALLA                                                                 #
#                                                                                                                                                             #
###############################################################################################################################################################

#Input donde irá la ruta del archivo:
txtImage = tkinter.Entry(appVisor, width=90, background='#BAD6F3', foreground='#064238', justify=['center'])
txtImage.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

#Boton que buscará la imagen en el pc:
buttonSearch = tkinter.Button(appVisor, cursor='hand2',text='Cargar Imagen:', width=20, command=lambda:uploadImage(), font=("Verdana", 10), bg='#009', fg='white')
buttonSearch.grid(row=2, column=0, padx=7, sticky=W)

#Espacio donde se va mostrar la imagen:
showImage = tkinter.Label(image="", border=4, cursor="X_cursor",background='#BAD6F3', text="\n\n\n<< Imagen >>\n\n\n", foreground='white', anchor=CENTER, justify=CENTER, font=("Verdana", 45))
showImage.grid(row=3, column=1, rowspan=100, columnspan=3, padx=5, pady=5)

#!Configuracion:
configuratioTextLabel = tkinter.Label(appVisor, text='Configuración de', font=("Verdana", 16), fg='#FFF', bg='#006')
configuratioTextLabel.grid(row=2, column=5)
configuratioTextLabel2 = tkinter.Label(appVisor, text='la Imagen:', font=("Verdana", 16), fg='#FFF', bg='#006')
configuratioTextLabel2.grid(row=2, column=6)    

#Controles de brillo en pantalla:
brightnessLabel = tkinter.Label(appVisor, text='Brillo', font=("Verdana", 10), bg='#006', fg='#FFF')
brightnessControl = tkinter.Spinbox(appVisor, from_=-20.0, to=20.0, increment=1.0, width=5, background='#BAD6F3', command=lambda:updateImage(1))
brightnessControl.grid(row=4, column=6, padx=2, pady=5)
brightnessLabel.grid(row=4, column=5, padx=2, pady=5)

#Controles de contraste en pantalla:
contrastLabel = tkinter.Label(appVisor, text='Contraste', font=("Verdana", 10), bg='#006', fg='#FFF')
contrastControl = tkinter.Spinbox(appVisor, from_=80, to=1000, increment=10.0, width=5, background='#BAD6F3', command=lambda:updateImage(2))
contrastControl.grid(row=5, column=6, padx=2, pady=5)
contrastLabel.grid(row=5, column=5, padx=2, pady=5)

#Controles tipo imagen:
imageTypeLabel = tkinter.Label(appVisor, text='Tipo de Imagen', font=("Verdana", 10), bg='#006', fg='#FFF')
imageTypeControl = ttk.Combobox(appVisor, values=('Original','Invertida','Escala grises','Binarizada'), width=15, background='#BAD6F3')
buttonApply = tkinter.Button(appVisor, command=lambda:updateImage(3), text='Aplicar', width=12, font=("Verdana", 10), bg='#009', fg='white', cursor='hand2')
buttonApply.grid(row=7, column=6, padx=2, pady=5)
imageTypeControl.grid(row=6, column=6, padx=2, pady=5)
imageTypeLabel.grid(row=6, column=5, padx=2, pady=5)

#Controles colores RGB y CMYK
#?Labels
rgbLabel = tkinter.Label(appVisor, text='Canales RGB:', font=("Verdana", 10), bg='#006', fg='#FFF')
cmykLabel = tkinter.Label(appVisor, text='Canales CMYK:', font=("Verdana", 10), bg='#006', fg='#FFF')
#?Check buttons para RGB
checkRed = tkinter.Checkbutton(appVisor, text=' Rojo  ', width=10, font=("Verdana", 10), bg='#006', fg='#FFF', command=lambda:colorRed())
checkGreen = tkinter.Checkbutton(appVisor, text=' Verde', width=10, font=("Verdana", 10), bg='#006', fg='#FFF', command=lambda:colorGreen())
checkBlue = tkinter.Checkbutton(appVisor, text=' Azul  ', width=10, font=("Verdana", 10), bg='#006', fg='#FFF', command=lambda:colorBlue())
#?Check buttons para CMYK
checkCyan = tkinter.Checkbutton(appVisor, text=' Cian     ', width=10, font=("Verdana", 10), bg='#006', fg='#FFF', command=lambda:colorCyan())
checkMagenta = tkinter.Checkbutton(appVisor, text=' Magenta', width=10, font=("Verdana", 10), bg='#006', fg='#FFF', command=lambda:colorMagenta())
checkYellow = tkinter.Checkbutton(appVisor, text=' Amarillo ', width=10, font=("Verdana", 10), bg='#006', fg='#FFF', command=lambda:colorYellow())
#?Posicion para los checkbutton y los label del control RGB:
rgbLabel.grid(row=9, column=5, padx=2, pady=5)
checkRed.grid(row=8, column=6, padx=2, pady=5)
checkGreen.grid(row=9, column=6, padx=2, pady=5)
checkBlue.grid(row=10, column=6, padx=2, pady=5)
#!------------------------------------------------------------------------------------------------------------------------------------------
cmykLabel.grid(row=12, column=5, padx=2, pady=5)
checkCyan.grid(row=11, column=6, padx=2, pady=5)
checkMagenta.grid(row=12, column=6, padx=2, pady=5)
checkYellow.grid(row=13, column=6, padx=2, pady=5)

appVisor.mainloop()