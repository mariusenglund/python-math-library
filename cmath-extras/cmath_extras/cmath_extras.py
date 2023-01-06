"""
This module contains functions that make it easier to work with complex numbers in Python.
"""

from math import e, pi
from cmath import phase

def cnum(a:int|float|complex, b:int|float|complex=None, unit:str='deg') -> complex:
    """Returns a complex number which can be used in further calculations.

    The complex number is defined using `a` and/or `b` and can be entered in both the Cartesian and polar complex plane by including or excluding the imaginary unit 'j'.
    
    When entering a complex number in the polar complex plane, the angle unit is degrees by default. This can be changed to radians by passing 'rad' to `unit`.

    Parameters
    ----------
    `a` : int | float | complex
        * The real part when entering the complex number as Cartesian coordinates, or
        
        * both the real and imaginary parts when entering the complex number as a Cartesian polynomial, or
        
        * the magnitude/modulus when entering the complex number as a position vector in the polar complex plane.

    `b` : int | float | complex, optional
        * The imaginary part, including the imaginary unit, when entering the complex number as Cartesian coordinates, or
        
        * the angle/argument when entering the complex number as a position vector in the polar complex plane (default is None).
    
    `unit` : {'deg', 'rad'}, optional
        * The angle unit (degrees or radians) when entering the complex number as a position vector in the polar complex plane (default is 'deg').
    
    Returns
    -------
    complex
        * The complex number in Python format which can be used in further calculations.
    
    Examples
    --------
    >>> cnum = cnum(2, 3j) # The complex number is entered as coordinates in the Cartesian complex plane.
    >>> cnum = cnum(2+3j) # The complex number is entered as a polynomial in the Cartesian complex plane.
    >>> cnum = cnum(10, 180) # The complex number is entered as a position vector in the polar complex plane with the angle in degrees.
    >>> cnum = cnum(10, 3.14, 'rad') # The complex number is entered as a position vector in the polar complex plane with the angle in radians.
    """

    # DEFINE AND RETURN THE COMPLEX NUMBER:
    if b is None:
        if isinstance(a, (int, float, complex)):
            # The complex number is entered as a Cartesian polynomial.
            return complex(a)
        else:
            raise TypeError("The polynomial must be of type 'int', 'float' or 'complex'.")
    else:
        if isinstance(a, (int, float)):
            if isinstance(b, complex):
                # The complex number is entered as Cartesian coordinates.
                return complex(a+b)
            elif isinstance(b, (int, float)):
                # The complex number is entered as a position vector in the polar complex plane.
                if unit.lower() == 'deg': 
                    return a*e**(b*(pi/180)*1j)
                elif unit.lower() == 'rad': 
                    return a*e**(b*1j)
                else: 
                    raise ValueError("The angle unit must be defined with either 'deg' or 'rad'.")
            else:
                raise TypeError("The second argument must be of type 'int', 'float' or 'complex'.") 
        else:
            raise TypeError("The first argument must be of type 'int' or 'float'.")


