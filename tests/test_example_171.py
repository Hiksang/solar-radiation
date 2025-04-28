# tests/test_example_171.py

import math

def test_example_171():
    """
    Example 1.7.1: 입사각, 천정각, 태양 방위각, 경사각, 표면 방위각 계산 테스트
    """

    latitude = math.radians(40.0)
    declination = math.radians(21.0)

    # Part (a)
    omega_a = math.radians(30.0)

    cos_theta_a = math.sqrt(1 - (math.cos(declination) ** 2) * (math.sin(omega_a) ** 2))
    theta_a = math.degrees(math.acos(cos_theta_a))
    assert 27.3 <= theta_a <= 28.3, f"Expected θ ≈ 27.8°, but got {theta_a:.2f}°"

    cos_theta_z_a = math.cos(latitude) * math.cos(declination) * math.cos(omega_a) + math.sin(latitude) * math.sin(declination)
    theta_z_a = math.degrees(math.acos(cos_theta_z_a))
    assert 31.3 <= theta_z_a <= 32.3, f"Expected θz ≈ 31.8°, but got {theta_z_a:.2f}°"

    cos_gamma_s_a = (math.cos(math.radians(theta_z_a)) * math.sin(latitude) - math.sin(declination)) / (math.sin(math.radians(theta_z_a)) * math.cos(latitude))
    cos_gamma_s_a = max(min(cos_gamma_s_a, 1), -1)  # Clamp
    gamma_s_a = math.degrees(math.acos(cos_gamma_s_a))  # omega positive → afternoon
    assert 61.5 <= gamma_s_a <= 63.0, f"Expected γs ≈ 62.3°, but got {gamma_s_a:.2f}°"

    beta_a = math.degrees(math.atan(math.tan(math.radians(theta_z_a)) * abs(math.cos(math.radians(gamma_s_a)))))
    assert 15.5 <= beta_a <= 16.7, f"Expected β ≈ 16.1°, but got {beta_a:.2f}°"

    surface_azimuth_a = 0 if gamma_s_a < 90 else 180
    assert surface_azimuth_a == 0, f"Expected γ = 0°, but got {surface_azimuth_a}"

    # Part (b)
    omega_b = math.radians(100.0)

    cos_theta_b = math.sqrt(1 - (math.cos(declination) ** 2) * (math.sin(omega_b) ** 2))
    theta_b = math.degrees(math.acos(cos_theta_b))
    assert 66.3 <= theta_b <= 67.3, f"Expected θ ≈ 66.8°, but got {theta_b:.2f}°"

    cos_theta_z_b = math.cos(latitude) * math.cos(declination) * math.cos(omega_b) + math.sin(latitude) * math.sin(declination)
    theta_z_b = math.degrees(math.acos(cos_theta_z_b))
    assert 83.4 <= theta_z_b <= 84.4, f"Expected θz ≈ 83.9°, but got {theta_z_b:.2f}°"

    cos_gamma_s_b = (math.cos(math.radians(theta_z_b)) * math.sin(latitude) - math.sin(declination)) / (math.sin(math.radians(theta_z_b)) * math.cos(latitude))
    cos_gamma_s_b = max(min(cos_gamma_s_b, 1), -1)
    gamma_s_b = math.degrees(math.acos(cos_gamma_s_b))
    assert 111.5 <= gamma_s_b <= 113.5, f"Expected γs ≈ 112.4°, but got {gamma_s_b:.2f}°"

    beta_b = math.degrees(math.atan(math.tan(math.radians(theta_z_b)) * abs(math.cos(math.radians(gamma_s_b)))))
    assert 73.5 <= beta_b <= 75.0, f"Expected β ≈ 74.3°, but got {beta_b:.2f}°"

    surface_azimuth_b = 0 if gamma_s_b < 90 else 180
    assert surface_azimuth_b == 180, f"Expected γ = 180°, but got {surface_azimuth_b}"
