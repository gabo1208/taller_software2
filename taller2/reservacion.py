'''
Created on 11/1/2015

@author: Gabo
'''
from datetime import datetime, timedelta
from decimal import *

getcontext().prec = 2

def reservacion(inidate, findate, tarifa):
    t_reserva = findate - inidate
    if (tarifa['diurna'] < Decimal(0) or tarifa['nocturna'] < Decimal(0)):
        return print("Las tarifas deben ser positivas.")
    if ((type(inidate) is datetime) and (type(findate) is datetime)):
        if (t_reserva >= timedelta(minutes=15) and t_reserva <= timedelta(days=3)):
            return print(t_reserva.seconds // 60)
        else:
            if(t_reserva < timedelta(microseconds=0)):
                return  print("Fecha negativa")
            else:
                return print('La reservacion debe ser minimo de 15 minutos y maximo 72 horas.')
    else:    return False

reservacion(datetime(2010, 5, 25, 0, 11), datetime(2010, 5, 25, 2),{'diurna': Decimal(10), 'nocturna': Decimal(15)})