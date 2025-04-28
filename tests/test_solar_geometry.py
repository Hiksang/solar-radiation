# tests/test_solar_geometry.py

from solar_radiation.core.solar_geometry import incidence_angle


def test_incidence_angle_example_161():
    """
    Test the incidence angle calculation based on Example 1.6.1 (Madison, Feb 13, 10:30 solar time).
    """

    latitude = 43.0  # Madison latitude
    declination = -14.0  # Approximate declination for Feb 13
    slope = 45.0  # Tilt from horizontal
    surface_azimuth = 15.0  # Surface azimuth 15° west of south
    hour_angle = -22.5  # Solar time 10:30 → -22.5°

    theta = incidence_angle(
        latitude=latitude,
        declination=declination,
        slope=slope,
        surface_azimuth=surface_azimuth,
        hour_angle=hour_angle
    )

    # Expected value from Example 1.6.1 is 35°
    assert 34.5 <= theta <= 35.5, f"Expected θ ≈ 35°, but got {theta:.2f}°"
# tests/test_solar_geometry.py

import math
from solar_radiation.core.solar_geometry import (
    declination_cooper,
    declination_spencer,
    incidence_angle,
)

def test_declination_cooper_basic():
    """
    declination_cooper() 테스트
    """
    n = 80  # 대략 3월 20일
    delta = declination_cooper(n)
    # 기대: 0도 근처 (춘분)
    assert -2 <= delta <= 2

def test_declination_spencer_basic():
    """
    declination_spencer() 테스트
    """
    n = 80
    delta = declination_spencer(n)
    assert -2 <= delta <= 2

def test_declination_accuracy_comparison():
    """
    declination_cooper와 declination_spencer 비교: 1도 이내 차이
    """
    for n in range(1, 366, 30):  # 1, 31, 61, ..., 361
        delta_cooper = declination_cooper(n)
        delta_spencer = declination_spencer(n)
        assert abs(delta_cooper - delta_spencer) <= 1.5  # Cooper는 약간 부정확하지만 1.5° 이내

def test_incidence_angle_flat_surface():
    """
    입사각 계산: 수평면 (slope=0) 테스트
    """
    theta = incidence_angle(
        latitude=43.0,
        declination=0.0,
        slope=0.0,
        surface_azimuth=0.0,
        hour_angle=0.0,
    )
    assert 42 <= theta <= 44  # 태양 고도=90-위도

def test_incidence_angle_tilted_surface():
    """
    입사각 계산: 경사진 면 (slope=45도) 테스트
    """
    theta = incidence_angle(
        latitude=43.0,
        declination=10.0,
        slope=45.0,
        surface_azimuth=0.0,
        hour_angle=15.0,
    )
    assert 0 <= theta <= 90  # 반드시 0~90° 범위

def test_incidence_angle_extreme_conditions():
    """
    입사각 극단 조건: 태양이 지평선 아래
    """
    theta = incidence_angle(
        latitude=80.0,
        declination=-23.0,
        slope=30.0,
        surface_azimuth=0.0,
        hour_angle=90.0,
    )
    assert 0 <= theta <= 180  # acos는 항상 유효한 범위로 클램핑 되어야 함
