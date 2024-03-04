import unittest
import conversions


class ConversionTestCase(unittest.TestCase):
    def testCelsiusToKelvin(self):
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(0), 273.15)
        self.assertAlmostEqual(conversions.convertCelsiusToKelvin(100), 373.15)

    def testCelsiusToFahrenheit(self):
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(0), 32)
        self.assertAlmostEqual(conversions.convertCelsiusToFahrenheit(-40), -40)

    def testFahrenheitToCelsius(self):
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(32), 0)
        self.assertAlmostEqual(conversions.convertFahrenheitToCelsius(212), 100)

    def testFahrenheitToKelvin(self):
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(32), 273.15)
        self.assertAlmostEqual(conversions.convertFahrenheitToKelvin(212), 373.15)

    def testKelvinToCelsius(self):
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(273.15), 0)
        self.assertAlmostEqual(conversions.convertKelvinToCelsius(373.15), 100)

    def testKelvinToFahrenheit(self):
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(273.15), 32)
        self.assertAlmostEqual(conversions.convertKelvinToFahrenheit(373.15), 212)

if __name__ == '__main__':
    unittest.main()