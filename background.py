"""
Hecho por Jaisir & Wilson

Librerias:
- SimpleCV
"""

from SimpleCV import *
import time

def backg(images_path, save_path, extension = "*.jpg"):
    init = time.time()
    """ Eliminar el fondo blanco de una imagen

        Keyword arguments:
        images_path -- la carpeta que contiene las imagenes
        save_path -- la carpeta donde se guardaran las imagenes modificadas
        extension -- extension de las imagenes (default: *.jpg)
    """
    directory = os.path.join(images_path, extension)
    files = glob.glob(directory)

    i = 0
    for file in files:
        i += 1
        """Recorrer el directorio"""
        # print(file)
        new_img = Image(file)
        mask = new_img.hueDistance(color=Color.WHITE).binarize()
        result = new_img - mask.invert()
        # result.show()
        result.save(save_path + '/bk' + str(i) + ".jpg")
    
    end = time.time()
    print(str(i) + " imagenes procesadas correctamente. Tiempo: " + str(end - init) + " segs.")

if __name__ == "__main__":
    """Correr el modulo desde la consola."""
    import sys

    if len(sys.argv) == 4:
        backg(sys.argv[1], sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 3:
        backg(sys.argv[1], sys.argv[2])
    else:
        print('Debe especificar todos los argumentos necesarios.')
