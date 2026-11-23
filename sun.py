import pandas as pd
from pvlib import solarposition

# Example coordinates for central London
latitude = 51.5074
longitude = -0.1278

# Historical timestamp in UTC
time = pd.DatetimeIndex(
    ["1995-06-21 14:00"],
    tz="UTC"
)

sun = solarposition.get_solarposition(
    time,
    latitude,
    longitude
)

print("Elevation:", sun["apparent_elevation"].iloc[0])
print("Azimuth:", sun["azimuth"].iloc[0])
