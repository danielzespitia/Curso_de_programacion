
# Patrones de Diseño
#
# Los patrones de diseño son soluciones estandarizadas y probadas para problemas recurrentes en el diseño de software.
# No son algoritmos específicos, sino plantillas conceptuales que se pueden adaptar.
#
# Singleton (Instancia Única): Garantiza que una clase tenga una y solo una instancia, y proporciona un punto de acceso global a ella.
# Es útil para gestionar recursos compartidos como una conexión a base de datos, un gestor de configuración o un servicio de logging.
#
# Factory (Fábrica): Proporciona una interfaz para crear objetos, pero deja que las subclases decidan qué clase concreta instanciar.
# Esto desacopla el código cliente de la creación de objetos específicos.
#
# Ejemplo Extendido (Patrón Factory):
# Un sistema de exportación de documentos que puede crear diferentes tipos de exportadores (PDF, CSV) sin que el cliente sepa cómo se construye cada uno.

from abc import ABC, abstractmethod

# --- Productos ---
class Exportador(ABC):
    @abstractmethod
    def exportar(self, contenido):
        pass

class ExportadorPDF(Exportador):
    def exportar(self, contenido):
        print(f"📄 Exportando a PDF: '{contenido[:20]}...'")

class ExportadorCSV(Exportador):
    def exportar(self, contenido):
        print(f"📈 Exportando a CSV: '{contenido[:20]}...'")

# --- La Fábrica ---
class FabricaDeExportadores:
    """
    La fábrica se encarga de la lógica de creación.
    El cliente solo pide lo que necesita por un nombre.
    """
    def obtener_exportador(self, formato):
        if formato.lower() == 'pdf':
            return ExportadorPDF()
        elif formato.lower() == 'csv':
            return ExportadorCSV()
        else:
            raise ValueError(f"Formato de exportación no soportado: {formato}")

# --- Código Cliente ---
def generar_reporte(datos, formato_deseado):
    """
    El código cliente no sabe nada de ExportadorPDF o ExportadorCSV.
    Solo interactúa con la fábrica y la interfaz común (Exportador).
    """
    fabrica = FabricaDeExportadores()
    try:
        # Pide a la fábrica que le dé el objeto adecuado
        exportador = fabrica.obtener_exportador(formato_deseado)
        # Usa el objeto sin saber su tipo concreto (polimorfismo)
        exportador.exportar(datos)
    except ValueError as e:
        print(e)

# --- Uso del sistema ---
reporte_ventas = "ID,Producto,Cantidad,Precio\n1,Laptop,10,1200\n2,Mouse,50,25"
reporte_narrativo = "Este fue un trimestre exitoso con un crecimiento del 15%..."

generar_reporte(reporte_ventas, "csv")
generar_reporte(reporte_narrativo, "pdf")
generar_reporte("Datos confidenciales", "docx") # Fallará de forma controlada