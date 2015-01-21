import unittest
import reservacion
from _datetime import datetime
from decimal import Decimal

class TestPruebasInicializacion(unittest.TestCase):
    
        format = '%Y-%m-%d %I:%M %p'
        tarifa = {'diurna': Decimal(10), 
                       'nocturna': Decimal(15)}
    
class TestPruebas(TestPruebasInicializacion):
    
    def test_Fecha_Final_Menor_Inicial(self):
        inidate = datetime.strptime('2015-11-01 03:01 AM', self.format)
        findate = datetime.strptime('2015-11-01 03:00 AM', self.format)
        self.assertFalse(reservacion.reservacion(inidate, findate, self.tarifa))
        
    def test_reserva_Mayor_3Dias(self):
        inidate = datetime.strptime('2015-11-01 03:00 AM', self.format)
        findate = datetime.strptime('2015-11-04 03:01 AM', self.format)
        self.assertFalse(reservacion.reservacion(inidate, findate, self.tarifa))
        
    def test_reserva_menor_a_15Min(self):
        inidate = datetime.strptime('2015-11-01 03:00 AM', self.format)
        findate = datetime.strptime('2015-11-04 03:14 AM', self.format)
        self.assertFalse(reservacion.reservacion(inidate, findate, self.tarifa))
        
    def test_reservacionSinNoche(self):
        inidate = datetime.strptime('2015-11-01 06:00 AM', self.format)
        findate = datetime.strptime('2015-11-01 06:00 PM', self.format)
        self.assertEqual(reservacion.reservacion(inidate, findate, self.tarifa), 12*self.tarifa['diurna'])
        
    def test_reservaSinDia(self):
        inidate = datetime.strptime('2015-11-01 06:00 PM', self.format)
        findate = datetime.strptime('2015-11-02 06:00 AM', self.format)
        self.assertEqual(reservacion.reservacion(inidate, findate, self.tarifa), 12*self.tarifa['nocturna'])
        
    def test_2_dias_enteros_empezando_en_noche(self):
        inidate = datetime.strptime('2015-11-01 03:00 PM', self.format)
        findate = datetime.strptime('2015-11-03 03:00 PM', self.format)
        total = 24*self.tarifa['nocturna'] + 24*self.tarifa['diurna']
        self.assertEqual(reservacion.reservacion(inidate, findate, self.tarifa), total)
        
    def test_2_dias_enteros_empezando_en_dia(self):
        inidate = datetime.strptime('2015-11-01 09:00 PM', self.format)
        findate = datetime.strptime('2015-11-03 09:00 PM', self.format)
        total = 24*self.tarifa['nocturna'] + 24*self.tarifa['diurna']
        self.assertEqual(reservacion.reservacion(inidate, findate, self.tarifa), total)
        
    def test_11_horas_noche(self):
        inidate = datetime.strptime('2015-11-01 03:00 AM', self.format)
        findate = datetime.strptime('2015-11-02 02:00 AM', self.format)
        total = 11*self.tarifa['nocturna'] + 12*self.tarifa['diurna']
        self.assertEqual(reservacion.reservacion(inidate, findate, self.tarifa), total)
        
    def test_fraccion_de_hora(self):
        inidate = datetime.strptime('2015-11-01 03:10 AM', self.format)
        findate = datetime.strptime('2015-11-02 02:11 AM', self.format)
        total = 12*self.tarifa['nocturna'] + 12*self.tarifa['diurna']
        self.assertEqual(reservacion.reservacion(inidate, findate, self.tarifa), total)
        
    def test_fraccion_de_hora_insuficiente(self):
        inidate = datetime.strptime('2015-11-01 03:12 AM', self.format)
        findate = datetime.strptime('2015-11-02 02:11 AM', self.format)
        total = 11*self.tarifa['nocturna'] + 12*self.tarifa['diurna']
        self.assertEqual(reservacion.reservacion(inidate, findate, self.tarifa), total)
        
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestPruebas))
    return test_suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')