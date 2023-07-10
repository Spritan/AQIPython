from .breakPoints import AQI_break
from .unitOperations import unitsSupported,ppmTOug
from .errorCustom import *

def calculate_aqi(Standard:str, pollutant:str, concentration:float, unit:str="ug/m3")->float:
    """Calculates the AQI for a given standard of pollutant and concentration
    """
    if (Standard not in AQI_break.keys()):
        raise UnknownStandardError(Standard)

    if (pollutant not in AQI_break[Standard].keys()):
        raise UnknownPollutantError(pollutant)

    if (unit != "ug/m3"):
        if (unit not in unitsSupported):
            raise UnSupportedUnitError(unit)
        elif (unit == "ppm"):
            concentration = ppmTOug(concentration, pollutant)
        elif (unit == "mg/m3"):
            concentration = ppmTOug(concentration, pollutant)
                 
    for bp in AQI_break[Standard][pollutant]:
        low_aqi, high_aqi, low_bp, high_bp = bp
        if low_bp <= concentration <= high_bp:
            aqi = ((high_aqi - low_aqi) / (high_bp - low_bp)) * (concentration - low_bp) + low_aqi
            return aqi
    
    return None