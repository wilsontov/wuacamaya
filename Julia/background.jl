using PyCall, FileIO
@pyimport SimpleCV

module BackgroundModule
  function backg(path::String, save_path::String)
    """ Eliminar el fondo blanco de una imagen
        Keyword arguments:
        path -- la carpeta que contiene las imagenes
        save_path -- la carpeta donde se guardaran las imagenes modificadas
        extension -- extension de las imagenes (default: *.jpg) (deprecated)
    """
    init = Float64(time())
    dir = Array{String,1}(readdir(path))

    for file in dir
      img = SimpleCV.Image(path*file)
      mask = img[:hueDistance]()[:binarize]()
      result = img - mask[:invert]()
      result[:save](save_path*file)
    end

    end_time = Float64(time())  # Tiempo final
    info(string(length(dir)," imagenes procesadas. Tiempo: ",end_time - init," segs."))
    return string(length(dir)," imagenes procesadas. Tiempo: ",end_time - init," segs.")
  end

  export backg
end

if length(ARGS) == 2
    using BackgroundModule
    BackgroundModule.backg(ARGS[1], ARGS[2])
else
    error("Debe escribir todos los argumentos.")
end
