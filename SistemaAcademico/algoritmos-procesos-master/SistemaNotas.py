import json
import os
from datetime import datetime

class SistemaNotas:
    def __init__(self, gestor_estudiantes):
        self.gestor = gestor_estudiantes
        self.archivo_datos = "notas.json"
        self.notas = self.cargar_datos()
    
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
                json.dump(self.notas, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando notas: {e}")
    
    def agregar_nota(self, id_estudiante, materia, nota, periodo, tipo_evaluacion):
        if str(id_estudiante) not in self.notas:
            self.notas[str(id_estudiante)] = []
        
        nueva_nota = {
            'materia': materia,
            'nota': float(nota),
            'periodo': periodo,
            'tipo': tipo_evaluacion,
            'fecha_registro': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        
        self.notas[str(id_estudiante)].append(nueva_nota)
        self.guardar_datos()
        return nueva_nota
    
    def obtener_notas_estudiante(self, id_estudiante):
        return self.notas.get(str(id_estudiante), [])
    
    def calcular_promedio_estudiante(self, id_estudiante, materia=None):
        notas = self.obtener_notas_estudiante(id_estudiante)
        if not notas:
            return 0.0
        
        if materia:
            notas = [n for n in notas if n['materia'] == materia]
            if not notas:
                return 0.0
        
        return sum(n['nota'] for n in notas) / len(notas)
    
    def obtener_materias_estudiante(self, id_estudiante):
        notas = self.obtener_notas_estudiante(id_estudiante)
        return list(set(n['materia'] for n in notas))