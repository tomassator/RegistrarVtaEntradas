from django.shortcuts import render
from rve.controlador import gestorVentaEntrada, pantallaSede


# Instanciamos el controlador
controlador = gestorVentaEntrada.GestorVentaDeEntrada()
# Creamos pantallas
controlador.crearPantallasSede()

# Funcion que devuelve la pantalla inicial para seleccionar la opcion registrar venta de entrada


def opciones(request):
    return render(request, 'primerapantalla.html')

# Funcion que muestra la primera pantalla con la informacion solicitada de las tarifas


def opcionVentaEntrada(request):
    controlador.entradas = []
    # Busca el empleado asociado al usuario actual
    controlador.buscarEmpleadoLogueado()
    controlador.buscarSede()  # El controlador ejecuta el metodo buscar sede
    # El controlador ejecuta el metodo buscarTarifasdeSede
    tarifas_vigentes = controlador.buscarTarifasDeSede()
    # El controlador ejecuta el metodo de seteo, setTarifasd
    controlador.setTarifas(tarifas_vigentes)
    return render(request, 'venta.html', {"tarifas": tarifas_vigentes})

# Esta vista muestra las tarifas con su monto sin guia asociado


def montoSinGuia(request):
    return render(request, 'montosinguia.html', {"tarifas": controlador.tarifas})

# Esta vista muestra las tarifas con su monto con guia asociado


def montoConGuia(request):
    return render(request, 'montoconguia.html', {"tarifas": controlador.tarifas})

# Esta vista muestra la tarifa seleccionada y pide que se seleccionen entradas


def tomarSeleccionTarifa(request):
    # Rescatamos el id de la tarifa que mostramos anteriormente
    id_tarifa = request.GET["id"]
    # Rescatamos el monto de la tarifa que mostramos anteriormente
    monto = request.GET["monto"]
    # Rescatamos el tipo de visita que mostramos anteriormente
    tipoVisita = request.GET["tipoVisita"]
    # Rescatamos el tipo de entrada que mostramos anteriormente
    tipoEntrada = request.GET["tipoEntrada"]
    # Rescatamos el tipò de entrada que mostramos anteriormente
    conGuia = request.GET["conGuia"]
    # Rescatamos la fecha de fin de vigencia de la tarifa que mostramos anteriormente
    fechaFinVigencia_tarifa = request.GET["fechaFinVigencia"]
    # El controlador ejecuta el metodo obtenerFechaHoraActual()
    fechaActual = controlador.obtenerFechaHoraActual()
    # El controlador ejecuta el metodo buscarCantidadSede()
    cantMaxVisitantes = controlador.buscarCantidadSede()
    # El controlador ejecuta el metodo buscarVisitantesEnSede()
    cantVisitantesEnSede = controlador.buscarVisitantesEnSede(fechaActual)
    # El controlador ejecuta el metodo buscarReservasParaAsistir()
    cantVisitantesReserva = controlador.buscarReservasParaAsistir(fechaActual)
    # Se calcula la cantidad de visitantes disponibles
    cantVisitantesDisp = int(cantMaxVisitantes) - int(cantVisitantesEnSede) + int(cantVisitantesReserva)
    # El controlador ejecuta el metodo buscarExposicionVIgente()
    duracion = controlador.buscarExposicionVigente()
    return render(request, 'duracion.html', {"duracion": duracion, "id": id_tarifa, "monto": monto, "fechaFinVigencia": fechaFinVigencia_tarifa, "tipoVisita": tipoVisita, "tipoEntrada": tipoEntrada, "cantVisitantesDisp": cantVisitantesDisp, "conGuia": conGuia})

# Esta vista muestra el detalle de la entrada y pide la confirmacion


def cantidadEntradasAEmitir(request):
    cantidad = request.GET["cantEntradas"]
    idTarifa = request.GET["idTarifa"]
    fechaFinVigencia = request.GET["fechaFinVigencia"]
    tipoVisita = request.GET["tipoVisita"]
    tipoEntrada = request.GET["tipoEntrada"]
    conGuia = request.GET["conGuia"]
    # El controlador ejecuta el metodo buscarCantidadSede()
    cantMaxVisitantes = controlador.buscarCantidadSede()
    # El controlador ejecuta el metodo obtenerFechaHoraActual()
    fechaActual = controlador.obtenerFechaHoraActual()
    # El controlador ejecuta el metodo buscarVisitantesEnSede()
    cantVisitantesEnSede = controlador.buscarVisitantesEnSede(fechaActual)
    # El controlador ejecuta el metodo buscarReservasParaAsistir()
    cantVisitantesReserva = controlador.buscarReservasParaAsistir(fechaActual)
    # Se suman la cantidad total de visitantes si se llegasen a vender las entradas
    cantVisitantes = int(cantVisitantesEnSede) + \
        int(cantVisitantesReserva) + int(cantidad)
    # El controlador ejecuta el metodo validarLimiteVisitantes() y espera un booleano como respuesta
    if controlador.validarLimiteVisitantes(cantVisitantes, cantMaxVisitantes):
        return render(request, "error.html")
    montoPorEntrada = request.GET["monto"]
    # El controlador ejecuta el metodo calcularMontoTotalVenta
    totalMontoVenta = controlador.calcularMontoTotalVenta(
        cantidad, montoPorEntrada)
    return render(request, "cantEntradasSelec.html", {"cantidadEntradas": cantidad, "totalmonto": totalMontoVenta,
                                                      "montoPorEntrada": montoPorEntrada, "totalMontoVenta": totalMontoVenta, "idTarifa": idTarifa, "cantVisitantes": cantVisitantes, "conGuia":conGuia,"tipoEntrada":tipoEntrada,"tipoVisita":tipoVisita,"fechaFinVigencia":fechaFinVigencia})

# Esta vista imprime todas las entradas que se vendieron


def tomarVentaConfirmada(request):
    controlador.actualizarVisitantesEnPantalla(
        int(request.GET["cantVisitantes"]))
    montoPorEntrada = request.GET["monto"]
    cantidad = request.GET["cantEntradas"]
    id_tarifa = request.GET["idTarifa"]
    id_sede = controlador.sede.id
    for i in range(int(cantidad)):
        nro_entrada = controlador.buscarUltimoNroEntrada()
        controlador.generarEntradas(
            nro_entrada, montoPorEntrada, id_tarifa, id_sede)
    entradas_vendidas = controlador.imprimirEntradas
    return render(request, "confirmada.html", {"entradasVendidas": entradas_vendidas})

# Esta vista muestra la cantidad de visitantes que actualmente estan en la sede
# Estos metodos simulan la existencia previa de la pantalla


def pantallaVisitantesSede(request):
    pantalla = controlador.pantalla[0]
    return render(request, "pantallaSede.html", {"pantalla": pantalla, "nombre": pantalla.getNombre()})


def pantallaVisitantesSedeDos(request):
    pantalla = controlador.pantalla[1]
    return render(request, "pantallaSedeDos.html", {"pantalla": pantalla, "nombre": pantalla.getNombre()})


def pantallaVisitantesSedeTres(request):
    pantalla = controlador.pantalla[2]
    return render(request, "pantallaSedeTres.html", {"pantalla": pantalla, "nombre": pantalla.getNombre()})


def pantallaPrincipal(request):
    pantallaPrinc = controlador.pantallaPrincipal[0]
    return render(request, "pantallaPrincipal.html", {"pantallaPrincipal": pantallaPrinc})
