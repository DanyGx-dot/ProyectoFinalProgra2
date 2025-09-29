class Estudiante:
    _contador_id = 1
    
    def __init__(self, nombre, edad, carrera, promedio, semestre, email):
        self.id = Estudiante._contador_id
        Estudiante._contador_id += 1
        self.nombre = nombre
        self.edad = int(edad)
        self.carrera = carrera
        self.promedio = float(promedio)
        self.semestre = int(semestre)
        self.email = email
        self.activo = True
    
    def __str__(self):
        return f"{self.nombre} ({self.carrera}, Semestre {self.semestre})"
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'edad': self.edad,
            'carrera': self.carrera,
            'promedio': self.promedio,
            'semestre': self.semestre,
            'email': self.email,
            'activo': self.activo
        }