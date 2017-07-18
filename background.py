from SimpleCV import *

def backg(images_path, save_path, extension = "*.jpg"):
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
        print(file)
        new_img = Image(file)
        mask = new_img.hueDistance(color=Color.WHITE).binarize()
        result = new_img - mask.invert()
        result.save(save_path + '/bk' + str(i) + ".jpg")
        i += 1

if __name__ == "__main__":
    import sys

    if not sys.argv[3]:
        backg(sys.argv[1], sys.argv[2])
    else:
        backg(sys.argv[1], sys.argv[2], sys.argv[3])

