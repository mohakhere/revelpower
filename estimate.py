import pandas as pd
import pvlib
from pvlib import solarposition, irradiance

def calculate_ghi(latitude, longitude, date, tilt, azimuth):
    times = pd.date_range(date, periods=24, freq='H')

    solar_position = solarposition.get_solarposition(times, latitude, longitude)

    clearsky = irradiance.clearsky(times, solar_position['apparent_elevation'])

    ghi = irradiance.get_total_irradiance(tilt, azimuth, solar_position['apparent_zenith'],
                                           solar_position['azimuth'], dni=clearsky['dni'], ghi=clearsky['ghi'])

    return ghi['ghi'].sum()

if __name__ == "__main__":
    latitude = 37.7749 
    longitude = -122.4194 
    date = '2023-06-21' 
    tilt = 30 
    azimuth = 180 

    total_ghi = calculate_ghi(latitude, longitude, date, tilt, azimuth)
    print(f'Total GHI for the given location and date: {total_ghi:.2f} Wh/m^2')
