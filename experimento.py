from proteina import ListaProteina, NodoProteina, ListaExperimento, ExperimentoXML
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

class Experimento():
    def __init__(self):
        self._lista_experimento = ListaExperimento()
        self._experimento_xml = None
        self._nombre_ejecutar = None

    def menu_principal(self):  # Listo
        print("\n====================================================")
        print("|          *            Menu          *            |")
        print("====================================================")
        print("| 1. Inicializar sistema                           |")
        print("| 2. Crear catalogo de experimentos                |")
        print("| 3. Desarrollar un experimento                    |")
        print("| 4. Mostrar datos del estudiante                  |")
        print("| 5. Salir                                         |")
        print("====================================================\n")
        try:
            opcion = int(input("Seleccione opcion: ").strip())
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
            exit()

    def _iniciar_sistema(self):
        self._lista_experimento.limpiar()
        carpeta = 'graficas'
        if os.path.exists(carpeta):
            for archivo in os.listdir(carpeta):
                ruta = os.path.join(carpeta, archivo)
                try:
                    if os.path.isfile(ruta):
                        os.remove(ruta)
                except Exception as e:
                    print(f"Error al eliminar {ruta}: {e}")
        else:
            print(f"La carpeta {carpeta} no existe.")
    
    def _crear_catalogo(self):  # Listo
        print("\n====================================================")
        print("|          *      Crear catalogo      *            |")
        print("====================================================")
        print("| 1. Cargar archivo de experimentos                |") 
        print("| 2. Ver estructura del archivo XML de entrada     |") 
        print("| 3. Regresar                                      |") 
        print("====================================================\n")
        try:
            opcion = int(input("Seleccione opcion: ").strip())
        except ValueError:
            print("Error: Debe ingresar un número.")
            return
        
        if opcion == 1:
            self._cargar_experimento()
        elif opcion == 2:
            self._mostrar_estructura()
        elif opcion == 3:
            print("\nRegresando...")

    def _cargar_experimento(self):  # Listo
        Tk().withdraw() 
        archivo_seleccionado = askopenfilename(
            title="Seleccionar un archivo",
            filetypes=[("XML Files", "*.xml"), ("All Files", "*.*")]
        )

        if not archivo_seleccionado:
            print("No se seleccionó ningún archivo.")
            return
        
        try: 
            self._experimento_xml = ExperimentoXML(archivo_seleccionado)
            self._experimento_xml.extraer_xml()

            self._lista_experimento = self._experimento_xml.get_experimentos()
            print("Experimentos cargados exitosamente.")

        except Exception as e:
            print("Error al leer el archivo XML:", e)
    
    def _mostrar_estructura(self):  # Listo
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
            <!-- otros experimentos -->
        </experimentos>""")

    def _desarrollar_experimento(self):  
        print("\n====================================================")
        print("|        *   Desarrollar un experimento    *       |")
        print("====================================================")
        print("| 1. Desarrollar experimento manual                |")
        print("| 2. Cargar un experimento del catálogo            |")
        print("| 3. Regresar                                      |")
        print("====================================================\n")
        try:
            opcion = int(input("Seleccione opcion: ").strip())
        except ValueError:
            print("Error: Debe ingresar un número.")
            return
        
        if opcion == 1:
            self._desarrollo_manual()
            return
        elif opcion == 2:
            self._desarrollo_catalogo()
            return
        elif opcion == 3:
            self._iniciar_sistema()
            print("\nRegresando...")

    def _desarrollo_manual(self):  # Listo
        nombre = input("Ingrese nombre del experimento: ").strip()
        try:
            filas = int(input("Ingrese número de filas: ").strip())
            columnas = int(input("Ingrese número de columnas: ").strip())
        except ValueError:
            print("Error: filas y columnas deben ser números.")
            return

        print("Ingrese la rejilla fila por fila, separando las proteínas con espacios:")

        rejilla = ""
        for i in range(filas):
            fila = input(f"Fila {i + 1}: ").strip()
            rejilla += fila + "\n"

        try:
            n_parejas = int(input("Ingrese el número de parejas: ").strip())
        except ValueError:
            print("Error: debe ingresar un número.")
            return

        parejas = ""  
        primera_pareja = True 

        if n_parejas > 0:
            print("Ingrese las parejas de proteínas (ejemplo: PROT1 PROT2):")

        for i in range(n_parejas):  
            pareja_texto = input(f"Pareja {i + 1}: ").strip()
            if pareja_texto:
                if not primera_pareja:
                    parejas += ", " 
                parejas += pareja_texto
                primera_pareja = False

        self._lista_experimento.insertar(nombre, filas, columnas, rejilla, parejas)
        print("\nExperimento guardado\n")

        self._nombre_ejecutar = nombre

        self._forma_de_ejecutar()
        

    def _modificar_experimento(self):  # Listo
        nombre = self._nombre_ejecutar
        if not nombre:
            return  
        experimento_modificar = self._lista_experimento.buscar(nombre)
        
        print(f"\n--- Modificando el experimento: {experimento_modificar.get_nombre()} ---")
        
        print(f"Nombre actual: {experimento_modificar.get_nombre()}")
        nuevo_nombre = input("Ingrese nuevo nombre (o deje vacío para mantener): ").strip()
        if nuevo_nombre != "":
            experimento_modificar._nombre = nuevo_nombre

        try:
            print(f"Numero de filas actuales: {experimento_modificar.get_filas()}")
            nueva_filas = input("Ingrese nuevo valor para filas (o deje vacío para mantener): ").strip()
            if nueva_filas != "":
                experimento_modificar._filas = int(nueva_filas)
        except ValueError:
            print("Valor no numérico; se mantendrá el valor actual.")

        try:
            print(f"Numero de columnas actuales: {experimento_modificar.get_columnas()}")
            nueva_columnas = input("Ingrese nuevo valor para columnas (o deje vacío para mantener): ").strip()
            if nueva_columnas != "":
                experimento_modificar._columnas = int(nueva_columnas)
        except ValueError:
            print("Valor no numérico; se mantendrá el valor actual.")

        print("\nRejilla actual:")
        print(experimento_modificar.get_rejilla())
        if input("¿Desea modificar la rejilla? (s/n): ").strip().lower() == "s":
            rejilla_nueva = ""
            filas_mod = experimento_modificar.get_filas()
            print("Ingrese la rejilla fila por fila, separando las proteínas con espacios:")
            for i in range(filas_mod):
                fila = input(f"Fila {i + 1}: ").strip()
                rejilla_nueva += fila + "\n"
            if rejilla_nueva != "":
                experimento_modificar._rejilla = rejilla_nueva

        print(f"\nPareja(s) actual(es): {experimento_modificar.get_pareja()}")
        if input("¿Desea modificar las parejas de proteínas? (s/n): ").strip().lower() == "s":
            try:
                n_parejas = int(input("Ingrese el nuevo número de parejas: ").strip())
            except ValueError:
                print("Número no válido; se mantendrán las parejas actuales.")
                n_parejas = 0
            parejas_nuevas = ""
            primera = True
            if n_parejas > 0:
                print("Ingrese las parejas de proteínas (ejemplo: PROT1 PROT2):")
            for i in range(n_parejas):
                pareja_texto = input(f"Pareja {i + 1}: ").strip()
                if pareja_texto:
                    if not primera:
                        parejas_nuevas += ", "
                    parejas_nuevas += pareja_texto
                    primera = False
            if parejas_nuevas != "":
                experimento_modificar._pareja = parejas_nuevas

        print("\nExperimento modificado correctamente.\n")
        self._forma_de_ejecutar()

    def _desarrollo_catalogo(self):  # Listo
        if self._lista_experimento.primero is None:
            print("No hay experimentos en el catálogo. Cargue un archivo XML primero.")
            return None  

        print("Experimentos disponibles:")
        tmp = self._lista_experimento.primero

        while tmp:
            print(f"- {tmp.get_nombre()}")
            tmp = tmp.siguiente

        nombre = input("Ingrese el nombre del experimento a ejecutar: ").strip()
        exp = self._lista_experimento.buscar(nombre)
        self._nombre_ejecutar = nombre

        if not exp:
            print("Experimento no encontrado.")
            return None 

        if input("¿Desea modificar el experimento? (s/n): ").strip().lower() == "s":
            self._modificar_experimento()
        else:
            self._forma_de_ejecutar()
        
    def _ingresar_proteinas(self, nombre):
        lista_proteinas = ListaProteina()
        exp = self._lista_experimento.buscar(nombre)
        rejilla = exp.get_rejilla().strip()
        filas = exp.get_filas()
        columnas = exp.get_columnas()
        lista_proteinas.cargar_rejilla_en_lista(rejilla, filas, columnas)
        return lista_proteinas

    def _ejecutar(self):
        nombre = self._nombre_ejecutar
        exp = self._lista_experimento.buscar(nombre)
        if not exp:
            print("Experimento no encontrado.")
            return

        lista_proteinas = self._ingresar_proteinas(nombre)
        filas = exp.get_filas()
        columnas = exp.get_columnas()

        self._experimento_xml._generar_rejilla(f"{nombre}", lista_proteinas.primero, filas, columnas, "Inicial")
        
        parejas = exp.get_pareja()
        
        while True:
            encontro_alguna = False
            for pareja in  parejas.split(","):
                proteina01, proteina02 = pareja.split()
                if lista_proteinas.buscar_parejas(proteina01, proteina02):
                    encontro_alguna = True
            if not encontro_alguna:
                break

        self._experimento_xml._generar_rejilla(f"{nombre}", lista_proteinas.primero, filas, columnas, "Final")

        porcentaje = lista_proteinas.contar_porcentaje_inertes()
        self._resultado(porcentaje)
        
    def _ejecutar_pasos(self):
        nombre = self._nombre_ejecutar
        exp = self._lista_experimento.buscar(nombre)
        if not exp:
            print("Experimento no encontrado.")
            return

        lista_proteinas = self._ingresar_proteinas(nombre)
        filas = exp.get_filas()
        columnas = exp.get_columnas()

        self._experimento_xml._generar_rejilla(f"{nombre}", lista_proteinas.primero, filas, columnas, 1) 

        parejas = exp.get_pareja()
        index = 1
        encontre = False
        
        parejas = exp.get_pareja()
        index = 1
        
        while True:
            encontro_alguna = False
            for pareja in  parejas.split(","):
                proteina01, proteina02 = pareja.split()
                if lista_proteinas.buscar_parejas(proteina01, proteina02):
                    encontro_alguna = True
                    index += 1
                    self._experimento_xml._generar_rejilla(f"{nombre}", lista_proteinas.primero, filas, columnas, index)
            if not encontro_alguna:
                break

        porcentaje = lista_proteinas.contar_porcentaje_inertes()
        self._resultado(porcentaje)

    def _cargar_rejilla_en_lista(self, exp):
        rejilla_txt = exp.get_rejilla().strip()
        primera_fila = None
        fila_anterior = None
        for linea in rejilla_txt.splitlines():
            linea = linea.strip()
            if linea == "":
                continue
            palabras = linea.split()
            cabeza_fila = None
            nodo_anterior = None
            for palabra in palabras:
                nuevo = NodoProteina(palabra, False)
                if cabeza_fila is None:
                    cabeza_fila = nuevo
                else:
                    nodo_anterior.siguiente = nuevo
                nodo_anterior = nuevo

            if fila_anterior is not None:
                nodo_actual = cabeza_fila
                nodo_superior = fila_anterior
                while nodo_actual is not None and nodo_superior is not None:
                    nodo_superior.abajo = nodo_actual
                    nodo_superior = nodo_superior.siguiente
                    nodo_actual = nodo_actual.siguiente
            else:
                primera_fila = cabeza_fila
            fila_anterior = cabeza_fila
        lista_proteinas = ListaProteina()
        lista_proteinas.primero = primera_fila
        return lista_proteinas

    def _forma_de_ejecutar(self):
        while True:
            if not os.path.exists('graficas'):
                os.makedirs('graficas')
            print("\n====================================================")
            print("|         *       Forma de Ejecución      *        |")
            print("====================================================")
            print("| 1. Paso a paso                                   |")
            print("| 2. Directamente                                  |")
            print("| 3. Regresar                                      |")
            print("====================================================\n")
            
            try:
                opcion = int(input("Seleccione opcion: ").strip())
                if opcion == 1:
                    self._ejecutar_pasos()
                    break  
                elif opcion == 2:
                    self._ejecutar()
                    break  
                elif opcion == 3:
                    print("\nRegresando...")
                    break 
                else:
                    print("Opción no válida. Intente de nuevo.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")

    
    def _resultado(self, porcentaje):
        print("\nResultados del experimento:")
        if porcentaje >= 31 and porcentaje <= 60:
            print("Medicamento exitoso")
        elif porcentaje >= 0 and porcentaje <= 30:
            print("Medicamento no eficiente")
        elif porcentaje >= 61 and porcentaje <= 100:
            print("Medicamento fatal")
        else:
            print("Resultado fuera de rango definido")
    
    def _datos_estudiante(self):
        print("\n==============================================================")
        print("|             *      Datos del Estudiante     *              |")
        print("==============================================================")
        print("| Carné: 201942079                                           |")
        print("| Nombre: Luz de Maria Jose Castillo Flores                  |")
        print("| Curso: Introducción a la Programación y Computación 2      |")
        print("| Carrera: Ingeniería en Sistemas                            |")
        print("| Semestre: 4to                                              |")
        print("==============================================================\n")

        print("Documentación: https://github.com/luzflors/IPC2_Proyecto1_201942079.git")
        while True:    
            opcion = input("Presione Enter para regresar al menú... ").strip()
            if opcion == "":
                print("\nRegresando...")
                break
            else:
                print("\nPor favor, solo presione Enter.")

if __name__ == "__main__":
    exp = Experimento()
    while True:
        exp.menu_principal()