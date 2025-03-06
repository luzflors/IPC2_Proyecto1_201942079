import xml.etree.ElementTree as ET
import subprocess as ET

class Nodo():
    def __init__(self, proteina, estado):
        self._proteina = proteina
        self._estado = estado
        self.siguiente = None

    def get_proteina(self):
        return self._proteina

    def get_estado(self):
        return self._estado
    
    def set_estado(self, estado):
        self._estado = estado
    
    def mostrar(self):
        print(f"{self.get_proteina()}")
        
class Lista_proteina():
    def __init__(self):
        self.primero = None

    def insertar_inicio(self, proteina, estado):
        nuevo = Nodo(proteina, estado)
        if self.primero is None:
            self.primero = nuevo
        else:
            nuevo.siguiente = self.primero
            self.primero = nuevo

    def insertar_final(self, proteina, estado):
        nuevo = Nodo(proteina, estado)
        if self.primero is None:
            self.primero = nuevo
        else:
            tmp = self.primero
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
    
    def buscar(self, proteina):
        tmp = self.primero
        while tmp:
            if tmp.get_proteina() == proteina:
                return tmp
            tmp = tmp.siguiente
        return None
    
    def eliminar(self, proteina):
        if self.primero is None:
            print('No existen proteinas')
        elif self.primero.get_proteina() == proteina:
            tmp = self.primero
            self.primero = tmp.siguiente
            tmp.siguiente = None
            print('Proteina eliminada correctamente')
        else:
            prev = self.primero
            tmp = self.primero.siguiente
            while tmp:
                if tmp.get_proteina() == proteina:
                    prev.siguiente = tmp.siguiente
                    tmp.siguiente = None
                    print('Proteina eliminada correctamente')
                    return
                prev = tmp
                tmp = tmp.siguiente
            print('Error al eliminar, la proteina no existe')
    
    def mostrar_lista(self):
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

class ExperimentoXML():
    def __init__(self, archivo):
        self._archivo = archivo
        self._rejilla_txt = None
        self._pareja_txt = None
        self._columnas_txt = None
        self._filas_txt = None
        self._nombre_exp = None
    
    def _cargar_xml(self):
        try:
            xml_file = ET.parse(self._archivo)
            return xml_file.getroot()
        except Exception as err:
            print("Error:", err)
        return None
    
    def extraer_xml(self):
        xml_raiz = self._cargar_xml()
        for experimento in xml_raiz.findall('experimento'):
            self._nombre_exp = experimento.get('nombre')
            if self._nombre_exp is None:
                self._nombre_exp = 'Experimento'
            tejido = experimento.find('tejido')
            if tejido is not None:
                self._rejilla_txt = tejido.find('rejilla').text
                self._filas_txt = tejido.get('filas')
                self._columnas_txt = tejido.get('columnas')
            proteina = experimento.find('proteinas')
            if proteina is not None:
                pareja = proteina.find('pareja')
                self._pareja_txt = pareja.text
    
    def get_nombre(self):
        if self._nombre_exp is not None:
            self._nombre_exp = 'Experimento'
        return self._nombre_exp
        
    
    def get_rejilla(self):
        return self._rejilla_txt

    
    def get_pareja(self):
        return self._pareja_txt
    
    def get_columnas(self):
        if self._columnas_txt is not None:
            return int(self._columnas_txt)
        else:
            return 0
    
    def get_filas(self):
        if self._filas_txt is not None:
            return int(self._filas_txt)
        else:
            return 0
    
    def generar_rejilla(self, nombre_archivo, lista, estado):
        with open(f'{nombre_archivo}.dot', 'w', encoding='utf-8') as file:
            file.write('digraph G {\n')
            file.write('\trankdir = LR;\n')
            file.write(f'\tlabel="Estados {estado}"\n')
            file.write('\tlabelloc=t;\n') 
            file.write('\tnode [shape = plaintext, color="#b8b0b0b8", width=3, height=2];\n')
            file.write('\testado [label = <\n')
            file.write('\t\t<TABLE BORDER="0" CELLBORDER="0">\n')
            
            file.write('\t\t\t<TR><TD></TD>')
            for j in range(1, self._columnas_txt + 1):
                file.write(f'<TD BORDER="0">{j}</TD>')
            file.write('</TR>\n')
            
            index = 0
            for i in range(1, self._filas_txt + 1):
                file.write('\t\t\t<TR>\n')
                file.write(f'\t\t\t\t<TD BORDER="0" CELLPADDING="15">{i}</TD>\n')
                for j in range(self._columnas_txt):
                    if index < len(lista):
                        protein = lista[index]
                        index += 1
                        file.write(f'\t\t\t\t<TD>{protein}</TD>\n')
                    else:
                        file.write('\t\t\t\t<TD></TD>\n')
                file.write('\t\t\t</TR>\n')
            
            file.write('\t\t</TABLE>>];\n')
            file.write('}\n')
        
        import subprocess
        subprocess.run(f"dot -Tsvg {nombre_archivo}.dot -o {nombre_archivo}.svg", shell=True)
