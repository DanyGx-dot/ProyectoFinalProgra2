import tkinter as tk
from tkinter import ttk, messagebox
from GestorEstudiantes import GestorEstudiantes
from SistemaNotas import SistemaNotas
from ControlAsistencias import ControlAsistencias
from SistemaPagos import SistemaPagos
from datetime import datetime

class AppCompleta:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Académico Integral")
        self.root.geometry("1200x700")
        self.root.configure(bg="#1e1e1e")

        # Gestores
        self.gestor = GestorEstudiantes()
        self.sistema_notas = SistemaNotas(self.gestor)
        self.control_asistencias = ControlAsistencias(self.gestor)
        self.sistema_pagos = SistemaPagos(self.gestor)

        # Configurar estilo
        self._configurar_estilo()

        # Crear interfaz
        self._crear_interfaz()

    def _configurar_estilo(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#1e1e1e", foreground="white")
        style.configure("TFrame", background="#1e1e1e")
        style.configure("TButton", background="#2d2d2d", foreground="white")
        style.map("TButton", background=[("active", "#444444")])
        style.configure("TEntry", fieldbackground="#2d2d2d", foreground="white")
        style.configure("TCombobox", fieldbackground="#2d2d2d", background="#2d2d2d", foreground="white")
        style.configure("Treeview", background="#2d2d2d", fieldbackground="#2d2d2d", foreground="white")
        style.map("Treeview", background=[("selected", "#444444")], foreground=[("selected", "white")])

    def _crear_interfaz(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestañas
        self.frame_estudiantes = ttk.Frame(notebook)
        self.frame_notas = ttk.Frame(notebook)
        self.frame_asistencias = ttk.Frame(notebook)
        self.frame_pagos = ttk.Frame(notebook)

        notebook.add(self.frame_estudiantes, text="Gestión de Estudiantes")
        notebook.add(self.frame_notas, text="Sistema de Notas")
        notebook.add(self.frame_asistencias, text="Control de Asistencias")
        notebook.add(self.frame_pagos, text="Pagos de Colegiatura")

        self._crear_interfaz_estudiantes()
        self._crear_interfaz_notas()
        self._crear_interfaz_asistencias()
        self._crear_interfaz_pagos()

    def _crear_interfaz_estudiantes(self):
        # (Aquí va todo el código original de la clase App para gestión de estudiantes)
        # Para ahorrar espacio, solo pongo el esqueleto
        pass

    def _crear_interfaz_notas(self):
        frame = ttk.Frame(self.frame_notas)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(frame, text="Sistema de Gestión de Notas", font=('Arial', 16)).pack(pady=10)

        # Frame de controles
        frame_controles = ttk.Frame(frame)
        frame_controles.pack(fill="x", pady=10)

        ttk.Label(frame_controles, text="Estudiante:").grid(row=0, column=0, padx=5, sticky="w")
        self.combo_estudiantes_notas = ttk.Combobox(frame_controles, width=25)
        self.combo_estudiantes_notas.grid(row=0, column=1, padx=5)

        ttk.Label(frame_controles, text="Materia:").grid(row=0, column=2, padx=5, sticky="w")
        self.entry_materia_nota = ttk.Entry(frame_controles, width=20)
        self.entry_materia_nota.grid(row=0, column=3, padx=5)

        ttk.Label(frame_controles, text="Nota:").grid(row=0, column=4, padx=5, sticky="w")
        self.entry_nota = ttk.Entry(frame_controles, width=10)
        self.entry_nota.grid(row=0, column=5, padx=5)

        ttk.Label(frame_controles, text="Periodo:").grid(row=1, column=0, padx=5, sticky="w")
        self.combo_periodo = ttk.Combobox(frame_controles, values=["2024-1", "2024-2", "2025-1", "2025-2"], width=10)
        self.combo_periodo.set("2024-1")
        self.combo_periodo.grid(row=1, column=1, padx=5)

        ttk.Label(frame_controles, text="Tipo:").grid(row=1, column=2, padx=5, sticky="w")
        self.combo_tipo_nota = ttk.Combobox(frame_controles, values=["Parcial", "Quiz", "Proyecto", "Final"], width=10)
        self.combo_tipo_nota.set("Parcial")
        self.combo_tipo_nota.grid(row=1, column=3, padx=5)

        ttk.Button(frame_controles, text="Agregar Nota", command=self.agregar_nota).grid(row=1, column=4, columnspan=2, padx=5)

        # Treeview de notas
        self.tree_notas = ttk.Treeview(frame, columns=("Estudiante", "Materia", "Nota", "Periodo", "Tipo", "Fecha"), show="headings", height=15)
        for col in ("Estudiante", "Materia", "Nota", "Periodo", "Tipo", "Fecha"):
            self.tree_notas.heading(col, text=col)
            self.tree_notas.column(col, width=120)
        self.tree_notas.pack(fill="both", expand=True, pady=10)

        # Botones adicionales
        frame_botones = ttk.Frame(frame)
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text="Cargar Notas del Estudiante", command=self.cargar_notas_estudiante).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Calcular Promedio", command=self.calcular_promedio).pack(side="left", padx=5)

        self.actualizar_combo_estudiantes_notas()

    def _crear_interfaz_asistencias(self):
        frame = ttk.Frame(self.frame_asistencias)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(frame, text="Control de Asistencias", font=('Arial', 16)).pack(pady=10)

        # (Implementación similar a la interfaz de notas)
        # Controles para registrar asistencia
        # Treeview para mostrar asistencias
        # Botones para generar reportes

    def _crear_interfaz_pagos(self):
        frame = ttk.Frame(self.frame_pagos)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(frame, text="Sistema de Pagos de Colegiatura", font=('Arial', 16)).pack(pady=10)

        # (Implementación similar)
        # Controles para registrar pagos
        # Información de mensualidad y deuda
        # Estado de cuenta

    def actualizar_combo_estudiantes_notas(self):
        estudiantes = self.gestor.obtener_todos()
        self.combo_estudiantes_notas['values'] = [f"{e.id} - {e.nombre}" for e in estudiantes]

    def agregar_nota(self):
        try:
            estudiante_text = self.combo_estudiantes_notas.get()
            materia = self.entry_materia_nota.get().strip()
            nota = float(self.entry_nota.get().strip())
            periodo = self.combo_periodo.get()
            tipo = self.combo_tipo_nota.get()

            if not all([estudiante_text, materia, periodo, tipo]):
                raise ValueError("Todos los campos son obligatorios")

            if nota < 0 or nota > 10:
                raise ValueError("La nota debe estar entre 0 y 10")

            id_estudiante = int(estudiante_text.split(' - ')[0])
            self.sistema_notas.agregar_nota(id_estudiante, materia, nota, periodo, tipo)

            # Actualizar treeview
            estudiante = next(e for e in self.gestor.obtener_todos() if e.id == id_estudiante)
            self.tree_notas.insert("", "end", values=(
                estudiante.nombre, materia, nota, periodo, tipo, 
                datetime.now().strftime("%Y-%m-%d")
            ))

            messagebox.showinfo("Éxito", "Nota agregada correctamente")
            self.limpiar_campos_notas()

        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def cargar_notas_estudiante(self):
        try:
            estudiante_text = self.combo_estudiantes_notas.get()
            if not estudiante_text:
                raise ValueError("Seleccione un estudiante")
            
            id_estudiante = int(estudiante_text.split(' - ')[0])
            notas = self.sistema_notas.obtener_notas_estudiante(id_estudiante)
            
            self.tree_notas.delete(*self.tree_notas.get_children())
            estudiante = next(e for e in self.gestor.obtener_todos() if e.id == id_estudiante)
            
            for nota in notas:
                self.tree_notas.insert("", "end", values=(
                    estudiante.nombre, nota['materia'], nota['nota'], 
                    nota['periodo'], nota['tipo'], nota['fecha_registro'].split(' ')[0]
                ))
                
        except ValueError as e:
            messagebox.showerror("Error", f"Error al cargar notas: {e}")

    def calcular_promedio(self):
        try:
            estudiante_text = self.combo_estudiantes_notas.get()
            if not estudiante_text:
                raise ValueError("Seleccione un estudiante")
            
            id_estudiante = int(estudiante_text.split(' - ')[0])
            promedio = self.sistema_notas.calcular_promedio_estudiante(id_estudiante)
            
            messagebox.showinfo("Promedio", f"Promedio general: {promedio:.2f}")
            
        except ValueError as e:
            messagebox.showerror("Error", f"Error al calcular promedio: {e}")

    def limpiar_campos_notas(self):
        self.entry_materia_nota.delete(0, tk.END)
        self.entry_nota.delete(0, tk.END)

# Métodos para asistencias y pagos (implementación similar)