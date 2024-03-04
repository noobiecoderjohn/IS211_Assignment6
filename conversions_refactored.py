class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    conversions = {
        'Celsius': {'Kelvin': 273.15, 'Fahrenheit': (9/5, 32)},
        'Kelvin': {'Celsius': -273.15, 'Fahrenheit': (9/5, -459.67)},
        'Fahrenheit': {'Celsius': (5/9, -32), 'Kelvin': (5/9, 255.37)},
        'Miles': {'Yards': 1760, 'Meters': 1609.34},
        'Yards': {'Miles': 1/1760, 'Meters': 0.9144},
        'Meters': {'Miles': 1/1609.34, 'Yards': 1.09361}
    }

    if fromUnit == toUnit:
        return value

    try:
        if fromUnit in ['Celsius', 'Fahrenheit'] and toUnit in ['Kelvin', 'Fahrenheit', 'Celsius']:
            if isinstance(conversions[fromUnit][toUnit], tuple):
                multiplier, addend = conversions[fromUnit][toUnit]
                return value * multiplier + addend
            else:
                return value + conversions[fromUnit][toUnit]
        elif fromUnit in ['Miles', 'Yards', 'Meters'] and toUnit in ['Miles', 'Yards', 'Meters']:
            return value * conversions[fromUnit][toUnit]
        else:
            raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not possible.")
    except KeyError:
        raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not supported.")