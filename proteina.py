import xml.etree.ElementTree as ET
import subprocess

class NodoProteina():
    def __init__(self, proteina, es_inerte):
        self._proteina = proteina
        self._es_inerte = es_inerte 
        self.siguiente = None
        self.abajo = None

    def get_proteina(self):
        return self._proteina

    def get_es_inerte(self):
        return self._es_inerte
    
    def get_set_es_inerte(self, es_inerte):
        self._es_inerte = es_inerte
    
    def mostrar(self):
        print(self._proteina)
        
class ListaProteina():
    def __init__(self):
        self.primero = None

    def contar_porcentaje_inertes(self):
        total_nodos = 0
        inertes = 0
        fila_actual = self.primero
        
        while fila_actual is not None:
            nodo_actual = fila_actual
            while nodo_actual is not None:
                total_nodos += 1
                if nodo_actual.get_es_inerte():
                    inertes += 1
                nodo_actual = nodo_actual.siguiente
            fila_actual = fila_actual.abajo
        
        if total_nodos == 0:
            return 0  
        return (inertes / total_nodos) * 100 

    def cargar_rejilla_en_lista(self, rejilla_txt, filas, columnas):
        pro = rejilla_txt.split()
        index = 0
        primera_fila = None
        fila_anterior = None
        for i in range(filas):
            cabeza_fila = None
            nodo_anterior = None
            for j in range(columnas):
                if index < len(pro):
                    nuevo = NodoProteina(pro[index], False)
                    index += 1
                else:
                    break
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
        self.primero = primera_fila

    def buscar_parejas(self, proteina01, proteina02):
        fila_actual = self.primero

        while fila_actual is not None:
            nodo_actual = fila_actual

            while nodo_actual is not None:
                while nodo_actual is not None and nodo_actual.get_es_inerte():
                    nodo_actual = nodo_actual.siguiente
                
                if nodo_actual is None:
                    break  

                nodo_siguiente = nodo_actual.siguiente
                while nodo_siguiente is not None and nodo_siguiente.get_es_inerte():
                    nodo_siguiente = nodo_siguiente.siguiente

                if nodo_siguiente is not None:
                    if (nodo_actual.get_proteina() == proteina01 and nodo_siguiente.get_proteina() == proteina02) or \
                    (nodo_actual.get_proteina() == proteina02 and nodo_siguiente.get_proteina() == proteina01):
                        nodo_actual._es_inerte = True
                        nodo_siguiente._es_inerte = True
                        print("Encontró pareja")
                        return True

                nodo_abajo = nodo_actual.abajo
                while nodo_abajo is not None and nodo_abajo.get_es_inerte():
                    nodo_abajo = nodo_abajo.abajo

                if nodo_abajo is not None:
                    if (nodo_actual.get_proteina() == proteina01 and nodo_abajo.get_proteina() == proteina02) or \
                    (nodo_actual.get_proteina() == proteina02 and nodo_abajo.get_proteina() == proteina01):
                        nodo_actual._es_inerte = True
                        nodo_abajo._es_inerte = True
                        print("Encontró pareja")
                        return True

                nodo_actual = nodo_actual.siguiente  

            fila_actual = fila_actual.abajo 

        return False


    def buscar(self, nombre):
        tmp = self.primero 
        while tmp:
            if tmp._proteina == nombre:
                return tmp
            tmp = tmp.siguiente
        return None
    
    def limpiar(self):
        while self.primero is not None:
            tmp = self.primero  
            self.primero = self.primero.siguiente  
            tmp.siguiente = None

class NodoExperimento():
    def __init__(self, nombre, filas, columnas, rejilla, pareja, iteracion):
        self._nombre = nombre 
        self._filas = int(filas)
        self._columnas = int(columnas)
        self._rejilla = rejilla 
        self._pareja = pareja
        self.__iteracion = int(iteracion)    
        self.siguiente = None 

    def get_nombre(self):
        return self._nombre if self._nombre is not None else 'Experimento'
    
    def get_rejilla(self):
        return self._rejilla if self._rejilla is not None else ""

    def get_pareja(self):
        return self._pareja if self._pareja is not None else ""

    def get_columnas(self):
        return int(self._columnas) if self._columnas is not None else 0
    
    def get_filas(self):
        return int(self._filas) if self._filas is not None else 0
    
    def get_iteracion(self):
        return int(self.__iteracion) if self.__iteracion is not None else 0

    def mostrar(self):
        print(f"  Nombre: {self.get_nombre()}")
        print(f"  Filas: {self.get_filas()}")
        print(f"  Columnas: {self.get_columnas()}")
        print("  Rejilla:")
        print(self.get_rejilla())
        print(f"  Pareja(s): {self.get_pareja()}")
        print(f" Iteracion: {self.get_iteracion}")
        
    
