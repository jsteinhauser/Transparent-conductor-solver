# -*- coding: utf-8 -*-

class TClayer:
    """ Transparent Conductive Layer
        Thickness (nm);         Sheet Resistance (Ohms square)
        Resistivity (Ohms.cm);  Conductivity (S)
        Mobility (cm2.V-1.s-1); Carrier density (cm-3)
                                                      """
    
    # Constructors
    def __init__(self, thickness = None,
                 sheetResistance = None,
                 resistivity = None,
                 conductivity = None,
                 mobility = None,
                 carrierDensity = None):

        self.thickness = thickness   
        self.sheetResistance = sheetResistance
        self.resistivity = resistivity
        self.conductivity = conductivity
        self.mobility = mobility
        self.carrierDensity = carrierDensity
        self.msg = ""

    # Getters
    def getThickness(self):
        return self.thickness
    def getSheetResistance(self):
        return self.sheetResistance
    def getResistivity(self):
        return self.resistivity
    def getConductivity(self):
        return conductivity
    def getMobility(self):
        return self.mobility
    def getCarrierDensity(self):
        return self.carrierDensity

    # Setters
    def setThickness(self, newValue):
        self.thickness = newValue
    def setSheetResistance(self, newValue):
        self.sheetResistance = newValue
    def setResistivity(self, newValue):
        self.resistivity = newValue
    def setConductivity(self, newValue):
        self.conductivity = newValue
    def setMobility(self, newValue):
        self.mobility = newValue
    def setCarrierDensity(self, newValue):
        self.carrierDensity = newValue

    # Methods
    def toString(self):
        """ Display the attributes of the TC layer """
        print("Thickness = "+str(self.thickness)+" nm")
        print("Sheet resistance = "+str(self.sheetResistance)+ " Ohms square")
        print("Resistivity = "+str(self.resistivity)+ " Ohms.cm")
        print("Conductivity = "+str(self.conductivity)+ " Siemens")
        print("Mobility = "+str(self.mobility)+ " cm2.V-1.s-1")
        print("Carrier density = "+str(self.carrierDensity)+ " cm-3")
        print(self.msg)

    def clear(self):
        self.setThickness(None)
        self.setSheetResistance(None)
        self.setResistivity(None)
        self.setConductivity(None)
        self.setMobility(None)
        self.setCarrierDensity(None)
        self.msg = ""

    def testConflict (self):
        """ Test conflict between parameters """
        # Too many parameters if 
        #(N.Mu).((d.Rsq)+Sig+Rho)+(d.Rsq).(Sig+Rho)+(Sig.Rho)= True
        if (
            ((self.carrierDensity is not None) & (self.mobility is not None))&
           (((self.thickness is not None) & (self.sheetResistance is not None))|
             (self.conductivity is not None) | (self.resistivity is not None) )|
            ((self.thickness is not None) & (self.sheetResistance is not None))&
            ((self.conductivity is not None) | (self.resistivity is not None)) |
            ((self.conductivity is not None) & (self.resistivity is not None))
            ):
            self.msg = "Too many input parameters\n"
        else:
            self.msg = ""
         
    def solve(self):
        """ Solve missing parameters """

        self.testConflict()
        
        # Solve the resistivity    
        if self.resistivity is None :
            # Calcul from the conductivity
            if self.conductivity is not None :
                self.resistivity = 1 / self.conductivity
            # Calcul from thickness and sheet resistance
            elif (self.thickness is not None) & (self.sheetResistance is not None) :
                self.resistivity = self.sheetResistance * self.thickness * 0.0000001
            # Calcul from mobility and carrier density
            elif (self.mobility is not None) & (self.carrierDensity is not None) :
                self.resistivity = 1 / (self.carrierDensity * self.mobility * 1.602E-19)
            else :
                self.msg = self.msg + "Not enough input data to solve the resistivity\n"

        # Solve the conductivity    
        if self.conductivity is None :
            # Calcul from the resistivity
            if self.resistivity is not None :
                self.conductivity = 1 / self.resistivity
            else :
                self.msg = self.msg + "Not enough input data to solve the conductivity\n"

        # Solve the thickness    
        if self.thickness is None :
            # Calcul from the resistivity and sheet resistance
            if (self.resistivity is not None) & (self.sheetResistance is not None) :
                self.thickness = self.resistivity / (self.sheetResistance * 0.0000001)
            else :
                self.msg = self.msg + "Not enough input data to solve the thickness\n"

        # Solve the sheet resistance    
        if self.sheetResistance is None :
            # Calcul from the resistivity and thickness
            if (self.resistivity is not None) & (self.thickness is not None) :
                self.sheetResistance = self.resistivity / (self.thickness * 0.0000001)
            else :
                self.msg = self.msg + "Not enough input data to solve the sheet resistance\n"

        # Solve the carrier density    
        if self.carrierDensity is None :
            # Calcul from the conductivity and the mobility
            if (self.conductivity is not None) & (self.mobility is not None) :
                self.carrierDensity = self.conductivity / (self.mobility * 1.602E-19)
            else :
                self.msg = self.msg + "Not enough input data to solve the carrier density\n"

        # Solve the mobility    
        if self.mobility is None :
            # Calcul from the conductivity and thecarrier density
            if (self.conductivity is not None) & (self.carrierDensity is not None) :
                self.mobility = self.conductivity / (self.carrierDensity * 1.602E-19)
            else :
                self.msg = self.msg + "Not enough input data to solve the mobility\n"

