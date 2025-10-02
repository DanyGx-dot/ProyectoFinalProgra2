from PIL import Image, ImageDraw
import os

def crear_icono_computadora():
    """
    Crea un icono simple de computadora usando PIL
    """
    # Tamaños estándar para iconos (Windows necesita múltiples tamaños)
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    images = []
    
    for size in sizes:
        # Crear imagen con fondo transparente
        img = Image.new('RGBA', size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        width, height = size
        
        # Colores
        color_monitor = (70, 130, 180)  # Azul acero
        color_pantalla = (30, 30, 30)   # Negro para la pantalla
        color_base = (100, 100, 100)    # Gris para la base
        color_boton = (50, 50, 50)      # Gris oscuro para botones
        
        # Escalar las dimensiones según el tamaño del icono
        scale = width / 64.0  # Usamos 64 como base
        
        if width >= 32:  # Para iconos más grandes, dibujar detalles
            # Monitor (rectángulo principal)
            monitor_w = int(40 * scale)
            monitor_h = int(30 * scale)
            monitor_x = (width - monitor_w) // 2
            monitor_y = int(5 * scale)
            
            # Pantalla (interior del monitor)
            pantalla_w = int(36 * scale)
            pantalla_h = int(24 * scale)
            pantalla_x = monitor_x + (monitor_w - pantalla_w) // 2
            pantalla_y = monitor_y + (monitor_h - pantalla_h) // 2
            
            # Base del monitor
            base_w = int(20 * scale)
            base_h = int(8 * scale)
            base_x = (width - base_w) // 2
            base_y = monitor_y + monitor_h
            
            # Soporte
            soporte_w = int(6 * scale)
            soporte_h = int(6 * scale)
            soporte_x = (width - soporte_w) // 2
            soporte_y = base_y + base_h
            
            # Dibujar monitor
            draw.rectangle([monitor_x, monitor_y, monitor_x + monitor_w, monitor_y + monitor_h], 
                          fill=color_monitor, outline=(50, 50, 50), width=int(scale))
            
            # Dibujar pantalla
            draw.rectangle([pantalla_x, pantalla_y, pantalla_x + pantalla_w, pantalla_y + pantalla_h], 
                          fill=color_pantalla)
            
            # Dibujar base
            draw.rectangle([base_x, base_y, base_x + base_w, base_y + base_h], 
                          fill=color_base)
            
            # Dibujar soporte
            draw.rectangle([soporte_x, soporte_y, soporte_x + soporte_w, soporte_y + soporte_h], 
                          fill=color_base)
            
            # Agregar algunos detalles (solo en iconos grandes)
            if width >= 48:
                # Botón de encendido
                boton_size = int(4 * scale)
                boton_x = monitor_x + monitor_w - int(8 * scale)
                boton_y = monitor_y + int(6 * scale)
                draw.ellipse([boton_x, boton_y, boton_x + boton_size, boton_y + boton_size], 
                            fill=color_boton)
                
                # Luz de encendido (punto verde)
                luz_size = int(2 * scale)
                luz_x = boton_x
                luz_y = boton_y + boton_size + int(2 * scale)
                draw.ellipse([luz_x, luz_y, luz_x + luz_size, luz_y + luz_size], 
                            fill=(0, 255, 0))
        
        else:  # Para iconos pequeños, versión simplificada
            monitor_w = int(30 * scale)
            monitor_h = int(20 * scale)
            monitor_x = (width - monitor_w) // 2
            monitor_y = int(3 * scale)
            
            pantalla_w = int(26 * scale)
            pantalla_h = int(14 * scale)
            pantalla_x = monitor_x + (monitor_w - pantalla_w) // 2
            pantalla_y = monitor_y + (monitor_h - pantalla_h) // 2
            
            base_w = int(12 * scale)
            base_h = int(4 * scale)
            base_x = (width - base_w) // 2
            base_y = monitor_y + monitor_h
            
            draw.rectangle([monitor_x, monitor_y, monitor_x + monitor_w, monitor_y + monitor_h], 
                          fill=color_monitor)
            draw.rectangle([pantalla_x, pantalla_y, pantalla_x + pantalla_w, pantalla_y + pantalla_h], 
                          fill=color_pantalla)
            draw.rectangle([base_x, base_y, base_x + base_w, base_y + base_h], 
                          fill=color_base)
        
        images.append(img)
    
    # Guardar como ICO (formato que soporta múltiples tamaños)
    images[0].save('icono_computadora.ico', format='ICO', sizes=[(size[0], size[1]) for size in sizes])
    print("✅ Icono de computadora creado: 'icono_computadora.ico'")

if __name__ == "__main__":
    # Verificar si PIL está instalado
    try:
        crear_icono_computadora()
        print("\n📝 Ahora actualiza tu archivo instalador.iss:")
        print('   SetupIconFile=icono_computadora.ico')
    except ImportError:
        print("❌ Error: Necesitas instalar Pillow")
        print("   Ejecuta: pip install pillow")
        print("\n📦 Como alternativa, usa la Opción 2 para descargar un icono")