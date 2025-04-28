# tests/test_incidence_angle_example.py

import math
from solar_radiation.core.solar_geometry import incidence_angle

def test_example_161_incidence_angle():
    """
    Example 1.6.1 입사각 계산 테스트 (Madison, Feb 13, 10:30 solar time)
    """

    latitude = 43.0  # Madison 위도
    declination = -14.0  # 2월 13일 declination
    slope = 45.0  # Surface Tilt
    surface_azimuth = 15.0  # Surface Azimuth (남쪽 기준 서쪽 15도)
    hour_angle = -22.5  # Solar Time 10:30 → ω = -22.5°

    theta = incidence_angle(
        latitude=latitude,
        declination=declination,
        slope=slope,
        surface_azimuth=surface_azimuth,
        hour_angle=hour_angle
    )

    # 기대값은 θ ≈ 35°
    assert 34.5 <= theta <= 35.5, f"Expected θ ≈ 35°, but got {theta:.2f}°"
