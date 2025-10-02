"""
Script para construir el ejecutable del Sistema Académico
"""
import os
import sys
import shutil
import subprocess

def crear_archivos_necesarios():
    """Crear archivos JSON vacíos si no existen"""
    archivos_json = ['estudiantes.json', 'notas.json', 'asistencias.json', 'pagos.json']
    
    for archivo in archivos_json:
        if not os.path.exists(archivo):
            with open(archivo, 'w', encoding='utf-8') as f:
                f.write('{}')
            print(f"✅ Creado: {archivo}")

def limpiar_directorios_previos():
    """Limpiar builds anteriores"""
    directorios = ['build', 'dist']
    
    for directorio in directorios:
        if os.path.exists(directorio):
            shutil.rmtree(directorio)
            print(f"🧹 Limpiado: {directorio}")

def construir_ejecutable():
    """Construir el ejecutable usando PyInstaller"""
    print("🚀 Construyendo ejecutable...")
    
    # Opción 1: Usar el archivo .spec
    comando = ['pyinstaller', 'build.spec', '--clean']
    
    # Opción 2: Usar línea de comandos directamente (descomenta si prefieres)
    # comando = [
    #     'pyinstaller',
    #     '--name=SistemaAcademico',
    #     '--onefile',
    #     '--windowed',
    #     '--add-data=estudiantes.json;.',
    #     '--add-data=notas.json;.',
    #     '--add-data=asistencias.json;.',
    #     '--add-data=pagos.json;.',
    #     '--icon=icon.ico',  # Opcional
    #     'main_completo.py'
    # ]
    
    try:
        resultado = subprocess.run(comando, check=True, capture_output=True, text=True)
        print("✅ Ejecutable construido exitosamente!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al construir el ejecutable: {e}")
        print(f"Salida de error: {e.stderr}")
        return False

def verificar_archivos_resultantes():
    """Verificar que los archivos necesarios se crearon correctamente"""
    ejecutable = os.path.join('dist', 'SistemaAcademico.exe')
    
    if os.path.exists(ejecutable):
        print(f"✅ Ejecutable creado: {ejecutable}")
        tamaño = os.path.getsize(ejecutable) / (1024 * 1024)  # Tamaño en MB
        print(f"📏 Tamaño del ejecutable: {tamaño:.2f} MB")
        return True
    else:
        print("❌ No se pudo encontrar el ejecutable")
        return False

def copiar_archivos_datos():
    """Copiar archivos de datos a la carpeta dist"""
    archivos_json = ['estudiantes.json', 'notas.json', 'asistencias.json', 'pagos.json']
    destino = 'dist'
    
    for archivo in archivos_json:
        if os.path.exists(archivo):
            shutil.copy2(archivo, destino)
            print(f"✅ Copiado: {archivo} -> {destino}")

def main():
    """Función principal"""
    print("🔨 Iniciando construcción del Sistema Académico...")
    print("=" * 50)
    
    # 1. Crear archivos necesarios
    crear_archivos_necesarios()
    
    # 2. Limpiar builds anteriores
    limpiar_directorios_previos()
    
    # 3. Construir ejecutable
    if construir_ejecutable():
        # 4. Verificar resultado
        if verificar_archivos_resultantes():
            # 5. Copiar archivos de datos
            copiar_archivos_datos()
            print("\n🎉 ¡Construcción completada!")
            print("📍 El ejecutable está en la carpeta 'dist'")
        else:
            print("\n❌ La construcción falló al verificar los archivos")
    else:
        print("\n❌ La construcción falló")

if __name__ == "__main__":
    main()