from params.breakPoints import AQI_break
from errors.paramsCompare import *

def calculate_aqi(Standard:str, pollutant:str, concentration:float)->float:
    """Exception raised for errors in the input parameters of the function.

    Attributes:
        Standard -- the standard yo be followed for the output
        message -- explanation of the error
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