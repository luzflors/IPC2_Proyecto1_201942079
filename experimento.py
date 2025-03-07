import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from proteina import Lista_proteina
from proteina import ExperimentoXML
import os


class Experimento():
    def __init__(self):
        self._lista = Lista_proteina
        self._experimento_xml = ExperimentoXML
        self._opcion = None
        self._carpeta = "Catalogo_experimento"
        self._crear_carpeta()

    def menu_principal(self):
        print("\n====================================================")
        print("|          *            Menu          *            |")
        print("====================================================")
        print("| 1. Inicializar sistema                           |")
        print("| 2. Crear catalogo de experimentos                |")
        print("| 3. Desarrollar un experimeto                     |")
        print("| 4. Mostrar datos del estudiante                  |")
        print("| 5. Salir                                         |")
        print("====================================================\n")

        try:
            self._opcion = int(input(f"Seleccione opcion: ").strip())
        except ValueError:
            print("Error: Debe ingresar un número.")
            return
        
        if self._opcion == 1:
            self._iniciar_sistema()
        elif self._opcion == 2:
            self._crear_carpeta()
        elif self._opcion == 3:
            self._desarrollar_experimento()
        elif self._opcion == 4:
            self._datos_estudiante()
        elif self._opcion == 5:
            print("\nSaliendo del programa... ¡Hasta luego!")
            return
    
    def _iniciar_sistema(self):
        if os.path.exists(self._carpeta):
            shutil.rmtree(self._carpeta)
            print("\nSe ha eliminado la información del catálogo de experimentos.")
        
        self._crear_carpeta()
    
    def _crear_catalogo(self):
        print("\n====================================================")
        print("|          *      Crear catalogo      *            |")
        print("====================================================")
        print("| 1. Cargar archivo de experimentos                |")
        print("| 2. Ver estructura del archivo XML de entrada     |")
        print("| 3. Regresar                                      |")
        print("====================================================\n")

        try:
            self._opcion = int(input(f"Seleccione opcion: ").strip())  
        except ValueError:
            print("Error: Debe ingresar un número.")
            return
        
        if self._opcion == 1:
            self._cargar_archivo()
        elif self._opcion == 2:
            pass
        elif self._opcion == 3:
            print("\nRegresando...")

    def _crear_carpeta(self):
        if not os.path.exists(self._carpeta):
            os.makedirs(self._carpeta)
            print(f"Carpeta '{self._carpeta}' creada.")
        else:
            return

    def _cargar_archivo(self, archivo):
        self._crear_carpeta()
        Tk().withdraw()
        archivo = askopenfilename(title="Seleccionar un archivo", filetypes=[("XML Files", "*.xml"), ("All Files", "*.*")])
        if archivo: 
            shutil.move(archivo, self._carpeta)
            print(f"Archivo '{archivo}' movido a '{self._carpeta}'.")
        else:
            print("No se seleccionó ningún archivo.")

    def _desarrollar_experimento(self):
        print("\n====================================================")
        print("|        *   Desarrollar un experimeto     *       |")
        print("====================================================")
        print("| 1. Desarrollar experimento manual                |")
        print("| 2. Cargar un experimento del catálogo            |")
        print("| 3. Regresar                                      |")
        print("====================================================\n")

        try:
            self._opcion = int(input(f"Seleccione opcion: ").strip())
        except ValueError:
            print("Error: Debe ingresar un número.")
            return
        
        if self._opcion == 1:
            pass
        elif self._opcion == 2:
            pass
        elif self._opcion == 3:
            print("\nRegresando...")
    
    def _forma_de_ejecutar(self):
        print("\n====================================================")
        print("|         *       Forma de Ejecución      *        |")
        print("====================================================")
        print("| 1. Paso a paso                                   |")
        print("| 2. Directamente                                  |")
        print("| 3. Regresar                                      |")
        print("====================================================\n")

        try:
            self._opcion = int(input(f"Seleccione opcion: ").strip())
        except ValueError:
            print("Error: Debe ingresar un número.")
            return
        
        if self._opcion == 1:
            pass
        elif self._opcion == 2:
            pass
        elif self._opcion == 3:
            print("\nRegresando...")


    def _ejecutar_experimento(self):
        pass

    def _paso_a_paso(self):
        pass

    def _datos_estudiante(self):
        print("\n==============================================================")
        print("|             *      Datos del Estudiante     *              |")
        print("==============================================================")
        print("| Carné: 201942079                                           |")
        print("| Nombre: Luz de Maria Jose Castillo Flores                  |")
        print("| Curso: Introducción a la Programación y Computación 2      |")
        print("| Carrera: Ingeniería en Sistemas                            |")
        print("| Semestre: 4to                                              |")
        print("| Documentación: https://github.com/proyecto-experimentos    |")
        print("==============================================================\n")

        while True:    
            self._opcion = input(f"\nPresione Enter para regresar al menú... ").strip()
            if self._opcion == "":
                print("\nRegresando...")
                break
            else:
                print("\nPor favor, solo presione Enter.")
