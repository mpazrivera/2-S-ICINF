class ReservaHostal():
    def __init__(self,nombre_cliente, fecha_ini, fecha_fin, num_habitacion):
        self.nombre_cliente = nombre_cliente 
        self.fecha_ini = fecha_ini
        self.fecha_fin = fecha_fin
        self.num_habitacion = num_habitacion

    duracion_estadias = (self.fecha_fin - self.fecha_ini)

    def dias_estadias(self):
        return(f"El tiempo que se quedo el cliente fue de {duracion_estadias}")
    