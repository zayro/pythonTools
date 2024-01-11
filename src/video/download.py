from pytube import YouTube


def Download(link):
    try:
        
       YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
 
    except:
        print("Hubo un error al descargar el video del URL proporcionado...")
 
# Pedimos al usuario en la línea de comandos ingresar el URL del video para descargar
link = "https://www.youtube.com/watch?v=WHejvUhX6rk"

# Descargamos el video
Download(link)
