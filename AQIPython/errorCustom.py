class UnknownStandardError(Exception):
    """Exception raised for errors in the input parameters of the function.

    Attributes:
        Standard -- the standard yo be followed for the output
        message -- explanation of the error
    """

    def __init__(self, Standard ):
        self.Standard = Standard
        self.message = f"The entered Stnadard \"{self.Standard}\" is not supported. "
        super().__init__(self.message)
        
class UnknownPollutantError(Exception):
    """Exception raised for errors in the input parameters of the function.

    Attributes:
        Standard -- the standard yo be followed for the output
        message -- explanation of the error
    """

    def __init__(self, Pollutant ):
        self.Pollutant = Pollutant
        self.message = f"The entered Pollutant \"{self.Pollutant}\" is not supported. "
        super().__init__(self.message)
        
class UnSupportedUnitError(Exception):
    """The unit specified is not supported. please convert to ppm, mg/m3, ug/m3

    Attributes:
        unit -- the unit yo be followed for the output
        message -- explanation of the error
    """

    def __init__(self, unit ):
        self.unit = unit
        self.message = f"The entered unit \"{self.unit}\" is not supported. Please convert to ppm, mg/m3, ug/m3 "
        super().__init__(self.message)