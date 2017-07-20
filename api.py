# -*- coding: utf-8 -*-
""" Hecho por Wilson Tovar """

import sys
import zerorpc
from background import backg as bg


class BackgroundAPI(object):
    """ API para la realización de tareas y conexion de la GUI con python """

    def bkg(self, images_path, save_path, extension=""):
        """ Realizar la  """
        try:
            if extension is "":
                return bg(images_path, save_path)
            else:
                return bg(images_path, save_path, extension)
        except Exception as e:
            return "ERROR. Ha ocurrido un error. Por favor, verifique los argumentos."

    def echo(self):
        return 'Hola we.'


def parse_port():
    port = 4242
    try:
        port = int(sys.argv[1])
    except Exception as e:
        pass

    return '{}'.format(port)


def main():
    addr = 'tcp://127.0.0.1:' + parse_port()
    s = zerorpc.Server(BackgroundAPI())
    s.bind(addr)
    print('Corriendo servidor en {}'.format(addr))
    s.run()


if __name__ == '__main__':
    main()
