from rve.models.Sede import Sede
from rve.models.Sesion import Sesion
from rve.models.Tarifa import Tarifa
from rve.models.Entrada import Entrada
from rve.models.ReservaVisita import ReservaVisita
from rve.controlador.pantallaSede import PantallaSede
from rve.controlador.pantallaPrincipal import PantallaPrincipal
from rve.controlador import ISujestorPantalla
from datetime import datetime, date, timedelta


#Clase gestor
class GestorVentaDeEntrada(ISujestorPantalla.sujestorPantalla):
    empleadoLogueado = None
    entradas = []
    sesionActual = Sesion.objects.get(id=1)
    tarifas = None
    sede = None
    cantidadActualVisitantes= None
    pantalla = []
    pantallaPrincipal = []
    observadores = []

    #self.pantalla.actualizarCantidadVisitantes(self.cantidadActualVisitantes)
    #return self.pantalla


    #Este metodo es para simular que las pantallas ya existian de antes
    def crearPantallasSede(self):
        self.pantallaPrincipal.append(PantallaPrincipal())
        for i in range(0,3):
            self.pantalla.append(PantallaSede())
            self.pantalla[i].setNombre("Pantalla Numero: {}".format(i+1))


    # Llama al metodo actualizarCantidadVisitantesd correspondiente a pantalla pasandole por parametro la cantidadActualVisitantes
    def actualizarVisitantesEnPantalla(self, cantidadVisitantes):
        self.cantidadActualVisitantes = cantidadVisitantes
        self.subscribir(self.pantallaPrincipal) #Suscribe la pantalla principal (ObservadorConcreto)
        self.subscribir(self.pantalla) #Suscribie las pantallas de la sede (ObservadorConcreto)
        self.notificar()

    #Metodos Observer
    def subscribir(self, pantallas):
        for pant in pantallas:
            self.observadores.append(pant)

    def quitar(self):
        pass

    def notificar(self):
        for obs in self.observadores:
            obs.actualizarCantidadVisitantes(self.cantidadActualVisitantes)


    #MetodosGestor

    #Retorna el empleado logueado
    def getEmpleado(self):
        return self.empleadoLogueado

    #Llama al metodo actualizarCantidadVisitantesd correspondiente a pantalla pasandole por parametro la cantidadActualVisitantes


    def buscarCantidadSede(self):
        return self.sede.getCantMaximaVisitantes()

    #Metodo que llama a sesion para poder obtener el empleado asociado a ella
    def buscarEmpleadoLogueado(self):
        self.empleadoLogueado = self.sesionActual.getEmpleadoEnSesion()
        return self.empleadoLogueado

    #Ejecuta el metodo calcularDuracionExposicionVigentes de la sede actual
    def buscarExposicionVigente(self):
        fecha_actual = self.obtenerFechaHoraActual()
        duracion = self.sede.calcularDuracionExposicionVigentes(self.sede.id, fecha_actual)
        return duracion

    def buscarReservasParaAsistir(self, fechaActual):
        visitantes = 0
        reservas = ReservaVisita.objects.all()
        for res in reservas:
            if res.sonParaFechaYHoraYSede(fechaActual):
                visitantes += res.cantidadAlumnosConfirmada
        return visitantes

    #Busca en la base de datos todos los objetos de sede que este vinculado al empleado logueado que esta en dicha sede
    def buscarSede(self):
        self.sede = Sede.objects.filter(id__icontains = self.empleadoLogueado.obtenerSede())
        self.sede = self.sede[0] #Devuelve una query ya que no se accede por clave foranea, pero siempre devuelve una sola sede
        return self.sede

    #Busca en la BD todas las tarifas que esten asociadas a una sede
    def buscarTarifasDeSede(self):
        tarifas = Tarifa.objects.filter(nro_sede__icontains = self.sede.id)
        tarifas_vigentes = self.sede.obtenerTarifasVigentes(tarifas)
        return tarifas_vigentes

    #Guarda las tarifas como atributo del gestor
    def setTarifas(self, tarifas):
        self.tarifas = tarifas

    ###Primero obtiene todas las tarifas de la base de datos, encuentra el ultimo registro obtiene su numero y devuelve el numero +1
    #Devuelve todos los numeros de entrada en una lista y retorna el mayor de esa lista + 1
    def buscarUltimoNroEntrada(self):
        numero_entrada = []
        entradas = Entrada.objects.all()
        for ent in entradas:
            numero_entrada.append(ent.numero)
        #ultima_entrada = entradas[(len(entradas)-1)]
        #nro_entrada = ultima_entrada.numero
        #return (int(nro_entrada) + 1)
        return (max(numero_entrada) + 1)


    def calDuracVisitaCompleto(self):
        None

    def cantidadEntradasAEmitir(self):
        None


    #Recibe por parametro todos los datos para registrar una entrada en la base de datos y luego la registra, ademas guarda las entradas como atributo del gestor
    def generarEntradas(self, nro_entrada, montoPorEntrada, idTarifa, idSede):
        fecha_actual = self.obtenerFechaHoraActual()
        entrada = Entrada(fechaVenta=fecha_actual, horaVenta=fecha_actual.hour, monto=int(montoPorEntrada), numero=nro_entrada, tarifa_id=idTarifa, sede_id=idSede)
        entrada.save()
        self.entradas.append(Entrada.objects.get(numero__icontains=nro_entrada))

    #Devuelve las entradas
    def imprimirEntradas(self):
        return self.entradas

    #Devuelve la fecha y hora actual
    def obtenerFechaHoraActual(self):
        return datetime.now()

    def opcionVtaEntradas(self):
        None

    def tomarTarifasSeleccionadas(self):
        None

    #Busca que visitantes estan actualmente en la sede, obtiene todas las entradas y valida si coinciden las fechas con la fecha actual
    #Si es asi entonces quiere decir que estan actualmente dentro de la sede y suma 1 visitante
    def buscarVisitantesEnSede(self, fechaActual):
        visitantes = 0
        entradas = Entrada.objects.all()
        for ent in entradas:
            if ent.sonDeFechaHoraSede(fechaActual):
                visitantes += 1
        return visitantes

    #Valida que la cantidad de visitantes que estan actualmente en la sede no supere la cantidad maxima de visitantes de la sede
    def validarLimiteVisitantes(self, cantidadVisitantes, cantMaximaVisitantes):
        self.cantidadActualVisitantes = cantidadVisitantes
        if cantidadVisitantes > cantMaximaVisitantes:
            return True
        return False

    #Devuelve la multiplicacion entre la cantidad de entradas por su monto
    def calcularMontoTotalVenta(self, cantidadEntradas, montoEntradas):
        total = int(cantidadEntradas) * int(montoEntradas)
        return total

    def finCU(self):
        None