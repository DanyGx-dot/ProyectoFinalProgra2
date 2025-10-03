from Estudiante import Estudiante
import json
import os

class GestorEstudiantes:
    def __init__(self):
        self.estudiantes = []
        self.archivo_datos = "estudiantes.json"
        self.cargar_datos()
    
    def cargar_datos(self):
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                    datos = json.load(f)
                    for est_data in datos:
                        estudiante = Estudiante(
                            est_data['nombre'],
                            est_data['edad'],
                            est_data['carrera'],
                            est_data['promedio'],
                            est_data['semestre'],
                            est_data['email']
                        )
                        estudiante.id = est_data['id']
                        estudiante.activo = est_data['activo']
                        self.estudiantes.append(estudiante)
                    # Actualizar contador ID
                    if self.estudiantes:
                        Estudiante._contador_id = max(e.id for e in self.estudiantes) + 1
            except Exception as e:
                print(f"Error cargando datos: {e}")
    
    def guardar_datos(self):
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                json.dump([e.to_dict() for e in self.estudiantes], f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando datos: {e}")
    
    def agregar_estudiante(self, nombre, edad, carrera, promedio, semestre, email):
        estudiante = Estudiante(nombre, edad, carrera, promedio, semestre, email)
        self.estudiantes.append(estudiante)
        self.guardar_datos()
        return estudiante
    
    def buscar_estudiante(self, criterio, valor):
        resultados = []
        valor = str(valor).lower()
        
        for estudiante in self.estudiantes:
            if criterio == "id" and str(estudiante.id) == valor:
                resultados.append(estudiante)
            elif criterio == "nombre" and valor in estudiante.nombre.lower():
                resultados.append(estudiante)
            elif criterio == "carrera" and valor in estudiante.carrera.lower():
                resultados.append(estudiante)
            elif criterio == "email" and valor in estudiante.email.lower():
                resultados.append(estudiante)
        
        return resultados
    
    def eliminar_estudiante(self, id_estudiante):
        for i, estudiante in enumerate(self.estudiantes):
            if estudiante.id == id_estudiante:
                del self.estudiantes[i]
                self.guardar_datos()
                return True
        return False
    
    def modificar_estudiante(self, id_estudiante, **kwargs):
        for estudiante in self.estudiantes:
            if estudiante.id == id_estudiante:
                for key, value in kwargs.items():
                    if hasattr(estudiante, key):
                        setattr(estudiante, key, value)
                self.guardar_datos()
                return True
        return False
    
    def obtener_todos(self):
        return self.estudiantes.copy()
    
    def obtener_por_carrera(self, carrera):
        return [e for e in self.estudiantes if e.carrera.lower() == carrera.lower()]
    
    def obtener_mejores_promedios(self, limite=10):
        return sorted(self.estudiantes, key=lambda x: x.promedio, reverse=True)[:limite]