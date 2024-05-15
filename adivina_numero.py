import numpy as np
import tkinter as tk

# Generar el número aleatorio
num_aleatorio = np.random.randint(1, 101)  # Generamos un número aleatorio entre 1 y 100
print("Número aleatorio:", num_aleatorio)  # Mensaje de depuración

# Variable para contar el número de intentos
intento=0

def adivinanza(event=None):
    global intento
    
    jugar = entrada.get()

    if jugar.lower() == 'exit':
        print("Saliendo del juego...")  # Mensaje de depuración
        root.quit()  # Cerrar la aplicación
        return

    try:
        numero = int(jugar)  # Convertir la entrada a entero
        print("Número convertido a entero:", numero)  # Mensaje de depuración
        
        if numero < 1 or numero > 100:
            resultado.config(text='El número debe estar entre 1 y 100.')
            print("Número fuera del rango 1-100.")  # Mensaje de depuración
        elif numero < num_aleatorio:
            intentos_restantes = 9 - intento 
            resultado.config(text=f'Inserte un número mayor. Te quedan {intentos_restantes} intentos.')
            print("Número menor que el aleatorio.")  # Mensaje de depuración
        elif numero > num_aleatorio:
            intentos_restantes = 9 - intento 
            resultado.config(text=f'Inserte un número menor. Te quedan {intentos_restantes} intentos.')
            print("Número mayor que el aleatorio.")  # Mensaje de depuración
        else:
            resultado.config(text='¡Enhorabuena, has acertado!')
            print("Número correcto!")  # Mensaje de depuración
            entrada.delete(0, tk.END)  # Limpiar la entrada
            root.quit()  # Salir de la aplicación
            return
        
    except ValueError:  # Manejar el caso en que se ingrese un valor no numérico
        resultado.config(text='Por favor, ingrese un número válido o "exit" para salir.')
        print("Valor no numérico ingresado.")  # Mensaje de depuración
    
    if numero >= 1 and numero <= 100:  # Contar el intento solo si el número está dentro del rango
            intento += 1
            if intento == 10:
                resultado.config(text='Ha superado el número de intentos. Acceso denegado\n' +
                                    f'Para que no te quedes con la intriga... el número correcto era {num_aleatorio}')
    

# ----------------Interfaz gráfica usando tkinter------------------#

root = tk.Tk() # Crea una instancia de la clase Tk para crear la ventana principal de la interfaz gráfica.
root.title("Adivina el número")

# Agrega widgets a la ventana principal

# widget 1
label = tk.Label(root, text="¿Conseguirás acertar el número correcto? Inserte un número entre el 1 al 100. Dispones de 10 intentos (o escribe exit para salir):")
label.pack() # El método pack() organiza el widget en la ventana principal

# widget 2
entrada = tk.Entry(root)
entrada.pack()
entrada.focus() # Para asegurar que el widget de entrada recibe el foco y esté listo para recibir la entrada del usuario

# widget 3
boton = tk.Button(root, text="Jugar", command=adivinanza)
boton.pack()

# widget 4
resultado = tk.Label(root, text="")
resultado.pack()

# Configurar el evento de tecla <Return> para llamar a la función adivinanza
root.bind('<Return>', adivinanza)

root.mainloop() # Inicia el bucle principal de la ventana. Este bucle hace que la ventana permanezca abierta y receptiva a las interacciones del usuario hasta que se cierre la ventana.