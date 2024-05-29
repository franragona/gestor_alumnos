import tkinter as tk

def agregar():
    nombre = caja_nombre.get()
    curso = caja_curso.get()
    diccionario[nombre] = curso
    print("Se agrego alumno correctamente.")
    
def ver_lista():
    if diccionario:
        print("Lista de alumnos:")
        for nombre,curso in diccionario.items():
            print(f"{nombre} - {curso}")
    else:
        print("No hay alumnos registrados.")
        
def ver_cursos():
    nombre = caja_nombre.get()
    if nombre in diccionario:
        print(f"{nombre} esta suscripto a {diccionario[nombre]} cursos.")
    else:
        print(f"{nombre} no se encuentra registrado.")
        
diccionario = {}
    
ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title("gusano.exe")

boton_ver_alumnos = tk.Button(text="Ver lista de alumnos", command=ver_lista)
boton_ver_alumnos.place(x=20, y=19, width=120, height=30)

caja_nombre = tk.Entry()
caja_nombre.place(x=120, y=75, width=200, height=25)

etiqueta_nombre = tk.Label(text="Nombre alumno:")
etiqueta_nombre.place(x=20,y=75)

caja_curso = tk.Entry()
caja_curso.place(x=120,y=115, width=200, height=25)

etiqueta_curso = tk.Label(text="Cursos:")
etiqueta_curso.place(x=20,y=115)

boton_agregar = tk.Button(text="Agregar a la lista", command=agregar)
boton_agregar.place(x=20, y=170)

boton_ver_curso = tk.Button(text="Ver cantidad de cursos", command=ver_cursos)
boton_ver_curso.place(x=125, y=170)



ventana.mainloop()