'''
Created on 11/1/2015

@author: Gabo
Observaciones: Se considera tiempo "nocturno" a aquellas horas entre las 6pm a las 6am.
'''
from datetime import datetime, timedelta
from decimal import *

format = '%Y-%m-%d %I:%M %p'

def horasNocturnas(inidate, findate, t_reserva):
    h_nocturnas = 0
    if(inidate.hour < 6):
        h_nocturnas += 12*t_reserva.days
        if(findate.hour >= 6):
            h_nocturnas += (6 - inidate.hour)
        else:
            if(findate.hour >= inidate.hour):
                h_nocturnas += findate.hour - inidate.hour
            else:
                h_nocturnas += 6 + (6 - inidate.hour) + findate.hour
        
        if (findate.hour >= 18):
            h_nocturnas += findate.hour - 18
        
    else:
        h_nocturnas += 12*t_reserva.days
        if(findate.hour >= inidate.hour):
            if(findate.hour >= 18):
                if(inidate.hour >= 18):
                    h_nocturnas += findate.hour - inidate.hour
                else:
                    h_nocturnas += (findate.hour - 18)
        else:
            if(findate.hour >= 6):
                h_nocturnas += 6
            
            if(inidate.hour >= 18):
                h_nocturnas += 24 - inidate.hour
                
            if(findate.hour >= 18):
                    h_nocturnas += findate.hour - 18
                    
    if(findate.minute > 0 and (findate.hour <= 6 or findate.hour >= 16)):
        h_nocturnas += 1
    
    return h_nocturnas

def totalHoras(t_reserva):
    total = t_reserva.days*24 + t_reserva.seconds // 3600
    if((t_reserva.seconds // 60)%60 != 0):
        total += 1
    return total

def reservacion(inidate, findate, tarifa):
    t_reserva = findate - inidate
    h_totales = totalHoras(t_reserva)
    
    if (tarifa['diurna'] < Decimal(0) or tarifa['nocturna'] < Decimal(0)):
        return print("Las tarifas deben ser positivas.")
    if ((type(inidate) is datetime) and (type(findate) is datetime)):
        if (t_reserva >= timedelta(minutes=15) and t_reserva <= timedelta(days=3)):
            h_nocturnas = horasNocturnas(inidate, findate, t_reserva)
            total = tarifa['diurna']*Decimal(h_totales - h_nocturnas) + tarifa['nocturna']*h_nocturnas
            print("El total a pagar es: %.2f" % total)
        else:
            if(t_reserva < timedelta(microseconds=0)):
                return  print("Fecha negativa")
            else:
                return print('La reservacion debe ser minimo de 15 minutos y maximo 72 horas.')
    else:    
        return print("Asegurese de indicar 2 argumentos de tipo datetime.")
    
    '''
    aqui los casos de prueba
    '''

reservacion(datetime(2010, 5, 25, 19), datetime(2010, 5, 26, 18, 15),{'diurna': Decimal(10), 'nocturna': Decimal(15)})