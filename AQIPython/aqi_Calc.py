from .breakPoints import AQI_break
from .paramsCompare import *

def calculate_aqi(Standard:str, pollutant:str, concentration:float, unit:str="microgram")->float:
    """Calculates the AQI for a given standard of pollutant and concentration
    """
    
    if (Standard not in AQI_break.keys()):
        raise UnknownStandardError(Standard)

    if (pollutant not in AQI_break[Standard].keys()):
        raise UnknownPollutantError(pollutant)

    for bp in AQI_break[Standard][pollutant]:
        low_aqi, high_aqi, low_bp, high_bp = bp
        if low_bp <= concentration <= high_bp:
            aqi = ((high_aqi - low_aqi) / (high_bp - low_bp)) * (concentration - low_bp) + low_aqi
            return aqi
        
    return None

print(calculate_aqi('IN', 'CO', 3.5))