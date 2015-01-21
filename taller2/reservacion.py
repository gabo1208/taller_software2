'''
Created on 11/1/2015

@author: Gabo
Observaciones: Se considera tiempo "nocturno" a aquellas horas entre las 6pm a las 6am.
'''
import unittest
import tests
from datetime import datetime, timedelta
from decimal import Decimal

def suite():
    suite = unittest.TestSuite()
    suite.addTest(tests.suite())
    return suite

def horasNocturnas(inidate, findate, t_reserva):
    h_nocturnas = 0
    fin_noche, ini_noche = 18, 6
    if(inidate.hour < ini_noche):
        h_nocturnas += 12*t_reserva.days
        if(findate.hour >= ini_noche):
            h_nocturnas += (ini_noche - inidate.hour)
        else:
            if(findate.hour >= inidate.hour):
                h_nocturnas += findate.hour - inidate.hour
            else:
                h_nocturnas += ini_noche + (ini_noche - inidate.hour) + findate.hour
        
        if (findate.hour >= fin_noche):
            h_nocturnas += findate.hour - fin_noche
        
    else:
        h_nocturnas += 12*t_reserva.days
        if(findate.hour >= inidate.hour):
            if(findate.hour >= fin_noche):
                if(inidate.hour >= fin_noche):
                    h_nocturnas += findate.hour - inidate.hour
                else:
                    h_nocturnas += (findate.hour - fin_noche)
        else:
            if(findate.hour >= ini_noche):
                h_nocturnas += ini_noche
            
            if(inidate.hour >= fin_noche):
                h_nocturnas += 24 - inidate.hour
                
            if(findate.hour >= 18):
                    h_nocturnas += findate.hour - 18
                    
    if(findate.minute - inidate.minute > 0 and (findate.hour <= 6 or findate.hour >= 16)):
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
        print("Las tarifas deben ser positivas.")
        return False
    if ((type(inidate) is datetime) and (type(findate) is datetime)):
        if (t_reserva >= timedelta(minutes=15) and t_reserva <= timedelta(days=3)):
            h_nocturnas = horasNocturnas(inidate, findate, t_reserva)
            total = tarifa['diurna']*Decimal(h_totales - h_nocturnas) + tarifa['nocturna']*h_nocturnas
            print("El total a pagar es: %.2f" % total)
            return total
        else:
            if(t_reserva < timedelta(microseconds=0)):
                print("Fecha negativa")
                return False
            else:
                print('La reservacion debe ser minimo de 15 minutos y maximo 72 horas.')
                return False
    else:    
        print("Asegurese de indicar 2 argumentos de tipo datetime.")
        return False
    
'''
Aqui se ejecutan los casos de prueba
'''
   
if __name__ == '__main__':
        unittest.main(defaultTest='suite')
