import xml.etree.ElementTree as ET
import subprocess

class NodoProteina():
    def __init__(self, proteina, es_inerte):
        self._proteina = proteina
        self._es_inerte = es_inerte
        self.siguiente = None

    def get_proteina(self):
        return self._proteina

    def get_estado(self):
        return self._es_inerte
    
    def set_estado(self, estado):
        self._es_inerte = estado
    
    def mostrar(self):
        print(self.get_proteina())
        
class ListaProteina():
    def __init__(self):
        self.primero = None

    def insertar(self, proteina, estado):
        nuevo = NodoProteina(proteina, estado)
        if self.primero is None:
            self.primero = nuevo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
    
    def mostrar_proteinas(self):
        tmp = self.primero
        while tmp:
            tmp.mostrar()
            tmp = tmp.siguiente

    def ver_estado(self, estado):
        tmp = self.primero
        while tmp:
            if tmp.get_estado() == estado:
                return tmp
            tmp = tmp.siguiente
        return None
    
    def limpiar(self):
        while self.primero is not None:
            tmp = self.primero  
            self.primero = self.primero.siguiente  
            tmp.siguiente = None 

class NodoParejas():
    def __init__(self, parejas):
        self._parejas = parejas
        self.siguiente = None

class ListaParejas:
    def __init__(self):
        self.primero = None  

    def insertar(self, nombre, pareja):
        nuevo = NodoParejas(nombre, pareja)
        if self.primero is None:
            self.primero = nuevo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def limpiar(self):
        while self.primero is not None:
            tmp = self.primero  
            self.primero = self.primero.siguiente  
            tmp.siguiente = None 


class NodoExperimento():
    def __init__(self, nombre, filas, columnas, rejilla, pareja):
        self._nombre = nombre 
        self._filas = int(filas)
        self._columnas = int(columnas)
        self._rejilla = rejilla 
        self._pareja = pareja 
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
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_filas(self, filas):
        self._filas = int(filas)

    def set_columnas(self, columnas):
        self._columnas = int(columnas)

    def set_rejilla(self, rejilla):
        self._rejilla = rejilla

    def set_pareja(self, pareja):
        self._pareja = pareja


class ListaExperimento:
    def __init__(self):
        self.primero = None  

    def insertar(self, nombre, filas, columnas, rejilla, pareja):
        nuevo = NodoExperimento(nombre, filas, columnas, rejilla, pareja)
        if self.primero is None:
            self.primero = nuevo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
    
    def limpiar(self):
        while self.primero is not None:
            tmp = self.primero  
            self.primero = self.primero.siguiente  
            tmp.siguiente = None 

class ExperimentoXML():
    def __init__(self, archivo):
        self._archivo = archivo
        self._experimentos = ListaExperimento()
        self._parejas = ListaParejas()
    
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
            return
        
        for experimento in xml_raiz.findall('experimento'):
            nombre = experimento.get('nombre', 'Experimento')

            rejilla = ""
            filas = 0
            columnas = 0
            pareja_texto = ""
            
            tejido = experimento.find('tejido')
            if tejido is not None:
                rejilla = tejido.find('rejilla').text if tejido.find('rejilla') is not None else ""
                filas = int(tejido.get('filas', 0) or 0)  
                columnas = int(tejido.get('columnas', 0) or 0) 
            
            proteina = experimento.find('proteinas')
            if proteina is not None:
                for parejas in proteina.findall('pareja'):
                    pareja_texto = parejas.text
                    if pareja_texto:  
                        self._parejas.insertar(nombre, pareja_texto)
            
            self._experimentos.insertar(nombre, filas, columnas, rejilla, self._parejas)

    def generar_rejilla(self, archivo, lista_proteinas, filas, columnas, estado):
        with open(f'{archivo}.dot', 'w', encoding='utf-8') as file:
            file.write('digraph G {\n')
            file.write('\trankdir = LR;\n')
            file.write(f'\tlabel="Estados {estado}"\n')
            file.write('\tlabelloc=t;\n') 
            file.write('\tnode [shape = plaintext, color="#b8b0b0b8", width=3, height=2];\n')
            file.write('\testado [label = <\n')
            file.write('\t\t<TABLE BORDER="0" CELLBORDER="0">\n')
            
            file.write('\t\t\t<TR><TD></TD>')
            for j in range(1, columnas + 1):
                file.write(f'<TD BORDER="0">{j}</TD>')
            file.write('</TR>\n')

            index = 0
            for i in range(1, filas + 1):
                file.write('\t\t\t<TR>\n')
                file.write(f'\t\t\t\t<TD BORDER="0" CELLPADDING="15">{i}</TD>\n')
                for j in range(columnas):
                    if index < len(lista_proteinas):
                        proteina = lista_proteinas[index]
                        index += 1
                        
                        file.write(f'\t\t\t\t<TD>{proteina}</TD>\n')
                    else:
                        file.write('\t\t\t\t<TD></TD>\n')
                file.write('\t\t\t</TR>\n')

            file.write('\t\t</TABLE>>];\n')
            file.write('}\n')

        subprocess.run(f"dot -Tsvg {archivo}.dot -o {archivo}.svg", shell=True)