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
        # Copiar la interfaz completa de App.py para gestión de estudiantes
        frame = ttk.Frame(self.frame_estudiantes)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        ttk.Label(frame, text="Gestión de Estudiantes", font=('Arial', 16)).pack(pady=10)

        # Frame de registro
        frame_registro = ttk.LabelFrame(frame, text="Registrar Nuevo Estudiante")
        frame_registro.pack(fill="x", pady=10, padx=10)

        ttk.Label(frame_registro, text="Nombre completo:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.nombre_entry = ttk.Entry(frame_registro, width=30)
        self.nombre_entry.grid(row=0, column=1, pady=5, padx=10)

        ttk.Label(frame_registro, text="Edad:").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        self.edad_entry = ttk.Entry(frame_registro, width=30)
        self.edad_entry.grid(row=1, column=1, pady=5, padx=10)

        ttk.Label(frame_registro, text="Carrera:").grid(row=2, column=0, sticky="w", pady=5, padx=5)
        self.carrera_combobox = ttk.Combobox(frame_registro, width=27, values=[
            "Ingeniería de Sistemas", "Medicina", "Derecho", "Administración", 
            "Contaduría", "Psicología", "Ingeniería Civil", "Arquitectura"
        ])
        self.carrera_combobox.grid(row=2, column=1, pady=5, padx=10)

        ttk.Label(frame_registro, text="Promedio:").grid(row=3, column=0, sticky="w", pady=5, padx=5)
        self.promedio_entry = ttk.Entry(frame_registro, width=30)
        self.promedio_entry.grid(row=3, column=1, pady=5, padx=10)

        ttk.Label(frame_registro, text="Semestre:").grid(row=4, column=0, sticky="w", pady=5, padx=5)
        self.semestre_combobox = ttk.Combobox(frame_registro, width=27, values=[str(i) for i in range(1, 11)])
        self.semestre_combobox.grid(row=4, column=1, pady=5, padx=10)

        ttk.Label(frame_registro, text="Email:").grid(row=5, column=0, sticky="w", pady=5, padx=5)
        self.email_entry = ttk.Entry(frame_registro, width=30)
        self.email_entry.grid(row=5, column=1, pady=5, padx=10)

        ttk.Button(frame_registro, text="Registrar Estudiante", command=self.registrar_estudiante).grid(row=6, column=0, columnspan=2, pady=15)

        # Frame de búsqueda
        frame_busqueda = ttk.LabelFrame(frame, text="Buscar Estudiantes")
        frame_busqueda.pack(fill="x", pady=10, padx=10)

        ttk.Label(frame_busqueda, text="Criterio de búsqueda:").grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.criterio_busqueda = ttk.Combobox(frame_busqueda, values=["Nombre", "Carrera", "Email", "ID"])
        self.criterio_busqueda.current(0)
        self.criterio_busqueda.grid(row=0, column=1, pady=5, padx=10)

        ttk.Label(frame_busqueda, text="Valor a buscar:").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        self.valor_busqueda = ttk.Entry(frame_busqueda, width=30)
        self.valor_busqueda.grid(row=1, column=1, pady=5, padx=10)

        ttk.Button(frame_busqueda, text="Buscar", command=self.buscar_estudiantes).grid(row=2, column=0, columnspan=2, pady=10)

        # Treeview para resultados
        self.tree_estudiantes = ttk.Treeview(frame_busqueda, columns=("ID", "Nombre", "Edad", "Carrera", "Promedio", "Semestre", "Email"), show="headings", height=8)
        for col in ("ID", "Nombre", "Edad", "Carrera", "Promedio", "Semestre", "Email"):
            self.tree_estudiantes.heading(col, text=col)
            self.tree_estudiantes.column(col, width=100, anchor="center")
        self.tree_estudiantes.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

        # Botones de acción
        frame_botones = ttk.Frame(frame_busqueda)
        frame_botones.grid(row=4, column=0, columnspan=2, pady=10)
        
        ttk.Button(frame_botones, text="Eliminar Seleccionado", command=self.eliminar_estudiante).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Modificar Seleccionado", command=self.modificar_estudiante).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Mostrar Todos", command=self.mostrar_todos_estudiantes).pack(side="left", padx=5)

        # Mostrar todos los estudiantes al inicio
        self.mostrar_todos_estudiantes()

    def _crear_interfaz_notas(self):
        frame = ttk.Frame(self.frame_notas)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(frame, text="Sistema de Gestión de Notas", font=('Arial', 16)).pack(pady=10)

        # Frame de controles
        frame_controles = ttk.LabelFrame(frame, text="Agregar Nueva Nota")
        frame_controles.pack(fill="x", pady=10, padx=10)

        ttk.Label(frame_controles, text="Estudiante:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.combo_estudiantes_notas = ttk.Combobox(frame_controles, width=25)
        self.combo_estudiantes_notas.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_controles, text="Materia:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_materia_nota = ttk.Entry(frame_controles, width=20)
        self.entry_materia_nota.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_controles, text="Nota (0-10):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_nota = ttk.Entry(frame_controles, width=10)
        self.entry_nota.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_controles, text="Periodo:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.combo_periodo = ttk.Combobox(frame_controles, values=["2024-1", "2024-2", "2025-1", "2025-2"], width=10)
        self.combo_periodo.set("2024-1")
        self.combo_periodo.grid(row=1, column=3, padx=5, pady=5)

        ttk.Label(frame_controles, text="Tipo:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.combo_tipo_nota = ttk.Combobox(frame_controles, values=["Parcial", "Quiz", "Proyecto", "Final"], width=10)
        self.combo_tipo_nota.set("Parcial")
        self.combo_tipo_nota.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(frame_controles, text="Agregar Nota", command=self.agregar_nota).grid(row=2, column=2, columnspan=2, padx=5, pady=5)

        # Treeview de notas
        frame_tree = ttk.LabelFrame(frame, text="Historial de Notas")
        frame_tree.pack(fill="both", expand=True, pady=10, padx=10)
        
        self.tree_notas = ttk.Treeview(frame_tree, columns=("Estudiante", "Materia", "Nota", "Periodo", "Tipo", "Fecha"), show="headings", height=15)
        for col in ("Estudiante", "Materia", "Nota", "Periodo", "Tipo", "Fecha"):
            self.tree_notas.heading(col, text=col)
            self.tree_notas.column(col, width=120)
        
        scrollbar = ttk.Scrollbar(frame_tree, orient="vertical", command=self.tree_notas.yview)
        self.tree_notas.configure(yscrollcommand=scrollbar.set)
        
        self.tree_notas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Botones adicionales
        frame_botones = ttk.Frame(frame)
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text="Cargar Notas del Estudiante", command=self.cargar_notas_estudiante).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Calcular Promedio", command=self.calcular_promedio).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Limpiar Campos", command=self.limpiar_campos_notas).pack(side="left", padx=5)

        self.actualizar_combo_estudiantes_notas()

    def _crear_interfaz_asistencias(self):
        frame = ttk.Frame(self.frame_asistencias)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(frame, text="Control de Asistencias", font=('Arial', 16)).pack(pady=10)

        # Frame de controles
        frame_controles = ttk.LabelFrame(frame, text="Registrar Asistencia")
        frame_controles.pack(fill="x", pady=10, padx=10)

        ttk.Label(frame_controles, text="Estudiante:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.combo_estudiantes_asistencias = ttk.Combobox(frame_controles, width=25)
        self.combo_estudiantes_asistencias.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_controles, text="Materia:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_materia_asistencia = ttk.Entry(frame_controles, width=20)
        self.entry_materia_asistencia.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_controles, text="Fecha (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_fecha_asistencia = ttk.Entry(frame_controles, width=15)
        self.entry_fecha_asistencia.insert(0, datetime.now().strftime("%Y-%m-%d"))
        self.entry_fecha_asistencia.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_controles, text="Estado:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.combo_estado_asistencia = ttk.Combobox(frame_controles, values=["Presente", "Ausente", "Tardanza", "Justificado"], width=10)
        self.combo_estado_asistencia.set("Presente")
        self.combo_estado_asistencia.grid(row=1, column=3, padx=5, pady=5)

        ttk.Button(frame_controles, text="Registrar Asistencia", command=self.registrar_asistencia).grid(row=2, column=0, columnspan=4, padx=5, pady=10)

        # Treeview de asistencias
        frame_tree = ttk.LabelFrame(frame, text="Historial de Asistencias")
        frame_tree.pack(fill="both", expand=True, pady=10, padx=10)
        
        self.tree_asistencias = ttk.Treeview(frame_tree, columns=("Estudiante", "Materia", "Fecha", "Estado", "Registro"), show="headings", height=15)
        for col in ("Estudiante", "Materia", "Fecha", "Estado", "Registro"):
            self.tree_asistencias.heading(col, text=col)
            self.tree_asistencias.column(col, width=120)
        
        scrollbar = ttk.Scrollbar(frame_tree, orient="vertical", command=self.tree_asistencias.yview)
        self.tree_asistencias.configure(yscrollcommand=scrollbar.set)
        
        self.tree_asistencias.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Botones adicionales
        frame_botones = ttk.Frame(frame)
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text="Cargar Asistencias del Estudiante", command=self.cargar_asistencias_estudiante).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Generar Reporte Mensual", command=self.generar_reporte_mensual).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Limpiar Campos", command=self.limpiar_campos_asistencias).pack(side="left", padx=5)

        self.actualizar_combo_estudiantes_asistencias()

    def _crear_interfaz_pagos(self):
        frame = ttk.Frame(self.frame_pagos)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(frame, text="Sistema de Pagos de Colegiatura", font=('Arial', 16)).pack(pady=10)

        # Frame de controles
        frame_controles = ttk.LabelFrame(frame, text="Registrar Pago")
        frame_controles.pack(fill="x", pady=10, padx=10)

        ttk.Label(frame_controles, text="Estudiante:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.combo_estudiantes_pagos = ttk.Combobox(frame_controles, width=25)
        self.combo_estudiantes_pagos.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_controles, text="Monto:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_monto_pago = ttk.Entry(frame_controles, width=10)
        self.entry_monto_pago.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_controles, text="Mes:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.combo_mes_pago = ttk.Combobox(frame_controles, values=[str(i) for i in range(1,13)], width=10)
        self.combo_mes_pago.set(str(datetime.now().month))
        self.combo_mes_pago.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame_controles, text="Año:").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.entry_año_pago = ttk.Entry(frame_controles, width=10)
        self.entry_año_pago.insert(0, str(datetime.now().year))
        self.entry_año_pago.grid(row=1, column=3, padx=5, pady=5)

        ttk.Label(frame_controles, text="Método de pago:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.combo_metodo_pago = ttk.Combobox(frame_controles, values=["Efectivo", "Tarjeta", "Transferencia"], width=10)
        self.combo_metodo_pago.set("Efectivo")
        self.combo_metodo_pago.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(frame_controles, text="Registrar Pago", command=self.registrar_pago).grid(row=2, column=2, columnspan=2, padx=5, pady=5)

        # Información de mensualidad y deuda
        frame_info = ttk.LabelFrame(frame, text="Información Financiera")
        frame_info.pack(fill="x", pady=10, padx=10)

        ttk.Label(frame_info, text="Mensualidad actual:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.label_mensualidad = ttk.Label(frame_info, text="Q0.00")
        self.label_mensualidad.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame_info, text="Deuda actual:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.label_deuda = ttk.Label(frame_info, text="Q0.00")
        self.label_deuda.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        ttk.Button(frame_info, text="Calcular Deuda", command=self.calcular_deuda).grid(row=0, column=4, padx=5, pady=5)

        # Treeview de pagos
        frame_tree = ttk.LabelFrame(frame, text="Historial de Pagos")
        frame_tree.pack(fill="both", expand=True, pady=10, padx=10)
        
        self.tree_pagos = ttk.Treeview(frame_tree, columns=("Estudiante", "Monto", "Mes", "Año", "Método", "Fecha"), show="headings", height=15)
        for col in ("Estudiante", "Monto", "Mes", "Año", "Método", "Fecha"):
            self.tree_pagos.heading(col, text=col)
            self.tree_pagos.column(col, width=120)
        
        scrollbar = ttk.Scrollbar(frame_tree, orient="vertical", command=self.tree_pagos.yview)
        self.tree_pagos.configure(yscrollcommand=scrollbar.set)
        
        self.tree_pagos.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Botones adicionales
        frame_botones = ttk.Frame(frame)
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text="Cargar Pagos del Estudiante", command=self.cargar_pagos_estudiante).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Generar Estado de Cuenta", command=self.generar_estado_cuenta).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Limpiar Campos", command=self.limpiar_campos_pagos).pack(side="left", padx=5)

        self.actualizar_combo_estudiantes_pagos()

    # Métodos para estudiantes
    def registrar_estudiante(self):
        try:
            nombre = self.nombre_entry.get().strip()
            edad = self.edad_entry.get().strip()
            carrera = self.carrera_combobox.get().strip()
            promedio = self.promedio_entry.get().strip()
            semestre = self.semestre_combobox.get().strip()
            email = self.email_entry.get().strip()

            if not all([nombre, edad, carrera, promedio, semestre, email]):
                raise ValueError("Todos los campos son obligatorios")

            if not email.count('@') == 1:
                raise ValueError("Email inválido")

            edad = int(edad)
            promedio = float(promedio)
            semestre = int(semestre)

            if edad < 18 or edad > 80:
                raise ValueError("Edad debe estar entre 18 y 80 años")
            if promedio < 0 or promedio > 5.0:
                raise ValueError("Promedio debe estar entre 0.0 y 5.0")
            if semestre < 1 or semestre > 10:
                raise ValueError("Semestre debe estar entre 1 y 10")

            estudiante = self.gestor.agregar_estudiante(nombre, edad, carrera, promedio, semestre, email)
            messagebox.showinfo("Éxito", f"Estudiante {estudiante.nombre} registrado correctamente (ID: {estudiante.id})")
            
            # Limpiar campos
            for entry in [self.nombre_entry, self.edad_entry, self.promedio_entry, self.email_entry]:
                entry.delete(0, tk.END)
            self.carrera_combobox.set('')
            self.semestre_combobox.set('')

            # Actualizar combobox en otras pestañas
            self.actualizar_combo_estudiantes_notas()
            self.actualizar_combo_estudiantes_asistencias()
            self.actualizar_combo_estudiantes_pagos()
            self.mostrar_todos_estudiantes()

        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def buscar_estudiantes(self):
        criterio = self.criterio_busqueda.get().lower()
        valor = self.valor_busqueda.get().strip()
        
        if not valor:
            messagebox.showwarning("Advertencia", "Ingrese un valor para buscar")
            return
        
        resultados = self.gestor.buscar_estudiante(criterio, valor)
        self._actualizar_treeview_estudiantes(self.tree_estudiantes, resultados)

    def mostrar_todos_estudiantes(self):
        estudiantes = self.gestor.obtener_todos()
        self._actualizar_treeview_estudiantes(self.tree_estudiantes, estudiantes)

    def _actualizar_treeview_estudiantes(self, treeview, estudiantes):
        treeview.delete(*treeview.get_children())
        for estudiante in estudiantes:
            treeview.insert("", "end", values=(
                estudiante.id,
                estudiante.nombre,
                estudiante.edad,
                estudiante.carrera,
                f"{estudiante.promedio:.2f}",
                estudiante.semestre,
                estudiante.email
            ))

    def eliminar_estudiante(self):
        seleccionado = self.tree_estudiantes.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un estudiante para eliminar")
            return
        
        id_estudiante = int(self.tree_estudiantes.item(seleccionado[0])['values'][0])
        nombre = self.tree_estudiantes.item(seleccionado[0])['values'][1]
        
        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar a {nombre}?"):
            if self.gestor.eliminar_estudiante(id_estudiante):
                messagebox.showinfo("Éxito", "Estudiante eliminado correctamente")
                self.mostrar_todos_estudiantes()
                # Actualizar combobox en otras pestañas
                self.actualizar_combo_estudiantes_notas()
                self.actualizar_combo_estudiantes_asistencias()
                self.actualizar_combo_estudiantes_pagos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el estudiante")

    def modificar_estudiante(self):
        seleccionado = self.tree_estudiantes.selection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un estudiante para modificar")
            return
        
        self.ventana_modificar = tk.Toplevel(self.root)
        self.ventana_modificar.title("Modificar Estudiante")
        self.ventana_modificar.geometry("400x300")
        
        valores = self.tree_estudiantes.item(seleccionado[0])['values']
        self.estudiante_modificar_id = valores[0]
        
        ttk.Label(self.ventana_modificar, text="Nombre:").pack(pady=5)
        self.mod_nombre = ttk.Entry(self.ventana_modificar, width=30)
        self.mod_nombre.insert(0, valores[1])
        self.mod_nombre.pack(pady=5)
        
        ttk.Label(self.ventana_modificar, text="Promedio:").pack(pady=5)
        self.mod_promedio = ttk.Entry(self.ventana_modificar, width=30)
        self.mod_promedio.insert(0, valores[4])
        self.mod_promedio.pack(pady=5)
        
        ttk.Label(self.ventana_modificar, text="Semestre:").pack(pady=5)
        self.mod_semestre = ttk.Combobox(self.ventana_modificar, values=[str(i) for i in range(1, 11)])
        self.mod_semestre.set(valores[5])
        self.mod_semestre.pack(pady=5)
        
        ttk.Button(self.ventana_modificar, text="Guardar Cambios", command=self.guardar_modificacion).pack(pady=20)

    def guardar_modificacion(self):
        try:
            cambios = {}
            cambios['nombre'] = self.mod_nombre.get().strip()
            cambios['promedio'] = float(self.mod_promedio.get().strip())
            cambios['semestre'] = int(self.mod_semestre.get().strip())
            
            if self.gestor.modificar_estudiante(self.estudiante_modificar_id, **cambios):
                messagebox.showinfo("Éxito", "Estudiante modificado correctamente")
                self.ventana_modificar.destroy()
                self.mostrar_todos_estudiantes()
                # Actualizar combobox en otras pestañas
                self.actualizar_combo_estudiantes_notas()
                self.actualizar_combo_estudiantes_asistencias()
                self.actualizar_combo_estudiantes_pagos()
            else:
                messagebox.showerror("Error", "No se pudo modificar el estudiante")
                
        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    # Métodos para notas
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

            estudiante = next(e for e in self.gestor.obtener_todos() if e.id == id_estudiante)
            self.tree_notas.insert("", "end", values=(
                estudiante.nombre, materia, f"{nota:.2f}", periodo, tipo, 
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
                    estudiante.nombre, nota['materia'], f"{nota['nota']:.2f}", 
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
            
            messagebox.showinfo("Promedio", f"Promedio general del estudiante: {promedio:.2f}")
            
        except ValueError as e:
            messagebox.showerror("Error", f"Error al calcular promedio: {e}")

    def limpiar_campos_notas(self):
        self.entry_materia_nota.delete(0, tk.END)
        self.entry_nota.delete(0, tk.END)

    # Métodos para asistencias
    def actualizar_combo_estudiantes_asistencias(self):
        estudiantes = self.gestor.obtener_todos()
        self.combo_estudiantes_asistencias['values'] = [f"{e.id} - {e.nombre}" for e in estudiantes]

    def registrar_asistencia(self):
        try:
            estudiante_text = self.combo_estudiantes_asistencias.get()
            materia = self.entry_materia_asistencia.get().strip()
            fecha = self.entry_fecha_asistencia.get().strip()
            estado = self.combo_estado_asistencia.get()

            if not all([estudiante_text, materia, fecha, estado]):
                raise ValueError("Todos los campos son obligatorios")

            id_estudiante = int(estudiante_text.split(' - ')[0])
            self.control_asistencias.registrar_asistencia(id_estudiante, materia, fecha, estado)

            estudiante = next(e for e in self.gestor.obtener_todos() if e.id == id_estudiante)
            self.tree_asistencias.insert("", "end", values=(
                estudiante.nombre, materia, fecha, estado, 
                datetime.now().strftime("%Y-%m-%d %H:%M")
            ))

            messagebox.showinfo("Éxito", "Asistencia registrada correctamente")
            self.limpiar_campos_asistencias()

        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def cargar_asistencias_estudiante(self):
        try:
            estudiante_text = self.combo_estudiantes_asistencias.get()
            if not estudiante_text:
                raise ValueError("Seleccione un estudiante")
            
            id_estudiante = int(estudiante_text.split(' - ')[0])
            asistencias = self.control_asistencias.obtener_asistencias_estudiante(id_estudiante)
            
            self.tree_asistencias.delete(*self.tree_asistencias.get_children())
            estudiante = next(e for e in self.gestor.obtener_todos() if e.id == id_estudiante)
            
            for asistencia in asistencias:
                # Extraer materia de la clave si es necesario
                materia = asistencia.get('materia', 'N/A')
                if 'materia' not in asistencia:
                    # Intentar extraer de la clave si está disponible
                    pass
                    
                self.tree_asistencias.insert("", "end", values=(
                    estudiante.nombre, materia, asistencia['fecha'], 
                    asistencia['estado'], asistencia['fecha_registro']
                ))
                
        except ValueError as e:
            messagebox.showerror("Error", f"Error al cargar asistencias: {e}")

    def generar_reporte_mensual(self):
        try:
            estudiante_text = self.combo_estudiantes_asistencias.get()
            if not estudiante_text:
                raise ValueError("Seleccione un estudiante")
            
            id_estudiante = int(estudiante_text.split(' - ')[0])
            año_actual = datetime.now().year
            mes_actual = datetime.now().month

            reporte = self.control_asistencias.generar_reporte_mensual(id_estudiante, año_actual, mes_actual)
            estudiante = next(e for e in self.gestor.obtener_todos() if e.id == id_estudiante)
            
            messagebox.showinfo("Reporte Mensual", 
                f"Reporte de Asistencia - {estudiante.nombre}\n"
                f"Mes: {mes_actual}/{año_actual}\n\n"
                f"Total de clases: {reporte['total_clases']}\n"
                f"Presentes: {reporte['presentes']}\n"
                f"Tardanzas: {reporte['tardanzas']}\n"
                f"Ausentes: {reporte['ausentes']}\n"
                f"Justificados: {reporte['justificados']}\n"
                f"Porcentaje de asistencia: {reporte['porcentaje_asistencia']:.2f}%")
            
        except ValueError as e:
            messagebox.showerror("Error", f"Error al generar reporte: {e}")

    def limpiar_campos_asistencias(self):
        self.entry_materia_asistencia.delete(0, tk.END)

    # Métodos para pagos
    def actualizar_combo_estudiantes_pagos(self):
        estudiantes = self.gestor.obtener_todos()
        self.combo_estudiantes_pagos['values'] = [f"{e.id} - {e.nombre}" for e in estudiantes]

    def registrar_pago(self):
        try:
            estudiante_text = self.combo_estudiantes_pagos.get()
            monto = float(self.entry_monto_pago.get().strip())
            mes = int(self.combo_mes_pago.get())
            año = int(self.entry_año_pago.get().strip())
            metodo = self.combo_metodo_pago.get()

            if not estudiante_text:
                raise ValueError("Seleccione un estudiante")

            id_estudiante = int(estudiante_text.split(' - ')[0])
            self.sistema_pagos.registrar_pago(id_estudiante, monto, mes, año, metodo)

            estudiante = next(e for e in self.gestor.obtener_todos() if e.id == id_estudiante)
            self.tree_pagos.insert("", "end", values=(
                estudiante.nombre, f"${monto:.2f}", mes, año, metodo, 
                datetime.now().strftime("%Y-%m-%d")
            ))

            messagebox.showinfo("Éxito", "Pago registrado correctamente")
            self.limpiar_campos_pagos()

        except ValueError as e:
            messagebox.showerror("Error", f"Datos inválidos: {e}")

    def cargar_pagos_estudiante(self):
        try:
            estudiante_text = self.combo_estudiantes_pagos.get()
            if not estudiante_text:
                raise ValueError("Seleccione un estudiante")
            
            id_estudiante = int(estudiante_text.split(' - ')[0])
            pagos = self.sistema_pagos.obtener_pagos_estudiante(id_estudiante)
            
            self.tree_pagos.delete(*self.tree_pagos.get_children())
            estudiante = next(e for e in self.gestor.obtener_todos() if e.id == id_estudiante)
            
            for pago in pagos:
                self.tree_pagos.insert("", "end", values=(
                    estudiante.nombre, f"${pago['monto']:.2f}", pago['mes'], pago['año'], 
                    pago['metodo_pago'], pago['fecha_pago'].split(' ')[0]
                ))
                
        except ValueError as e:
            messagebox.showerror("Error", f"Error al cargar pagos: {e}")

    def calcular_deuda(self):
        try:
            estudiante_text = self.combo_estudiantes_pagos.get()
            if not estudiante_text:
                raise ValueError("Seleccione un estudiante")
            
            id_estudiante = int(estudiante_text.split(' - ')[0])
            mensualidad = self.sistema_pagos.calcular_mensualidad(id_estudiante)
            deuda = self.sistema_pagos.calcular_deuda_actual(id_estudiante)

            self.label_mensualidad.config(text=f"${mensualidad:.2f}")
            self.label_deuda.config(text=f"${deuda:.2f}")
            
        except ValueError as e:
            messagebox.showerror("Error", f"Error al calcular deuda: {e}")

    def generar_estado_cuenta(self):
        try:
            estudiante_text = self.combo_estudiantes_pagos.get()
            if not estudiante_text:
                raise ValueError("Seleccione un estudiante")
            
            id_estudiante = int(estudiante_text.split(' - ')[0])
            estado_cuenta = self.sistema_pagos.generar_estado_cuenta(id_estudiante)
            estudiante = next(e for e in self.gestor.obtener_todos() if e.id == id_estudiante)

            messagebox.showinfo("Estado de Cuenta", 
                f"Estado de Cuenta - {estudiante.nombre}\n\n"
                f"Mensualidad actual: Q{estado_cuenta['mensualidad_actual']:.2f}\n"
                f"Total pagado: Q{estado_cuenta['total_pagado']:.2f}\n"
                f"Deuda actual: Q{estado_cuenta['deuda_actual']:.2f}\n"
                f"Pagos registrados: {estado_cuenta['pagos_registrados']}\n"
                f"Próximo vencimiento: {estado_cuenta['proximo_vencimiento']}")
            
        except ValueError as e:
            messagebox.showerror("Error", f"Error al generar estado de cuenta: {e}")

    def limpiar_campos_pagos(self):
        self.entry_monto_pago.delete(0, tk.END)