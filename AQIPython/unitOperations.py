unitsSupported = ['ppm', 'ug/m3', 'mg/m3']

def ppmTOug(concentration:float, pollutant:str)->float:
    if (pollutant == "NH3"):
        concentration = concentration*696.208
    elif pollutant == "CO":
        concentration = concentration*1145.085
    elif pollutant == "NO2":
        concentration = concentration*1880.948
    elif pollutant == "SO2":
        concentration = concentration*2619.264
    elif pollutant == "O3":
        concentration = concentration*1962.302
    elif pollutant == "PB":
        concentration = concentration*8474.437
    return concentration
    
def mgTOug(concentration:float)->float:
    return concentration*1000