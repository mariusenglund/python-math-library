# cmath-extras
A package of [functions](#function-list) to deal with complex numbers in Python more efficiently. The package is especially intended for use with electrical circuits.


## Background
What would you do if you were told to use Python to calculate the magnitude and phase angle of the voltage $V$ over a RLC branch given the current $I\angle\phi\degree$?

While it's not *hard* doing calculations like these, they do have the potencial of getting quite messy within a script. Especially when working with bigger circuits.

As we know, the voltage over a RLC branch can be found using the following equation:

$$ {{V} = ({R}+{j(X_{L}-X_{C})})*{I}\angle\phi\degree} $$

With the `cmath-extras` module installed, calculations with complex numbers can be done easily using an [one and only function](#cnum):
```
from cmath_extras import *

V = cnum(R+(XL-XC)j)*cnum(I, phi)   # cnum() takes care of the complex conversion.
polprint(V, 2)                      # While polprint() outputs the result in a pretty manner (here with 2 decimals).
```
The code above could output something like this if all parameters was defined:
```
123.45∠43.21°
```


## Installation
The package can be installed using [pip](https://pip.pypa.io/en/stable/installation/#). However, since this project is not yet hosted at [PyPI](https://pypi.org/), *[git](https://git-scm.com/download) is also required for the installation*.
```
$ pip3 install 'git+https://github.com/mariusenglund/python-math-library.git#egg=cmath-extras&subdirectory=cmath-extras'
```


## Usage
After you have successfully installed the package, all functions in the `cmath-extras` module can be made available within a script by importing them:
```
from cmath_extras import *
```
You can then call any function in the module directly by [it's name](#function-list).


## Function list
### cnum()
Returns a complex number which can be used in further calculations.

#### Parameters
`a` : int | float | complex
* The real part when entering the complex number as Cartesian coordinates, or
* both the real and imaginary parts when entering the complex number as a Cartesian polynomial, or
* the magnitude/modulus when entering the complex number as a position vector in the polar complex plane.
    
`b` : int | float | complex, optional
* The imaginary part, including the imaginary unit, when entering the complex number as Cartesian coordinates, or
* the angle/argument when entering the complex number as a position vector in the polar complex plane (default is None).
    
`unit` : {'deg', 'rad'}, optional
* The angle unit (degrees or radians) when entering the complex number as a position vector in the polar complex plane (default is 'deg').

#### Usage
The complex number is defined using `a` and/or `b` and can be entered in both the Cartesian and polar complex plane by including or excluding the imaginary unit 'j'.
    
When entering a complex number in the polar complex plane, the angle unit is degrees by default. This can be changed to radians by passing 'rad' to `unit`.

#### Examples
```
>>> cnum = cnum(2, 3j) # The complex number is entered as coordinates in the Cartesian complex plane.
>>> cnum = cnum(2+3j) # The complex number is entered as a polynomial in the Cartesian complex plane.
>>> cnum = cnum(10, 180) # The complex number is entered as a position vector in the polar complex plane with the angle in degrees.
>>> cnum = cnum(10, 3.14, 'rad') # The complex number is entered as a position vector in the polar complex plane with the angle in radians.
```

### pol()
Returns a complex number as a string with polar angle notation and the angle in degrees.

#### Parameters
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

#### Usage
The complex number is defined using `a` and/or `b` and can be entered in both the Cartesian and polar complex plane by including or excluding the imaginary unit 'j'.
    
When entering a complex number in the polar complex plane, the angle unit is degrees by default. This can be changed to radians by passing 'rad' to `unit`.
    
The number of decimals in the string can be defined using `dec`.

#### Examples
```
>>> string = pol(2, 3j) # The complex number is entered as coordinates in the Cartesian complex plane with 0 decimals.
>>> string = pol(2, 3j, 1) # The complex number is entered as coordinates in the Cartesian complex plane with 1 decimal.
>>> string = pol(2+3j) # The complex number is entered as a polynomial in the Cartesian complex plane with 0 decimals. 
>>> string = pol(2+3j, 1) # The complex number is entered as a polynomial in the Cartesian complex plane with 1 decimal. 
>>> string = pol(10, 180) # The complex number is entered as a position vector in the polar complex plane with the angle in degrees and 0 decimals.
>>> string = pol(10, 180, 1) # The complex number is entered as a position vector in the polar complex plane with the angle in degrees and 1 decimal.
>>> string = pol(10, 3.14, 0, 'rad') # The complex number is entered as a position vector in the polar complex plane with the angle in radians and 0 decimals.
```

### polprint()
Prints a complex number with polar angle notation and the angle in degrees.

#### Parameters
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

#### Usage
The complex number is defined using `a` and/or `b` and can be entered in both the Cartesian and polar complex plane by including or excluding the imaginary unit 'j'.
    
When entering a complex number in the polar complex plane, the angle unit is degrees by default. This can be changed to radians by passing 'rad' to `unit`.
    
The number of decimals when printing can be defined using `dec`.

#### Examples
```
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
```