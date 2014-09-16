TCsolver
========

Transparent conductive layer solver

Calculate the thickness, sheet resistance, resistivity, conductivity, mobility and carrier density of transparent conductive layers. 

Example
'''
Python 3.3.4 (v3.3.4:7ff62415e426, Feb 10 2014, 18:13:51) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> # Instantiate a transparent conductive layer
>>> myLayer = TClayer()
>>> # Set known parameters
>>> myLayer.setThickness(2000)
>>> myLayer.setResistivity(2E-3)
>>> # Solve
>>> myLayer.solve()
>>> # Display
>>> myLayer.toString()
Thickness = 2000 nm
Sheet resistance = 10.000000000000002 Ohms square
Resistivity = 0.002 Ohms.cm
Conductivity = 500.0 Siemens
Mobility = None cm2.V-1.s-1
Carrier density = None cm-3
Not enough input data to solve the carrier density
Not enough input data to solve the mobility
'''
>>> 
