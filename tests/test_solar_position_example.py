# tests/test_solar_position_example.py

import math

def test_example_162_zenith_and_azimuth():
    """
    Example 1.6.2 태양 천정각(zenith)과 방위각(azimuth) 계산 테스트
    """

    # 공통 조건
    latitude = math.radians(43.0)  # 위도 43°, radian 변환

    # a. 2월 13일 9:30 AM (n=44)
    declination_a = math.radians(-14.0)
    hour_angle_a = math.radians(-37.5)

    cos_theta_z_a = math.sin(latitude) * math.sin(declination_a) + math.cos(latitude) * math.cos(declination_a) * math.cos(hour_angle_a)
    theta_z_a = math.degrees(math.acos(cos_theta_z_a))

    # Solar Azimuth (γs)
    numerator_a = math.cos(math.radians(theta_z_a)) * math.sin(latitude) - math.sin(declination_a)
    denominator_a = math.sin(math.radians(theta_z_a)) * math.cos(latitude)
    cos_azimuth_a = numerator_a / denominator_a
    azimuth_a = -math.degrees(math.acos(max(min(cos_azimuth_a, 1), -1)))  # 오전이므로 부호 -

    assert 66.0 <= theta_z_a <= 67.0, f"Expected θz ≈ 66.5°, but got {theta_z_a:.2f}°"
    assert -41.0 <= azimuth_a <= -39.0, f"Expected γs ≈ -40°, but got {azimuth_a:.2f}°"

    # b. 7월 1일 6:30 PM (n=182)
    declination_b = math.radians(23.1)
    hour_angle_b = math.radians(97.5)

    cos_theta_z_b = math.sin(latitude) * math.sin(declination_b) + math.cos(latitude) * math.cos(declination_b) * math.cos(hour_angle_b)
    theta_z_b = math.degrees(math.acos(cos_theta_z_b))

    numerator_b = math.cos(math.radians(theta_z_b)) * math.sin(latitude) - math.sin(declination_b)
    denominator_b = math.sin(math.radians(theta_z_b)) * math.cos(latitude)
    cos_azimuth_b = numerator_b / denominator_b
    azimuth_b = math.degrees(math.acos(max(min(cos_azimuth_b, 1), -1)))  # 오후이므로 부호 +

    assert 79.0 <= theta_z_b <= 80.0, f"Expected θz ≈ 79.6°, but got {theta_z_b:.2f}°"
    assert 111.0 <= azimuth_b <= 113.0, f"Expected γs ≈ 112°, but got {azimuth_b:.2f}°"
