
# Instrucciones

1. Clonar este repositorio
2. Realizar su aportación/cambios correspondientes
3. Ejecutar el archivo main.py (esto funcionará hasta que todas las estrategías estén implementadas)
4. Crear rama personal de git con el comando: git checkout -b myNombre
5. Realizar un pull request

# Demostración de uso


# Manual de usuario

Este proyecto simula cómo un sistema operativo gestiona varios procesos usando distintos algoritmos de planificación:

* FCFS (First Come, First Served) → El primero que llega es el primero en ejecutarse.

* SJF (Shortest Job First) → El proceso con menor tiempo requerido se ejecuta primero.

* SRTF (Shortest Remaining Time First) → Variante expropiativa de SJF, siempre se ejecuta el que tenga menos tiempo restante.

* Round Robin → Cada proceso obtiene un turno de CPU con duración igual al quantum. Cuando se le acaba, si aún no terminó, vuelve a la cola.

El programa automatiza el trabajo del planificador: recibe procesos como entrada, aplica el algoritmo elegido y  muestra cómo se van ejecutando hasta que todos terminan.

## ¿Cómo interpretar la interfaz gráfica (UI)?

### Formulario de entrada (Nombre, Tiempo CPU, Llegada, Quantum)

Aquí se define los procesos:

* Nombre: identificador que eliges (ej. “P1”).

* Tiempo CPU: cuántas unidades de tiempo necesita.

* Llegada: en qué instante “entra” al sistema.

* Quantum: solo relevante si se usa Round Robin.

### Tabla de procesos

Lista todos los procesos que agregaste, mostrando su PID, nombre, tiempo, llegada y quantum.

### Selector de Algoritmo

Permite elegir qué estrategia de planificación aplicar.

### Botón “Iniciar Simulación”
Lanza la simulación en tiempo real. Cada unidad de tiempo equivale a 5 segundos reales, por lo que verás la ejecución avanzar poco a poco.

### Cola de procesos
Muestra qué procesos están esperando en la cola listos para ejecutarse (ordenados según el algoritmo).

### Historial
Registra los procesos que ya terminaron, indicando el instante en el que finalizaron.

## ¿Cómo interpretar los resultados?

* Si se elige FCFS, la cola se respeta según el orden de llegada.

* Si se elige SJF, los procesos cortos terminan antes que los largos.

* Si se elige SRTF, un proceso corto puede interrumpir a otro más largo en ejecución.

* Si se elige Round Robin, los procesos se “reparten” la CPU en turnos.

### Capturas:

![Captura de pantalla (150).png](../../Pictures/Screenshots/Captura%20de%20pantalla%20%28150%29.png)
