import pygetwindow as gw

# Obtén todas las ventanas abiertas
ventanas = gw.getAllTitles()

# Busca la ventana específica por su título
titulo_ventana = "new chat"
ventana = gw.getWindowsWithTitle(titulo_ventana)

# Verifica si se encontró la ventana
if ventana:
    # Accede a la ventana encontrada
    ventana = ventana[0]
    print("Se encontró la ventana:", ventana.title)

    # Puedes realizar acciones en la ventana, por ejemplo, maximizarla
    ventana.maximize()
else:
    print("No se encontró la ventana con el título especificado")
