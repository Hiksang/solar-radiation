# solar-radiation

---

## Installation

```bash
git clone https://github.com/Hiksang/solar-radiation.git
cd solar-radiation
poetry install
```

If you don't have Poetry:

```bash
pip install poetry
```

```bash
pip install solar-radiation
```

---

## Quick Start

```python
from serc.solar_radiation import calculate_extraterrestrial_radiation
import datetime

df = calculate_extraterrestrial_radiation(
    latitude=37.5665,           # Seoul
    longitude=126.9780,
    start_date=datetime.date(2025, 6, 21),
    end_date=datetime.date(2025, 6, 21),
    time_interval="1h",
    timezone="Asia/Seoul",      # IANA timezone name (e.g., "Asia/Seoul", "UTC", "America/New_York")
)

print(df)

```

## Main Functions

calculate_extraterrestrial_radiation
Calculates extraterrestrial solar radiation over user-specified date ranges and intervals.

Parameters:

latitude (float): Latitude of location (degrees)

longitude (float): Longitude of location (degrees)

start_date (datetime.date): Start date

end_date (datetime.date): End date

time_interval (str): Time interval ('1m', '5m', '15m', '30m', '1h', '4h', '12h', '1d')

timezone (str): Timezone in IANA format (e.g., "Asia/Seoul", "UTC")

surface_tilt (float): Surface tilt from horizontal (degrees)

surface_azimuth (float): Surface azimuth (degrees from south)

only_daytime (bool): If True, only returns daytime values

return_Gon (bool): If True, include extraterrestrial normal irradiance (G_on)

return_solar_angles (bool): If True, include solar elevation and azimuth

Returns:

A Pandas DataFrame with:

datetime

G_o (W/m²)

(Optional) G_on (W/m²)

(Optional) solar_elevation (degrees)

(Optional) solar_azimuth (degrees)
