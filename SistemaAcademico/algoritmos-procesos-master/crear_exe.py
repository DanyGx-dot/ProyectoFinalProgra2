"""
Script simple para crear el ejecutable del Sistema Académico
"""
import os
import subprocess
import sys

def main():
    print("🔨 Creando ejecutable del Sistema Académico...")
    print("Esto puede tomar varios minutos...")
    
    # Comando para crear el ejecutable
    comando = [
        'pyinstaller',
        '--onefile',           # Un solo archivo .exe
        '--windowed',          # Sin ventana de consola
        '--name=SistemaAcademico',
        '--icon=NONE',         # Sin icono (puedes cambiar esto después)
        'main_completo.py'
    ]
    
    try:
        # Ejecutar PyInstaller
        subprocess.run(comando, check=True)
        print("✅ ¡Ejecutable creado exitosamente!")
        
        # Copiar archivos JSON a la carpeta dist
        archivos_json = ['estudiantes.json', 'notas.json', 'asistencias.json', 'pagos.json']
        for archivo in archivos_json:
            if os.path.exists(archivo):
                import shutil
                shutil.copy2(archivo, 'dist')
                print(f"✅ Copiado: {archivo}")
        
        print("\n🎉 ¡Proceso completado!")
        print("📍 El ejecutable está en la carpeta 'dist'")
        print("\n📋 Siguientes pasos:")
        print("1. Ve a la carpeta 'dist'")
        print("2. Encuentra 'SistemaAcademico.exe'")
        print("3. Arrástralo a tu escritorio")
        print("4. ¡Listo! Haz doble clic para ejecutar")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Soluciones posibles:")
        print("- Asegúrate de que todos los archivos .py estén en la misma carpeta")
        print("- Verifica que PyInstaller esté instalado: pip install pyinstaller")
        print("- Ejecuta como administrador si hay problemas de permisos")

if __name__ == "__main__":
    main()