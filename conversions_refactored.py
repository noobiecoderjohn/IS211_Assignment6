class ConversionNotPossible(Exception):
    """Exception for invalid conversion attempts."""
    pass

def convert(fromUnit, toUnit, value):
    """Converts a value from one unit to another.

    Args:
        fromUnit (str): The unit you are converting from.
        toUnit (str): The unit you are converting to.
        value (float): The value in the fromUnit.

    Returns:
        float: The converted value in the toUnit.

    Raises:
        ConversionNotPossible: If the conversion between the specified units is not supported.
    """
    conversions = {
        'Celsius': {'Kelvin': 273.15, 'Fahrenheit': (9/5, 32)},
        'Kelvin': {'Celsius': -273.15, 'Fahrenheit': (9/5, -459.67)},
        'Fahrenheit': {'Celsius': (5/9, -32), 'Kelvin': (5/9, 255.37)},
        'Miles': {'Yards': 1760, 'Meters': 1609.34},
        'Yards': {'Miles': 1/1760, 'Meters': 0.9144},
        'Meters': {'Miles': 1/1609.34, 'Yards': 1.09361}
    }

    # Check for conversion to the same unit
    if fromUnit == toUnit:
        return value

    try:
        # Attempt to perform the conversion using the appropriate formula.
        if fromUnit in ['Celsius', 'Fahrenheit'] and toUnit in ['Kelvin', 'Fahrenheit', 'Celsius']:
            if isinstance(conversions[fromUnit][toUnit], tuple):
                multiplier, add = conversions[fromUnit][toUnit]
                return value * multiplier + add
            else:
                return value + conversions[fromUnit][toUnit]
        elif fromUnit in ['Miles', 'Yards', 'Meters'] and toUnit in ['Miles', 'Yards', 'Meters']:
            return value * conversions[fromUnit][toUnit]
        else:
            raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not supported.")
    except KeyError:
        # If no conversion formula is found, raise an exception.
        raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not supported.")