class LineaTelefonica:
    '''----------------------------------------------------------------
    # atributos
    ----------------------------------------------------------------'''
    
    # Numero de llamadas realizadas
    numeroLlamadas = 0
    
    # Numero de minutos consumidos
    numeroMinutos = 0
    
    # Costo total de las llamadas
    costoLlamadas = 0

    descuento = 0 

    prepago = 0

    '''----------------------------------------------------------------
    # 1,2, 3, 4, 5, 6
    ----------------------------------------------------------------'''

    estrato = 0
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    # Inicializar el número de llamadas, número de minutos y costo de llamadas en 0.
    def __init__(self):
        self.numeroLlamadas = 0 
        self.numeroMinutos = 0
        self.costoLlamadas = 0
        # TODO Parte2 PuntoA: Completar el método según la documentación dada.
        
    #Retorna el costo total de las llamadas realizadas.
    def darCostoLlamadas(self):
        return self.costoLlamadas
        # TODO Parte2 PuntoB: Completar el método según la documentación dada.
        
    # Retorna el número de llamadas realizadas por esta línea.
    def darNumeroLlamadas(self):
        return self.numeroLlamadas
        # TODO Parte2 PuntoC: Completar el método según la documentación dada.
        
    # Retorna el número de minutos consumidos.
    def darNumeroMinutos(self):
        return self.numeroMinutos
        # TODO Parte2 PuntoD: Completar el método según la documentación dada.

    # Reinicia la línea telefónica, dejando todos sus valores en cero.
    # post: El número de llamadas, número de minutos y costo de llamadas son 0.
    def reiniciar(self):
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0
        
        # TODO Parte2 PuntoE: Completar el método según la documentación dada.

    # Agrega una llamada local a la línea telefónica
    # post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 35 ).
    # :param pMinutos Número de minutos de la llamada. pMinutos >0.
    def agregarLlamadaLocal(self, pMinutos):
        
        # Una llamada más
        self.numeroLlamadas += 1
        # Suma los minutos consumidos
        self.numeroMinutos += pMinutos
        # Suma el costo (costo por minuto: 35 pesos)
        self.costoLlamadas += pMinutos * 35

        self.prepago - self.costoLlamadas


    """
        Agrega una llamada de larga distancia a la línea telefónica.
        
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 380 )
        
        :param pMinutos: Número de minutos de la llamada. pMinutos >0.
        """
    def agregarLlamadaLargaDistancia(self, pMinutos):
        
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        self.costoLlamadas += pMinutos * 380
        # TODO Parte2 PuntoF: Completar el método según la documentación dada.

    '''
        Agrega una llamada a celular a la lÍnea telefónica
        post: Se incrementá en 1 numeroDeLlamadas, se incremento numeroDeMinutos en minutos, costoLlamadas aumentá en ( minutos * 999 )
        :param pMinutos Número de minutos de la llamada. pMinutos >0.
    '''
    def agregarLlamadaCelular(self, pMinutos):
        
        self.numeroLlamadas += 1
        self.numeroMinutos += pMinutos
        self.costoLlamadas += pMinutos * 999
        # TODO Parte2 PuntoG: Completar el método según la documentación dada.
       
    def ConsultarDescuento(self):
        return self.descuento
    
    def AplicarDescuento(self): 
        return (self.costoLlamadas * self.descuento) / 100 
    
    def darSaldo(self):
        return self.prepago
    
    def Recarga (self, Recarga):
        nPrepago = self.prepago + Recarga
        self.prepago = nPrepago 
        
    def MotivarCliente(self):
        if self.numeroMinutos == 30:
            self.prepago + 1000