def pol(a:int|float|complex, b:int|float|complex=None, dec:int=0, unit:str='deg') -> str:
    """Returns a complex number as a string with polar angle notation and the angle in degrees.

    The complex number is defined using `a` and/or `b` and can be entered in both the Cartesian and polar complex plane by including or excluding the imaginary unit 'j'.
    
    When entering a complex number in the polar complex plane, the angle unit is degrees by default. This can be changed to radians by passing 'rad' to `unit`.
    
    The number of decimals in the string can be defined using `dec`.

    Parameters
    ----------
    `a` : int | float | complex
        * The real part when entering the complex number as Cartesian coordinates, or

        * both the real and imaginary parts when entering the complex number as a Cartesian polynomial, or

        * the magnitude/modulus when entering the complex number as a position vector in the polar complex plane.

    `b` : int | float | complex, optional
        * The imaginary part, including the imaginary unit, when entering the complex number as Cartesian coordinates, or

        * the number of decimals when entering the complex number as a Cartesian polynomial, or

        * the angle/argument when entering the complex number as a position vector in the polar complex plane (default is None).

    `dec` : int, optional
        * The number of decimals when entering the complex number as a position vector in the polar complex plane (default is 0).

    `unit` : {'deg', 'rad'}, optional
        * The angle unit (degrees or radians) when entering the complex number as a position vector in the polar complex plane (default is 'deg').
    
    Returns
    -------
    str
        * The complex number with polar angle notation and the angle in degrees.
    
    Examples
    --------
    >>> string = pol(2, 3j) # The complex number is entered as coordinates in the Cartesian complex plane with 0 decimals.
    >>> string = pol(2, 3j, 1) # The complex number is entered as coordinates in the Cartesian complex plane with 1 decimal.
    >>> string = pol(2+3j) # The complex number is entered as a polynomial in the Cartesian complex plane with 0 decimals. 
    >>> string = pol(2+3j, 1) # The complex number is entered as a polynomial in the Cartesian complex plane with 1 decimal. 
    >>> string = pol(10, 180) # The complex number is entered as a position vector in the polar complex plane with the angle in degrees and 0 decimals.
    >>> string = pol(10, 180, 1) # The complex number is entered as a position vector in the polar complex plane with the angle in degrees and 1 decimal.
    >>> string = pol(10, 3.14, 0, 'rad') # The complex number is entered as a position vector in the polar complex plane with the angle in radians and 0 decimals.
    """

    # DEFINE THE MAGNITUDE AND ANGLE:
    if isinstance(a, complex):
        # The complex number is entered as a Cartesian polynomial, 
        # which means cnum() does not allow passing any argument to the second parameter.
        mag = abs(a)
        ang = phase(a)*(180/pi) # Angle in degrees.
        if b is not None:
            dec = b # Treat the second argument as the number of decimals.
    else:
        # The complex number is entered as either Cartesian coordinates or a position vector in the polar complex plane.
        mag = abs(cnum(a, b, unit))
        ang = phase(cnum(a, b, unit))*(180/pi) # Angle in degrees.
    
    # RETURN THE COMPLEX NUMBER:
    if isinstance(dec, int):
        if dec >= 0:
            return f"{mag:.{dec}f}{chr(8736)}{ang:.{dec}f}{chr(176)}"
        else:
            raise ValueError("The number of decimals must be defined with a positive integer.")
    else:
        raise TypeError("The number of decimals must be of type 'int'.")


def polprint(a:int|float|complex, b:int|float|complex=None, dec:int=0, unit:str='deg'):
    """Prints a complex number with polar angle notation and the angle in degrees.

    The complex number is defined using `a` and/or `b` and can be entered in both the Cartesian and polar complex plane by including or excluding the imaginary unit 'j'.
    
    When entering a complex number in the polar complex plane, the angle unit is degrees by default. This can be changed to radians by passing 'rad' to `unit`.
    
    The number of decimals when printing can be defined using `dec`.

    Parameters
    ----------
    `a` : int | float | complex
        * The real part when entering the complex number as Cartesian coordinates, or

        * both the real and imaginary parts when entering the complex number as a Cartesian polynomial, or

        * the magnitude/modulus when entering the complex number as a position vector in the polar complex plane.

    `b` : int | float | complex, optional
        * The imaginary part, including the imaginary unit, when entering the complex number as Cartesian coordinates, or

        * the number of decimals when entering the complex number as a Cartesian polynomial, or

        * the angle/argument when entering the complex number as a position vector in the polar complex plane (default is None).

    `dec` : int, optional
        * The number of decimals when entering the complex number as a position vector in the polar complex plane (default is 0).
        
    `unit` : {'deg', 'rad'}, optional
        * The angle unit (degrees or radians) when entering the complex number as a position vector in the polar complex plane (default is 'deg').
    
    Examples
    --------
    >>> polprint(2, 3j) # The complex number is entered as coordinates in the Cartesian complex plane with 0 decimals.
    4∠56°
    >>> polprint(2, 3j, 1) # The complex number is entered as coordinates in the Cartesian complex plane with 1 decimal.
    3.6∠56.3°
    >>> polprint(2+3j) # The complex number is entered as a polynomial in the Cartesian complex plane with 0 decimals.
    4∠56°
    >>> polprint(2+3j, 1) # The complex number is entered as a polynomial in the Cartesian complex plane with 1 decimal. 
    3.6∠56.3°
    >>> polprint(10, 180) # The complex number is entered as a position vector in the polar complex plane with the angle in degrees and 0 decimals.
    10∠180°
    >>> polprint(10, 180, 1) # The complex number is entered as a position vector in the polar complex plane with the angle in degrees and 1 decimal.
    10.0∠180.0°
    >>> polprint(10, 3.14, 0, 'rad') # The complex number is entered as a position vector in the polar complex plane with the angle in radians and 0 decimals.
    10∠180°
    """

    # PRINT THE COMPLEX NUMBER:
    print(pol(a, b, dec, unit))