import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from proteina import ListaExperimento, ListaProteina, ExperimentoXML
import os


class Experimento():
    def __init__(self):
        self._lista_proteinas = ListaProteina
        self._lista_experimento = ListaExperimento
        self._experimento_xml = ExperimentoXML
        self._crear_carpeta()

    def menu_principal(self):
        print("\n====================================================")
        print("|          *            Menu          *            |")
        print("====================================================")
        print("| 1. Inicializar sistema                           |") #Ya
        print("| 2. Crear catalogo de experimentos                |") #Ya
        print("| 3. Desarrollar un experimeto                     |") 
        print("| 4. Mostrar datos del estudiante                  |") #Ya
        print("| 5. Salir                                         |")
        print("====================================================\n")
        opcion = 0
        try:
            opcion = int(input(f"Seleccione opcion: ").strip())
        except ValueError:
            print("Error: Debe ingresar un número.")
            return
        
        if opcion == 1:
            self._iniciar_sistema()
        elif opcion == 2:
            self._crear_catalogo()
        elif opcion == 3:
            self._desarrollar_experimento()
        elif opcion == 4:
            self._datos_estudiante()
        elif opcion == 5:
            print("\nSaliendo del programa... ¡Hasta luego!")
            return
    
    def _iniciar_sistema(self):
        if os.path.exists(self._carpeta):
            shutil.rmtree(self._carpeta)
            print("\nSe ha eliminado la información del catálogo de experimentos.")
        if self._lista_proteinas is None:
            self._lista_proteinas.limpiar()
        if self._lista_experimento is None:
            self._lista_experimento.limpiar()

        self._crear_carpeta()
    
    def _crear_catalogo(self):
        print("\n====================================================")
        print("|          *      Crear catalogo      *            |")
        print("====================================================")
        print("| 1. Cargar archivo de experimentos                |") 
        print("| 2. Ver estructura del archivo XML de entrada     |") 
        print("| 3. Regresar                                      |") 
        print("====================================================\n")
        opcion = 0
        try:
            opcion = int(input(f"Seleccione opcion: ").strip())  
        except ValueError:
            print("Error: Debe ingresar un número.")
            return
        
        if opcion == 1:
            self._cargar_archivo()
        elif opcion == 2:
            self._mostrar_estructura()
        elif opcion == 3:
            print("\nRegresando...")

    def _crear_carpeta(self, nombre_carpeta):
        carpeta = "Catalogo_experimento"
        try:
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)
                print(f"Catalogo listo.")
        except Exception as e:
            print(f"Error al crear la carpeta: {e}")


    def _cargar_archivo(self):
        self._crear_carpeta()
        Tk().withdraw() 
        archivo_seleccionado = askopenfilename(
            title = "Seleccionar un archivo",
            filetypes=[("XML Files", "*.xml"), ("All Files", "*.*")]
        )

        if not archivo_seleccionado:
            print("No se seleccionó ningún archivo.")
            return
        
        try:
            destino = os.path.join("Catalogo_experimento", os.path.basename(archivo_seleccionado))
            shutil.move(archivo_seleccionado, destino)
            print(f"Archivo '{os.path.basename(archivo_seleccionado)}' movido a '{self._carpeta}'.")
        except Exception as e:
            print(f"Error al mover el archivo: {e}")

    def _mostrar_estructura(self):
        print("\n--- Estructura del archivo XML de entrada ---")
        print("""<?xml version="1.0" encoding="UTF-8"?>
            <experimentos>
                <experimento nombre="paciente01">
                    <tejido filas="5" columnas="5">
                        <rejilla>
                            LAV LAV VAL VAL VAL
                            VAR RAV GHI VAL VAL
                            LAV AVL ALV LAV LAV
                            VAL ILL KEQ DCC LAV
                            VAR ILL KQA CDC LAV
                        </rejilla>
                    </tejido>
                    <proteinas>
                        <pareja> LAV VAL </pareja>
                    </proteinas>
                </experimento>
                <---- otros experimentos ---->
            </experimentos>""")

    def _desarrollar_experimento(self):
        print("\n====================================================")
        print("|        *   Desarrollar un experimeto     *       |")
        print("====================================================")
        print("| 1. Desarrollar experimento manual                |")
        print("| 2. Cargar un experimento del catálogo            |")
        print("| 3. Regresar                                      |")
        print("====================================================\n")
        opcion = 0
        try:
            opcion = int(input(f"Seleccione opcion: ").strip())
        except ValueError:
            print("Error: Debe ingresar un número.")
            return
        
        if opcion == 1:
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            print("\nRegresando...")
    
    def desarrollo_manual(self):
        pass

    def _desarrollo_catalogo(self):
        pass

    def _forma_de_ejecutar(self):
        print("\n====================================================")
        print("|         *       Forma de Ejecución      *        |")
        print("====================================================")
        print("| 1. Paso a paso                                   |")
        print("| 2. Directamente                                  |")
        print("| 3. Regresar                                      |")
        print("====================================================\n")
        opcion = 0
        try:
            opcion = int(input(f"Seleccione opcion: ").strip())
        except ValueError:
            print("Error: Debe ingresar un número.")
            return
        
        if opcion == 1:
            self._paso_a_paso()
        elif opcion == 2:
            self._directamente()
        elif opcion == 3:
            print("\nRegresando...")

    def _ejecutar_experimento(self):
        pass

    def _directamente(self):
        pass

    def _paso_a_paso(self):
        pass

    def _resultado(self, porcentaje):
        if porcentaje > 0.3 and porcentaje < 0.6:
            print("Medicamento exitoso")
        elif porcentaje > 0.0 and porcentaje < 0.29:
            print("Medicamento no eficiente")
        elif porcentaje > 0.61 and porcentaje < 1.0:
            print("Medicamento fatal")    

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
        opcion = ""
        while True:    
            opcion = input(f"\nPresione Enter para regresar al menú... ").strip()
            if opcion == "":
                print("\nRegresando...")
                break
            else:
                print("\nPor favor, solo presione Enter.")
