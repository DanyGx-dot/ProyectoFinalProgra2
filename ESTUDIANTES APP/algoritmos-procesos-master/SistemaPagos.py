import json
import os
from datetime import datetime, timedelta

class SistemaPagos:
    def __init__(self, gestor_estudiantes):
        self.gestor = gestor_estudiantes
        self.archivo_datos = "pagos.json"
        self.pagos = self.cargar_datos()
        self.mensualidad_base = 1000  # Monto base de la colegiatura
    
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
                json.dump(self.pagos, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando pagos: {e}")
    
    def calcular_mensualidad(self, id_estudiante):
        estudiante = next((e for e in self.gestor.obtener_todos() if e.id == id_estudiante), None)
        if not estudiante:
            return self.mensualidad_base
        
        # Puedes personalizar el cálculo según carrera, semestre, etc.
        mensualidad = self.mensualidad_base
        
        # Ejemplo: carreas más costosas
        if estudiante.carrera in ["Medicina", "Ingeniería Civil"]:
            mensualidad *= 1.3
        
        # Ejemplo: semestres avanzados pueden tener costos diferentes
        if estudiante.semestre >= 7:
            mensualidad *= 1.1
        
        return round(mensualidad, 2)
    
    def registrar_pago(self, id_estudiante, monto, mes, año, metodo_pago, referencia=""):
        if str(id_estudiante) not in self.pagos:
            self.pagos[str(id_estudiante)] = []
        
        pago = {
            'monto': float(monto),
            'mes': mes,
            'año': año,
            'metodo_pago': metodo_pago,
            'referencia': referencia,
            'fecha_pago': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'estado': 'completado'
        }
        
        self.pagos[str(id_estudiante)].append(pago)
        self.guardar_datos()
        return pago
    
    def obtener_pagos_estudiante(self, id_estudiante):
        return self.pagos.get(str(id_estudiante), [])
    
    def verificar_pago_mensual(self, id_estudiante, mes, año):
        pagos = self.obtener_pagos_estudiante(id_estudiante)
        for pago in pagos:
            if pago['mes'] == mes and pago['año'] == año and pago['estado'] == 'completado':
                return True
        return False
    
    def calcular_deuda_actual(self, id_estudiante):
        # Calcular meses pendientes del año actual
        año_actual = datetime.now().year
        mes_actual = datetime.now().month
        
        deuda = 0
        for mes in range(1, mes_actual + 1):
            if not self.verificar_pago_mensual(id_estudiante, mes, año_actual):
                deuda += self.calcular_mensualidad(id_estudiante)
        
        return deuda
    
    def generar_estado_cuenta(self, id_estudiante):
        pagos = self.obtener_pagos_estudiante(id_estudiante)
        deuda = self.calcular_deuda_actual(id_estudiante)
        mensualidad = self.calcular_mensualidad(id_estudiante)
        
        return {
            'mensualidad_actual': mensualidad,
            'total_pagado': sum(p['monto'] for p in pagos),
            'deuda_actual': deuda,
            'pagos_registrados': len(pagos),
            'proximo_vencimiento': self.calcular_proximo_vencimiento()
        }
    
    def calcular_proximo_vencimiento(self):
        hoy = datetime.now()
        if hoy.day > 5:  # Suponiendo vencimiento día 5 de cada mes
            próximo_mes = hoy.replace(day=1) + timedelta(days=32)
            próximo_mes = próximo_mes.replace(day=5)
        else:
            próximo_mes = hoy.replace(day=5)
        
        return próximo_mes.strftime("%Y-%m-%d")