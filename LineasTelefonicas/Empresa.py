from LineaTelefonica import LineaTelefonica

class Empresa:
    
    '''----------------------------------------------------------------
    # atributos
    ----------------------------------------------------------------'''
    
    # Línea telefónica número 1.
    linea1 = 0
    # Línea telefónica número 2.
    linea2 = 0
    # Línea telefónica número 3.
    linea3 = 0
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def __init__(self):
        self.linea1 = LineaTelefonica()
        self.linea2 = LineaTelefonica()
        self.linea3 = LineaTelefonica()
        # TODO Parte3 PuntoA: Construir linea2 y linea3.
        
    # Retorna la l�nea 1.
    def darLinea1(self):
        return self.linea1
        # TODO Parte3 PuntoB: Completar el m�todo seg�n la documentaci�n dada.

    # Retorna la l�nea 2.
    def darLinea2(self):
        return self.linea2
        # // TODO Parte3 PuntoC: Completar el m�todo seg�n la documentaci�n dada.

    # Retorna la l�nea 3.
    def darLinea3(self):
        return self.linea3
        # // TODO Parte3 PuntoD: Completar el m�todo seg�n la documentaci�n dada.

    '''
	# Retorna el n�mero total de llamadas realizadas.
	# @return Total de llamadas de las tres l�neas.
	'''
    def darTotalNumeroLlamadas(self):
        return self.linea1.darNumeroLlamadas() + self.linea2.darNumeroLlamadas() + self.linea3.darNumeroLlamadas() 
        # TODO Parte3 PuntoE: Completar el m�todo seg�n la documentaci�n dada.

    '''
	    # Retorna el total de minutos consumidos.
	    # @return Total de minutos de las tres l�neas.
	'''
    def darTotalMinutos(self):
        return self.linea1.darNumeroMinutos() + self.linea2.darNumeroMinutos() + self.linea3.darNumeroMinutos()
        # TODO Parte3 PuntoF: Completar el m�todo seg�n la documentaci�n dada.

    '''
	    # Retorna el costo total de las llamadas realizadas.
	    # @return Costo total de las tres l�neas.
    '''
    def darTotalCostoLlamadas(self):
        return self.linea1.darCostoLlamadas() + self.linea2.darCostoLlamadas() + self.linea3.darCostoLlamadas()
        # TODO Parte3 PuntoG: Completar el m�todo seg�n la documentaci�n dada.

    '''
        # Retorna el costo promedio de un minuto, seg�n los minutos consumidos. <br>
	    # @return Costo promedio por minuto.
    '''
    def darCostoPromedioMinuto(self):
        return self.darTotalCostoLlamadas() / self.darTotalMinutos()
        # TODO Parte3 PuntoH: Completar el m�todo seg�n la documentaci�n dada.

    '''
        # Agrega una llamada local a la l�nea telef�nica 1 <br>
        # <b>post: </b> Se agreg� la llamada a la l�nea 1.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
        '''
    def agregarLlamadaLocalLinea1(self, pMinutos):
        self.linea1.agregarLlamadaLocal(pMinutos)

    '''
        # Agrega una llamada local a la l�nea telef�nica 2. <br>
        # <b>post: </b> Se agreg� la llamada a la l�nea 2.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLocalLinea2(self, pMinutos):
        self.linea2.agregarLlamadaLocal(pMinutos)
        # TODO Parte3 PuntoI: Completar el m�todo seg�n la documentaci�n dada.

        '''
        # Agrega una llamada local a la l�nea telef�nica 3. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 3.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
        '''
    def agregarLlamadaLocalLinea3(self, pMinutos):
        self.linea3.agregarLlamadaLocal(pMinutos)
        # TODO Parte3 PuntoJ: Completar el m�todo seg�n la documentaci�n dada.

        '''
        # Agrega una llamada de larga distancia a la l�nea telef�nica 1. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 1.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
        '''
    def agregarLlamadaLargaDistanciaLinea1(self, pMinutos):
        self.linea1.agregarLlamadaLargaDistancia(pMinutos)

    '''
        # Agrega una llamada de larga distancia a la l�nea telef�nica 2. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 2.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaLargaDistanciaLinea2(self, pMinutos):
        self.linea2.agregarLlamadaLargaDistancia(pMinutos)
        # TODO Parte3 PuntoK: Completar el m�todo seg�n la documentaci�n dada.
    
        '''
        # Agrega una llamada de larga distancia a la l�nea telef�nica 3. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 3.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
        '''
    def agregarLlamadaLargaDistanciaLinea3(self, pMinutos):
        self.linea3.agregarLlamadaLargaDistancia(pMinutos)
        # TODO Parte3 PuntoL: Completar el m�todo seg�n la documentaci�n dada.

        '''
        # Agrega una llamada a celular a la l�nea telef�nica 1. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 1.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
        '''
    def agregarLlamadaCelularLinea1(self, pMinutos):
        self.linea1.agregarLlamadaCelular(pMinutos)

    '''
        # Agrega una llamada a celular a la l�nea telef�nica 2. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 2.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
    '''
    def agregarLlamadaCelularLinea2(self, pMinutos):
        self.linea2.agregarLlamadaCelular(pMinutos)
        # TODO Parte3 PuntoM: Completar el m�todo seg�n la documentaci�n dada.
    
        '''
        # Agrega una llamada a celular a la l�nea telef�nica 3. <br>
        # <b>post: </b> Se agrega la llamada a la l�nea 3.
        # @param pMinutos N�mero de minutos de la llamada. pMinutos > 0.
        '''
    def agregarLlamadaCelularLinea3(self, pMinutos):
        self.linea3.agregarLlamadaCelular(pMinutos)
        #TODO Parte3 PuntoN: Completar el m�todo seg�n la documentaci�n dada.
    
        '''
        # Reinicia todas las l�neas telef�nicas.
        # <b>post: </b> Se reinici� la llamada a la l�nea 1, 2 y 3. 
        '''
    def reiniciar(self):
        self.linea1.reiniciar()
        self.linea2.reiniciar()
        self.linea3.reiniciar()
        # // TODO Parte3 PuntoB: Completar el m�todo para reiniciar las lineas 2 y 3.

    def DescuentoTodos(self):
        Descuento1=(self.linea1.costoLlamadas * self.linea1.descuento) / 100
        Descuento2=(self.linea2.costoLlamadas * self.linea2.descuento) / 100
        Descuento3=(self.linea3.costoLlamadas * self.linea3.descuento) / 100
        return Descuento1 + Descuento2 + Descuento3

    '''----------------------------------------------------------------
    # Puntos de Extensi�n
    ----------------------------------------------------------------'''
    
    # M�todo para la extensi�n 1.
    # @return Respuesta 1.
    def metodo1(self):
        return "Respuesta 1"

    # M�todo para la extensi�n 2.
    # @return Respuesta 2.
    def metodo2(self):
        return "Respuesta 2"