class ListaExperimento:
    def __init__(self):
        self.primero = None  

    def insertar(self, nombre, filas, columnas, rejilla, pareja):
        nuevo = NodoExperimento(nombre, filas, columnas, rejilla, pareja, 0)
        if self.primero is None:
            self.primero = nuevo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
    
    def insertar(self, nombre, filas, columnas, rejilla, pareja, iteracion):
        nuevo = NodoExperimento(nombre, filas, columnas, rejilla, pareja, iteracion)
        if self.primero is None:
            self.primero = nuevo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def mostrar_experimentos(self):
        tmp = self.primero
        while tmp:
            tmp.mostrar()
            tmp = tmp.siguiente

    def buscar(self, nombre):
        tmp = self.primero 
        while tmp:
            if tmp.get_nombre() == nombre:
                return tmp
            tmp = tmp.siguiente
        return None 

    def modificar(self, nombre):
        self.buscar(nombre)

    def limpiar(self):
        while self.primero is not None:
            tmp = self.primero  
            self.primero = self.primero.siguiente  
            tmp.siguiente = None 

class ExperimentoXML():
    def __init__(self, archivo):
        self._archivo = archivo
        self._experimentos = ListaExperimento()

    def get_experimentos(self):
        return self._experimentos

    def _cargar_xml(self):
        try:
            xml_file = ET.parse(self._archivo)
            return xml_file.getroot()
        except Exception as err:
            print("Error:", err)
        return None
    
    def extraer_xml(self):
        xml_raiz = self._cargar_xml()
        if xml_raiz is None:
            print('No existen datos')
            return
        
        for experimento in xml_raiz.findall('experimento'):
            nombre = experimento.get('nombre')
            rejilla = ""
            filas = 0
            columnas = 0
            iteracion = int(experimento.find('limite').text)

            tejido = experimento.find('tejido')
            if tejido is not None:
                rejilla = tejido.find('rejilla').text if tejido.find('rejilla') is not None else ""
                filas = int(tejido.get('filas'))
                columnas = int(tejido.get('columnas'))
            
            parejas = ""
            proteinas = experimento.find('proteinas')
            if proteinas is not None:
                primera_pareja = True 
                for pareja in proteinas.findall('pareja'):
                    pareja_texto = pareja.text.strip() if pareja.text else ""
                    if pareja_texto:
                        if not primera_pareja:
                            parejas += ", " 
                        parejas += pareja_texto
                        primera_pareja = False

            

            self._experimentos.insertar(nombre, filas, columnas, rejilla, parejas, iteracion)

    
    def _generar_rejilla(self, archivo, raiz, filas, columnas, estado):
        nombre_archivo = f"{archivo}_estado{estado}"
        with open(f"graficas/{nombre_archivo}.dot", "w", encoding="utf-8") as file:
            file.write("digraph G {\n")
            file.write("\trankdir = LR;\n")
            file.write(f'\tlabel="Estado: {estado}"\n')
            file.write("\tlabelloc=t;\n")
            file.write('\tnode [shape = plaintext, width=3, height=2];\n')
            file.write('\testado [label = <\n')
            file.write('\t\t<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">\n')
  
            file.write("\t\t\t<TR><TD></TD>")
            for j in range(1, columnas + 1):
                file.write(f"<TD>{j}</TD>")
            file.write("</TR>\n")
         
            fila_actual = raiz
            for i in range(1, filas + 1):
                file.write("\t\t\t<TR>\n")
                file.write(f"\t\t\t\t<TD CELLPADDING='5'>{i}</TD>\n")
                nodo_actual = fila_actual
                for j in range(1, columnas + 1):
                    if nodo_actual:
                        if nodo_actual.get_es_inerte():
                            file.write(f"\t\t\t\t<TD BGCOLOR='red'>{nodo_actual.get_proteina()}</TD>\n")
                        else:
                            file.write(f"\t\t\t\t<TD>{nodo_actual.get_proteina()}</TD>\n")
                        nodo_actual = nodo_actual.siguiente
                    else:
                        file.write("\t\t\t\t<TD></TD>\n")
                file.write("\t\t\t</TR>\n")
                if fila_actual:
                    fila_actual = fila_actual.abajo
            file.write("\t\t</TABLE>>];\n")
            file.write("}\n")

        subprocess.run(f"dot -Tsvg graficas/{nombre_archivo}.dot -o graficas/{nombre_archivo}.svg", shell=True)
        print(f"Se ha generado la gráfica: {estado} del experimento")