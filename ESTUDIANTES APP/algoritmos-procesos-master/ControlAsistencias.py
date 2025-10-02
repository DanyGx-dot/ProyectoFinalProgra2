import json
import os
from datetime import datetime, timedelta

class ControlAsistencias:
    def __init__(self, gestor_estudiantes):
        self.gestor = gestor_estudiantes
        self.archivo_datos = "asistencias.json"
        self.asistencias = self.cargar_datos()
    
    def cargar_datos(self):
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def guardar_datos(self):
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                json.dump(self.asistencias, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando asistencias: {e}")
    
    def registrar_asistencia(self, id_estudiante, materia, fecha, estado, observaciones=""):
        clave = f"{id_estudiante}_{materia}"
        if clave not in self.asistencias:
            self.asistencias[clave] = []
        
        registro = {
            'fecha': fecha,
            'estado': estado,  # 'presente', 'ausente', 'tardanza', 'justificado'
            'observaciones': observaciones,
            'fecha_registro': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.asistencias[clave].append(registro)
        self.guardar_datos()
        return registro
    
    def obtener_asistencias_estudiante(self, id_estudiante, materia=None):
        resultados = []
        for clave, registros in self.asistencias.items():
            if clave.startswith(f"{id_estudiante}_"):
                if materia is None or clave.endswith(f"_{materia}"):
                    resultados.extend(registros)
        return sorted(resultados, key=lambda x: x['fecha'])
    
    def calcular_porcentaje_asistencia(self, id_estudiante, materia, periodo):
        asistencias = self.obtener_asistencias_estudiante(id_estudiante, materia)
        if not asistencias:
            return 0.0
        
        asistencias_periodo = [a for a in asistencias if periodo in a['fecha']]
        if not asistencias_periodo:
            return 0.0
        
        presentes = len([a for a in asistencias_periodo if a['estado'] in ['presente', 'tardanza']])
        return (presentes / len(asistencias_periodo)) * 100
    
    def generar_reporte_mensual(self, id_estudiante, año, mes):
        asistencias = self.obtener_asistencias_estudiante(id_estudiante)
        mes_str = str(mes).zfill(2)
        asistencias_mes = [a for a in asistencias if f"{año}-{mes_str}" in a['fecha']]
        
        reporte = {
            'total_clases': len(asistencias_mes),
            'presentes': len([a for a in asistencias_mes if a['estado'] == 'presente']),
            'tardanzas': len([a for a in asistencias_mes if a['estado'] == 'tardanza']),
            'ausentes': len([a for a in asistencias_mes if a['estado'] == 'ausente']),
            'justificados': len([a for a in asistencias_mes if a['estado'] == 'justificado']),
            'porcentaje_asistencia': 0.0
        }
        
        if reporte['total_clases'] > 0:
            efectivas = reporte['presentes'] + reporte['tardanzas'] + reporte['justificados']
            reporte['porcentaje_asistencia'] = (efectivas / reporte['total_clases']) * 100
        
        return reporte