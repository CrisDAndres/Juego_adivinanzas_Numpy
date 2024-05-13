import numpy as np
import tkinter as tk


def adivinanza():
    intento = 0
    num_aleatorio = np.random.randint(1, 101)  # Generamos un número aleatorio entre 1 y 100
    
    while intento < 9 or intento == 9: 
        jugar = entrada.get()  # Obtiene el número ingresado por el usuario desde el widget Entry
        
        if jugar.lower() == 'exit':
            root.quit()  # Cerrar la aplicación
            return
        
        else:
            try:
                numero = int(jugar)  # Convertir la entrada a entero
                
                if numero < num_aleatorio:
                    intentos_restantes = 9 - intento
                    resultado.config(text=f'Inserte un número mayor. Te quedan {intentos_restantes} intentos.')
                    
                elif numero > num_aleatorio:
                    intentos_restantes = 9 - intento
                    resultado.config(text=f'Inserte un número menor. Te quedan {intentos_restantes} intentos.')
                
                elif numero < 1 or numero > 100:
                    resultado.config(text='Lo siento, el número debe estar entre 1 y 100.')
                    continue  # No contar este intento, seguir al siguiente
                    
                elif intento == 9:
                    resultado.config(text='Ha superado el número de intentos. Acceso denegado\n' +
                                          f'Para que no te quedes con la intriga... el número correcto era {num_aleatorio}')
                    
                else:
                    resultado.config(text='¡Enhorabuena, has acertado!')
                    return
                

            except ValueError:  # Manejar el caso en que se ingrese un valor no numérico
                resultado.config(text='Por favor, ingrese un número válido o "exit" para salir.')
                continue
            
            intento += 1  # Incrementar el contador de intentos
             
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

# widget 3
boton = tk.Button(root, text="Jugar", command=adivinanza)
boton.pack()

# widget 4
resultado = tk.Label(root, text="")
resultado.pack()

root.mainloop() # Inicia el bucle principal de la ventana. Este bucle hace que la ventana permanezca abierta y receptiva a las interacciones del usuario hasta que se cierre la ventana.