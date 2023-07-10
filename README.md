# AQIPython
## Description
AQIPython is a Python module that calculates the Air Quality Index (AQI) for various air pollutants based on different standards. The module takes pollutant concentration values in parts per million (PPM), milligrams per cubic meter (mg/m³), and micrograms per cubic meter (µg/m³) and provides the corresponding AQI value.

## Installation
To install AQIPython, you can use pip, the Python package manager. Open your terminal or command prompt and run the following command:
```shell:
pip install AQIPython
```
## Usage
Here's an example of how to use AQIPython to calculate the AQI for different pollutants:
```python:
from AQIPython import calculate_aqi

AQI = calculate_aqi('IN', 'CO', 3.5, "ug/m3")
print(AQi)
```
Make sure to replace the country code, pollutant code, concentration value, and unit with your actual data. The calculate_aqi() function takes four arguments: the country code (e.g., 'IN' for India), pollutant code (e.g., 'CO' for carbon monoxide), concentration value, and concentration unit (e.g., 'ug/m3' for micrograms per cubic meter).

## Supported Pollutants

AQIPython supports the following pollutants for calculating AQI:

- *PM25*  (particulate matter with a diameter of 2.5 micrometers or  less)
- *PM10* (particulate matter with a diameter of 10 micrometers or less)
- *NO2* (nitrogen dioxide)
- *SO2* (sulfur dioxide)
- *CO* (carbon monoxide)
- *O3* (ozone)
- *PB* (Lead)** (Not for US)

## Supported Standards
AQIPython supports the following Standards for calculating AQI:

- IN (India)
- US (United States of America)

## Contributing
If you'd like to contribute to AQIPython, please take a look at [Contributing Guidelines](https://github.com/Spritan/AQIPython/blob/main/CONTRIBUTING.md).

## Author
- [@Spritan](https://github.com/Spritan)
- [@dev-rajk](https://github.com/dev-rajk)


## Changelog

### [1.0.0] - 2023-07-10
- Initial release of AQIPython.
- Support for Indian and US standard AQI calculation.
- Calculate AQI for PM2.5, PM10, NO2, SO2, CO, and O3 pollutants.
- Provide function calculate_aqi() to calculate AQI based on pollutant concentrations.

## License
This module is released under the MIT License.
