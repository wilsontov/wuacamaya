using PyCall, FileIO
@pyimport SimpleCV

module Background
  """ Módulo con todas las funciones de procesamiento de imágenes """

  function backg(path::String, save_path::String)
    """ Eliminar el fondo blanco de una imagen

        path : la carpeta que contiene las imágenes
        save_path : la carpeta donde se guardarán las imágenes modificadas
    """
    init = Float64(time())
    dir = Array{String,1}(readdir(path))

    for file in dir
      img = SimpleCV.Image(path*file)
      mask = img[:hueDistance]()[:binarize]()
      result = img - mask[:invert]()
      result[:save](save_path*file)
    end


    end_time = Float64(time())
    info(string(length(dir)," imagenes procesadas. Tiempo: ",end_time - init," segs."))
    return string(length(dir)," imagenes procesadas. Tiempo: ",end_time - init," segs.")
  end

  export backg
end

module API
  """ Implementación de una pequeña API """
  # TODO Implementar
end

if length(ARGS) == 2
    using BackgroundModule
    backg(ARGS[1], ARGS[2])
else
    warn("Debe escribir todos los argumentos.")
end
