import tkinter as tk
from tkinter import ttk, messagebox
from GestorEstudiantes import GestorEstudiantes
from SistemaNotas import SistemaNotas
from ControlAsistencias import ControlAsistencias
from SistemaPagos import SistemaPagos
from datetime import datetime

class AppCompleta:
    """
    Clase principal que representa la aplicación completa del Sistema Académico Integral.
    Esta clase gestiona la interfaz gráfica y coordina todos los módulos del sistema.
    """
    
    def __init__(self, root):
        """
        Constructor de la clase AppCompleta.
        
        Args:
            root: Ventana principal de Tkinter
        """
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Sistema Académico Integral - Universidad")
        self.root.geometry("1200x700")
        
        # Configurar icono (opcional)
        try:
            self.root.iconbitmap("icon.ico")  # Si tienes un icono
        except:
            pass
        
        # Paleta de colores moderna y profesional
        self.colors = {
            'primary': '#2C3E50',        # Azul oscuro elegante
            'secondary': '#3498DB',      # Azul brillante
            'accent': '#E74C3C',         # Rojo coral para énfasis
            'success': '#27AE60',        # Verde para acciones positivas
            'warning': '#F39C12',        # Naranja para advertencias
            'light_bg': "#EFF1EC",       # Fondo claro
            'dark_bg': '#34495E',        # Fondo oscuro para headers
            'text_light': '#FFFFFF',     # Texto claro
            'text_dark': '#2C3E50',      # Texto oscuro
            'card_bg': '#FFFFFF',        # Fondo de tarjetas
            'border': '#BDC3C7',         # Color de bordes
            'hover': '#2980B9'           # Color hover para botones
        }
        
        self.root.configure(bg=self.colors['light_bg'])

        # Inicialización de los gestores de cada módulo
        self.gestor = GestorEstudiantes()  # Gestor de estudiantes
        self.sistema_notas = SistemaNotas(self.gestor)  # Sistema de notas
        self.control_asistencias = ControlAsistencias(self.gestor)  # Control de asistencias
        self.sistema_pagos = SistemaPagos(self.gestor)  # Sistema de pagos

        # Configuración del estilo visual
        self._configurar_estilo()

        # Creación de la interfaz gráfica
        self._crear_interfaz()

    def _configurar_estilo(self):
        """
        Configura el estilo visual de los componentes de Tkinter.
        Define colores, fuentes y apariencia de los widgets con una paleta moderna.
        """
        style = ttk.Style()
        style.theme_use('clam')  # Tema base que permite personalización
        
        # Configurar fuentes
        font_normal = ('Segoe UI', 10)
        font_bold = ('Segoe UI', 10, 'bold')
        font_title = ('Segoe UI', 12, 'bold')
        
        # Configuración general de estilos
        style.configure('.', 
                       background=self.colors['light_bg'],
                       foreground=self.colors['text_dark'],
                       font=font_normal)
        
        # Configurar Notebook (pestañas)
        style.configure('TNotebook', background=self.colors['light_bg'])
        style.configure('TNotebook.Tab', 
                       background=self.colors['primary'],
                       foreground=self.colors['text_light'],
                       padding=[15, 5],
                       font=font_bold)
        style.map('TNotebook.Tab', 
                 background=[('selected', self.colors['secondary'])],
                 foreground=[('selected', self.colors['text_light'])])
        
        # Configurar Frames
        style.configure('TFrame', 
                       background=self.colors['light_bg'])
        
        # Configurar Labels
        style.configure('TLabel',
                       background=self.colors['light_bg'],
                       foreground=self.colors['text_dark'],
                       font=font_normal)
        
        # Configurar LabelFrame
        style.configure('TLabelframe',
                       background=self.colors['light_bg'],
                       foreground=self.colors['primary'],
                       bordercolor=self.colors['border'],
                       relief='solid',
                       borderwidth=1)
        style.configure('TLabelframe.Label',
                       background=self.colors['light_bg'],
                       foreground=self.colors['primary'],
                       font=font_title)
        
        # Configurar Botones
        style.configure('TButton',
                       background=self.colors['secondary'],
                       foreground=self.colors['text_light'],
                       borderwidth=1,
                       focusthickness=3,
                       focuscolor=self.colors['secondary'],
                       font=font_bold,
                       padding=[10, 5])
        style.map('TButton',
                 background=[('active', self.colors['hover']),
                           ('pressed', self.colors['primary'])],
                 foreground=[('active', self.colors['text_light']),
                           ('pressed', self.colors['text_light'])])
        
        # Botones de éxito (verde)
        style.configure('Success.TButton',
                       background=self.colors['success'],
                       foreground=self.colors['text_light'])
        style.map('Success.TButton',
                 background=[('active', '#219955'),
                           ('pressed', '#1e8449')])
        
        # Botones de advertencia (naranja)
        style.configure('Warning.TButton',
                       background=self.colors['warning'],
                       foreground=self.colors['text_light'])
        style.map('Warning.TButton',
                 background=[('active', '#e67e22'),
                           ('pressed', '#d35400')])
        
        # Botones de peligro (rojo)
        style.configure('Danger.TButton',
                       background=self.colors['accent'],
                       foreground=self.colors['text_light'])
        style.map('Danger.TButton',
                 background=[('active', '#c0392b'),
                           ('pressed', '#a93226')])
        
        # Configurar Entradas
        style.configure('TEntry',
                       fieldbackground=self.colors['card_bg'],
                       foreground=self.colors['text_dark'],
                       borderwidth=1,
                       relief='solid',
                       padding=[5, 2])
        style.map('TEntry',
                 fieldbackground=[('focus', self.colors['card_bg']),
                                ('disabled', self.colors['light_bg'])])
        
        # Configurar Combobox
        style.configure('TCombobox',
                       fieldbackground=self.colors['card_bg'],
                       background=self.colors['card_bg'],
                       foreground=self.colors['text_dark'],
                       borderwidth=1,
                       relief='solid')
        style.map('TCombobox',
                 fieldbackground=[('focus', self.colors['card_bg']),
                                ('readonly', self.colors['card_bg'])],
                 background=[('readonly', self.colors['card_bg'])])
        
        # Configurar Treeview
        style.configure('Treeview',
                       background=self.colors['card_bg'],
                       foreground=self.colors['text_dark'],
                       fieldbackground=self.colors['card_bg'],
                       borderwidth=1,
                       relief='solid',
                       rowheight=25)
        style.configure('Treeview.Heading',
                       background=self.colors['primary'],
                       foreground=self.colors['text_light'],
                       relief='flat',
                       font=font_bold)
        style.map('Treeview.Heading',
                 background=[('active', self.colors['secondary'])])
        style.map('Treeview',
                 background=[('selected', self.colors['secondary'])],
                 foreground=[('selected', self.colors['text_light'])])
        
        # Configurar Scrollbar
        style.configure('TScrollbar',
                       background=self.colors['primary'],
                       troughcolor=self.colors['light_bg'],
                       borderwidth=0,
                       relief='flat')
        style.map('TScrollbar',
                 background=[('active', self.colors['secondary'])])
        
        # Configurar Progressbar
        style.configure('TProgressbar',
                       background=self.colors['success'],
                       troughcolor=self.colors['light_bg'],
                       borderwidth=0)

    def _crear_interfaz(self):
        """
        Crea la interfaz gráfica principal con pestañas para cada módulo.
        Utiliza un Notebook (pestañas) para organizar las diferentes secciones.
        """
        # Crear header con logo y título
        self._crear_header()
        
        # Crear el widget de pestañas
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=15, pady=10)

        # Crear frames para cada pestaña
        self.frame_estudiantes = ttk.Frame(notebook)
        self.frame_notas = ttk.Frame(notebook)
        self.frame_asistencias = ttk.Frame(notebook)
        self.frame_pagos = ttk.Frame(notebook)

        # Agregar las pestañas al notebook
        notebook.add(self.frame_estudiantes, text="🎓 Gestión de Estudiantes")
        notebook.add(self.frame_notas, text="📊 Sistema de Notas")
        notebook.add(self.frame_asistencias, text="📅 Control de Asistencias")
        notebook.add(self.frame_pagos, text="💰 Pagos de Colegiatura")

        # Crear las interfaces de cada módulo
        self._crear_interfaz_estudiantes()
        self._crear_interfaz_notas()
        self._crear_interfaz_asistencias()
        self._crear_interfaz_pagos()

    def _crear_header(self):
        """
        Crea el encabezado de la aplicación con logo y título.
        """
        header_frame = tk.Frame(self.root, bg=self.colors['primary'], height=80)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)  # Evita que el frame se ajuste al contenido
        
        # Título de la aplicación
        title_label = tk.Label(header_frame, 
                              text="Sistema Académico Integral - Universidad",
                              font=('Segoe UI', 20, 'bold'),
                              bg=self.colors['primary'],
                              fg=self.colors['text_light'],
                              pady=20)
        title_label.pack(side="left", padx=20)
        
        # Información de usuario/sistema (puedes personalizar esto)
        user_info = tk.Label(header_frame,
                            text=f"Usuario: Admin | {datetime.now().strftime('%d/%m/%Y')}",
                            font=('Segoe UI', 10),
                            bg=self.colors['primary'],
                            fg=self.colors['text_light'])
        user_info.pack(side="right", padx=20)

    def _crear_interfaz_estudiantes(self):
        """
        Crea la interfaz para el módulo de Gestión de Estudiantes.
        Incluye formularios para registrar, buscar, modificar y eliminar estudiantes.
        """
        # Frame principal para estudiantes
        main_frame = ttk.Frame(self.frame_estudiantes)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título del módulo con icono
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill="x", pady=(0, 20))
        
        ttk.Label(title_frame, 
                 text="🎓 Gestión de Estudiantes", 
                 font=('Segoe UI', 18, 'bold'),
                 foreground=self.colors['primary']).pack()

        # Contenedor principal con dos columnas
        container = ttk.Frame(main_frame)
        container.pack(fill="both", expand=True)
        
        # Columna izquierda - Registro
        left_frame = ttk.LabelFrame(container, text="📝 Registrar Nuevo Estudiante")
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        # Columna derecha - Búsqueda y lista
        right_frame = ttk.LabelFrame(container, text="🔍 Buscar y Gestionar Estudiantes")
        right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # ========== FORMULARIO DE REGISTRO ==========
        form_frame = ttk.Frame(left_frame)
        form_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Campos del formulario en una grid organizada
        fields = [
            ("Nombre completo:", "nombre_entry", None),
            ("Edad:", "edad_entry", None),
            ("Carrera:", "carrera_combobox", [
                "Ingeniería de Sistemas", "Medicina", "Derecho", "Administración", 
                "Contaduría", "Psicología", "Ingeniería Civil", "Arquitectura"
            ]),
            ("Promedio:", "promedio_entry", None),
            ("Semestre:", "semestre_combobox", [str(i) for i in range(1, 11)]),
            ("Email:", "email_entry", None)
        ]
        
        for i, (label_text, attr_name, values) in enumerate(fields):
            ttk.Label(form_frame, text=label_text, font=('Segoe UI', 9, 'bold')).grid(
                row=i, column=0, sticky="w", pady=8, padx=(0, 10))
            
            if values:  # Combobox
                widget = ttk.Combobox(form_frame, values=values, width=25)
                setattr(self, attr_name, widget)
            else:  # Entry
                widget = ttk.Entry(form_frame, width=28)
                setattr(self, attr_name, widget)
                
            widget.grid(row=i, column=1, sticky="ew", pady=8, padx=(0, 10))
        
        # Botón para registrar estudiante
        ttk.Button(form_frame, 
                  text="➕ Registrar Estudiante", 
                  command=self.registrar_estudiante,
                  style='Success.TButton').grid(
                    row=len(fields), column=0, columnspan=2, pady=20, sticky="ew")

        # ========== BÚSQUEDA Y GESTIÓN ==========
        search_frame = ttk.Frame(right_frame)
        search_frame.pack(fill="x", padx=15, pady=15)
        
        # Fila de búsqueda
        ttk.Label(search_frame, text="Buscar por:").grid(row=0, column=0, sticky="w", padx=(0, 5))
        self.criterio_busqueda = ttk.Combobox(search_frame, values=["Nombre", "Carrera", "Email", "ID"], width=10)
        self.criterio_busqueda.current(0)
        self.criterio_busqueda.grid(row=0, column=1, padx=5)
        
        self.valor_busqueda = ttk.Entry(search_frame, width=20)
        self.valor_busqueda.grid(row=0, column=2, padx=5)
        
        ttk.Button(search_frame, 
                  text="🔍 Buscar", 
                  command=self.buscar_estudiantes).grid(row=0, column=3, padx=5)

        # Tabla de estudiantes
        table_frame = ttk.Frame(right_frame)
        table_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        
        # Treeview con scrollbar
        self.tree_estudiantes = ttk.Treeview(table_frame, 
                                           columns=("ID", "Nombre", "Edad", "Carrera", "Promedio", "Semestre", "Email"), 
                                           show="headings", 
                                           height=12)
        
        # Configurar columnas
        columns = {
            "ID": 80, "Nombre": 150, "Edad": 60, "Carrera": 120, 
            "Promedio": 80, "Semestre": 80, "Email": 150
        }
        
        for col, width in columns.items():
            self.tree_estudiantes.heading(col, text=col)
            self.tree_estudiantes.column(col, width=width, anchor="center")
        
        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree_estudiantes.yview)
        self.tree_estudiantes.configure(yscrollcommand=scrollbar.set)
        
        self.tree_estudiantes.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Botones de acción
        action_frame = ttk.Frame(right_frame)
        action_frame.pack(fill="x", padx=15, pady=10)
        
        ttk.Button(action_frame, 
                  text="📋 Mostrar Todos", 
                  command=self.mostrar_todos_estudiantes).pack(side="left", padx=5)
        
        ttk.Button(action_frame, 
                  text="✏️ Modificar", 
                  command=self.modificar_estudiante).pack(side="left", padx=5)
        
        ttk.Button(action_frame, 
                  text="🗑️ Eliminar", 
                  command=self.eliminar_estudiante,
                  style='Danger.TButton').pack(side="left", padx=5)

        # Mostrar todos los estudiantes al iniciar
        self.mostrar_todos_estudiantes()

    def _crear_interfaz_notas(self):
        """
        Crea la interfaz para el módulo de Sistema de Notas.
        Permite registrar calificaciones y ver el historial académico.
        """
        # Frame principal para notas
        main_frame = ttk.Frame(self.frame_notas)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título del módulo
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill="x", pady=(0, 20))
        
        ttk.Label(title_frame, 
                 text="📊 Sistema de Gestión de Notas", 
                 font=('Segoe UI', 18, 'bold'),
                 foreground=self.colors['primary']).pack()

        # Contenedor principal con dos secciones
        container = ttk.Frame(main_frame)
        container.pack(fill="both", expand=True)
        
        # Sección izquierda - Registro de notas
        left_frame = ttk.LabelFrame(container, text="➕ Agregar Nueva Nota")
        left_frame.pack(side="left", fill="both", padx=(0, 10))
        
        # Sección derecha - Historial de notas
        right_frame = ttk.LabelFrame(container, text="📋 Historial de Notas")
        right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # ========== FORMULARIO DE NOTAS ==========
        form_frame = ttk.Frame(left_frame)
        form_frame.pack(fill="both", padx=15, pady=15)
        
        # Campos del formulario
        fields = [
            ("Estudiante:", "combo_estudiantes_notas", None),
            ("Materia:", "entry_materia_nota", None),
            ("Nota (0-10):", "entry_nota", None),
            ("Periodo:", "combo_periodo", ["2024-1", "2024-2", "2025-1", "2025-2"]),
            ("Tipo:", "combo_tipo_nota", ["Parcial", "Quiz", "Proyecto", "Final"])
        ]
        
        for i, (label_text, attr_name, values) in enumerate(fields):
            ttk.Label(form_frame, text=label_text, font=('Segoe UI', 9, 'bold')).grid(
                row=i, column=0, sticky="w", pady=8, padx=(0, 10))
            
            if values:
                widget = ttk.Combobox(form_frame, values=values, width=20)
                if values[0]:  # Establecer valor por defecto
                    widget.set(values[0])
                setattr(self, attr_name, widget)
            else:
                widget = ttk.Entry(form_frame, width=23)
                setattr(self, attr_name, widget)
                
            widget.grid(row=i, column=1, sticky="ew", pady=8)
        
        # Botones de acción
        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=len(fields), column=0, columnspan=2, pady=20, sticky="ew")
        
        ttk.Button(button_frame, 
                  text="💾 Agregar Nota", 
                  command=self.agregar_nota,
                  style='Success.TButton').pack(side="left", padx=5)
        
        ttk.Button(button_frame, 
                  text="🧹 Limpiar", 
                  command=self.limpiar_campos_notas).pack(side="left", padx=5)

        # ========== HISTORIAL DE NOTAS ==========
        table_frame = ttk.Frame(right_frame)
        table_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Treeview para notas
        self.tree_notas = ttk.Treeview(table_frame, 
                                     columns=("Estudiante", "Materia", "Nota", "Periodo", "Tipo", "Fecha"), 
                                     show="headings", 
                                     height=15)
        
        # Configurar columnas
        columns = {
            "Estudiante": 120, "Materia": 120, "Nota": 80, 
            "Periodo": 80, "Tipo": 100, "Fecha": 100
        }
        
        for col, width in columns.items():
            self.tree_notas.heading(col, text=col)
            self.tree_notas.column(col, width=width, anchor="center")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree_notas.yview)
        self.tree_notas.configure(yscrollcommand=scrollbar.set)
        
        self.tree_notas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Botones adicionales
        action_frame = ttk.Frame(right_frame)
        action_frame.pack(fill="x", padx=15, pady=10)
        
        ttk.Button(action_frame, 
                  text="📥 Cargar Notas", 
                  command=self.cargar_notas_estudiante).pack(side="left", padx=5)
        
        ttk.Button(action_frame, 
                  text="📈 Calcular Promedio", 
                  command=self.calcular_promedio,
                  style='Success.TButton').pack(side="left", padx=5)

        # Actualizar combobox con estudiantes
        self.actualizar_combo_estudiantes_notas()

    def _crear_interfaz_asistencias(self):
        """
        Crea la interfaz para el módulo de Control de Asistencias.
        Permite registrar asistencias y generar reportes.
        """
        # Frame principal para asistencias
        main_frame = ttk.Frame(self.frame_asistencias)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título del módulo
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill="x", pady=(0, 20))
        
        ttk.Label(title_frame, 
                 text="📅 Control de Asistencias", 
                 font=('Segoe UI', 18, 'bold'),
                 foreground=self.colors['primary']).pack()

        # Contenedor principal
        container = ttk.Frame(main_frame)
        container.pack(fill="both", expand=True)
        
        # Sección izquierda - Registro
        left_frame = ttk.LabelFrame(container, text="✅ Registrar Asistencia")
        left_frame.pack(side="left", fill="both", padx=(0, 10))
        
        # Sección derecha - Historial
        right_frame = ttk.LabelFrame(container, text="📋 Historial de Asistencias")
        right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # ========== FORMULARIO DE ASISTENCIAS ==========
        form_frame = ttk.Frame(left_frame)
        form_frame.pack(fill="both", padx=15, pady=15)
        
        # Campos del formulario
        fields = [
            ("Estudiante:", "combo_estudiantes_asistencias", None),
            ("Materia:", "entry_materia_asistencia", None),
            ("Fecha:", "entry_fecha_asistencia", None),
            ("Estado:", "combo_estado_asistencia", ["Presente", "Ausente", "Tardanza", "Justificado"])
        ]
        
        for i, (label_text, attr_name, values) in enumerate(fields):
            ttk.Label(form_frame, text=label_text, font=('Segoe UI', 9, 'bold')).grid(
                row=i, column=0, sticky="w", pady=10, padx=(0, 10))
            
            if values:
                widget = ttk.Combobox(form_frame, values=values, width=20)
                widget.set(values[0])  # Valor por defecto
                setattr(self, attr_name, widget)
            else:
                widget = ttk.Entry(form_frame, width=23)
                if label_text == "Fecha:":
                    widget.insert(0, datetime.now().strftime("%Y-%m-%d"))
                setattr(self, attr_name, widget)
                
            widget.grid(row=i, column=1, sticky="ew", pady=10)
        
        # Botón de registro
        ttk.Button(form_frame, 
                  text="✅ Registrar Asistencia", 
                  command=self.registrar_asistencia,
                  style='Success.TButton').grid(
                    row=len(fields), column=0, columnspan=2, pady=20, sticky="ew")

        # ========== HISTORIAL DE ASISTENCIAS ==========
        table_frame = ttk.Frame(right_frame)
        table_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Treeview para asistencias
        self.tree_asistencias = ttk.Treeview(table_frame, 
                                           columns=("Estudiante", "Materia", "Fecha", "Estado", "Registro"), 
                                           show="headings", 
                                           height=15)
        
        # Configurar columnas
        columns = {
            "Estudiante": 120, "Materia": 120, "Fecha": 100, 
            "Estado": 100, "Registro": 120
        }
        
        for col, width in columns.items():
            self.tree_asistencias.heading(col, text=col)
            self.tree_asistencias.column(col, width=width, anchor="center")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree_asistencias.yview)
        self.tree_asistencias.configure(yscrollcommand=scrollbar.set)
        
        self.tree_asistencias.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Botones de acción
        action_frame = ttk.Frame(right_frame)
        action_frame.pack(fill="x", padx=15, pady=10)
        
        ttk.Button(action_frame, 
                  text="📥 Cargar Asistencias", 
                  command=self.cargar_asistencias_estudiante).pack(side="left", padx=5)
        
        ttk.Button(action_frame, 
                  text="📊 Generar Reporte", 
                  command=self.generar_reporte_mensual,
                  style='Success.TButton').pack(side="left", padx=5)
        
        ttk.Button(action_frame, 
                  text="🧹 Limpiar", 
                  command=self.limpiar_campos_asistencias).pack(side="left", padx=5)

        # Actualizar combobox con estudiantes
        self.actualizar_combo_estudiantes_asistencias()

    def _crear_interfaz_pagos(self):
        """
        Crea la interfaz para el módulo de Pagos de Colegiatura.
        Permite registrar pagos, calcular deudas y generar estados de cuenta.
        """
        # Frame principal para pagos
        main_frame = ttk.Frame(self.frame_pagos)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título del módulo
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(fill="x", pady=(0, 20))
        
        ttk.Label(title_frame, 
                 text="💰 Sistema de Pagos de Colegiatura", 
                 font=('Segoe UI', 18, 'bold'),
                 foreground=self.colors['primary']).pack()

        # Contenedor principal
        container = ttk.Frame(main_frame)
        container.pack(fill="both", expand=True)
        
        # Sección izquierda - Registro e información
        left_frame = ttk.LabelFrame(container, text="💳 Registrar Pago")
        left_frame.pack(side="left", fill="both", padx=(0, 10))
        
        # Sección derecha - Historial
        right_frame = ttk.LabelFrame(container, text="📋 Historial de Pagos")
        right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # ========== FORMULARIO DE PAGOS ==========
        form_frame = ttk.Frame(left_frame)
        form_frame.pack(fill="both", padx=15, pady=15)
        
        # Campos del formulario
        fields = [
            ("Estudiante:", "combo_estudiantes_pagos", None),
            ("Monto ($):", "entry_monto_pago", None),
            ("Mes:", "combo_mes_pago", [str(i) for i in range(1, 13)]),
            ("Año:", "entry_año_pago", None),
            ("Método:", "combo_metodo_pago", ["Efectivo", "Tarjeta", "Transferencia"])
        ]
        
        for i, (label_text, attr_name, values) in enumerate(fields):
            ttk.Label(form_frame, text=label_text, font=('Segoe UI', 9, 'bold')).grid(
                row=i, column=0, sticky="w", pady=8, padx=(0, 10))
            
            if values:
                widget = ttk.Combobox(form_frame, values=values, width=20)
                if label_text == "Mes:":
                    widget.set(str(datetime.now().month))
                else:
                    widget.set(values[0])
                setattr(self, attr_name, widget)
            else:
                widget = ttk.Entry(form_frame, width=23)
                if label_text == "Año:":
                    widget.insert(0, str(datetime.now().year))
                setattr(self, attr_name, widget)
                
            widget.grid(row=i, column=1, sticky="ew", pady=8)
        
        # Botón de registro
        ttk.Button(form_frame, 
                  text="💳 Registrar Pago", 
                  command=self.registrar_pago,
                  style='Success.TButton').grid(
                    row=len(fields), column=0, columnspan=2, pady=15, sticky="ew")

        # ========== INFORMACIÓN FINANCIERA ==========
        info_frame = ttk.LabelFrame(left_frame, text="💰 Información Financiera")
        info_frame.pack(fill="x", padx=15, pady=15)
        
        info_content = ttk.Frame(info_frame)
        info_content.pack(fill="x", padx=10, pady=10)
        
        ttk.Label(info_content, text="Mensualidad actual:", font=('Segoe UI', 9, 'bold')).grid(
            row=0, column=0, sticky="w", pady=5)
        self.label_mensualidad = ttk.Label(info_content, text="$0.00", foreground=self.colors['success'])
        self.label_mensualidad.grid(row=0, column=1, sticky="w", pady=5, padx=(10, 20))
        
        ttk.Label(info_content, text="Deuda actual:", font=('Segoe UI', 9, 'bold')).grid(
            row=0, column=2, sticky="w", pady=5)
        self.label_deuda = ttk.Label(info_content, text="$0.00", foreground=self.colors['accent'])
        self.label_deuda.grid(row=0, column=3, sticky="w", pady=5, padx=(10, 0))
        
        ttk.Button(info_content, 
                  text="📊 Calcular Deuda", 
                  command=self.calcular_deuda).grid(
                    row=1, column=0, columnspan=4, pady=10, sticky="ew")

        # ========== HISTORIAL DE PAGOS ==========
        table_frame = ttk.Frame(right_frame)
        table_frame.pack(fill="both", expand=True, padx=15, pady=15)
        
        # Treeview para pagos
        self.tree_pagos = ttk.Treeview(table_frame, 
                                     columns=("Estudiante", "Monto", "Mes", "Año", "Método", "Fecha"), 
                                     show="headings", 
                                     height=15)
        
        # Configurar columnas
        columns = {
            "Estudiante": 120, "Monto": 100, "Mes": 80, 
            "Año": 80, "Método": 100, "Fecha": 100
        }
        
        for col, width in columns.items():
            self.tree_pagos.heading(col, text=col)
            self.tree_pagos.column(col, width=width, anchor="center")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree_pagos.yview)
        self.tree_pagos.configure(yscrollcommand=scrollbar.set)
        
        self.tree_pagos.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Botones de acción
        action_frame = ttk.Frame(right_frame)
        action_frame.pack(fill="x", padx=15, pady=10)
        
        ttk.Button(action_frame, 
                  text="📥 Cargar Pagos", 
                  command=self.cargar_pagos_estudiante).pack(side="left", padx=5)
        
        ttk.Button(action_frame, 
                  text="📄 Estado de Cuenta", 
                  command=self.generar_estado_cuenta,
                  style='Success.TButton').pack(side="left", padx=5)
        
        ttk.Button(action_frame, 
                  text="🧹 Limpiar", 
                  command=self.limpiar_campos_pagos).pack(side="left", padx=5)

        # Actualizar combobox con estudiantes
        self.actualizar_combo_estudiantes_pagos()

    # Los métodos de funcionalidad (registrar_estudiante, buscar_estudiantes, etc.)
    # se mantienen igual que en la versión anterior, solo cambia la interfaz visual
    # [Aquí irían todos los métodos de funcionalidad que ya tenías...]

# Por razones de espacio, solo muestro los cambios en la interfaz visual
# Los métodos de funcionalidad se mantienen igual que en tu versión anterior

# ... [Los métodos de funcionalidad permanecen igual] ...