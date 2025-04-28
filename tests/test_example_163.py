# tests/test_example_163.py

import math

def test_example_163():
    """
    Example 1.6.3: 일출/일몰 시간각, 태양 고도, 천정각, 방위각, 프로파일 각도 테스트
    """

    latitude = math.radians(43.0)
    declination = math.radians(-2.4)
    surface_azimuth = math.radians(25.0)  # 표면 방위각 (서쪽으로 25도)
    omega_at_time = math.radians(60.0)

    # 1. Sunset hour angle (ωₛ)
    omega_sunset = math.degrees(math.acos(-math.tan(latitude) * math.tan(declination)))
    assert 87.5 <= omega_sunset <= 88.1, f"Expected ωₛ ≈ 87.8°, but got {omega_sunset:.2f}°"

    # 2. Solar altitude αₛ at 4:00 PM
    sin_alpha_s = (math.sin(latitude) * math.sin(declination)) + (math.cos(latitude) * math.cos(declination) * math.cos(omega_at_time))
    alpha_s = math.degrees(math.asin(sin_alpha_s))
    assert 19.2 <= alpha_s <= 20.2, f"Expected αₛ ≈ 19.7°, but got {alpha_s:.2f}°"

    # 3. Zenith angle θz
    theta_z = 90 - alpha_s
    assert 70.0 <= theta_z <= 71.0, f"Expected θz ≈ 70.3°, but got {theta_z:.2f}°"

    # 4. Solar azimuth γₛ
    cos_gamma_s = (math.cos(math.radians(theta_z)) * math.sin(latitude) - math.sin(declination)) / (math.sin(math.radians(theta_z)) * math.cos(latitude))
    cos_gamma_s = max(min(cos_gamma_s, 1), -1)  # clamp
    gamma_s = math.degrees(math.acos(cos_gamma_s))  # sign(omega) positive (afternoon)
    assert 65.0 <= gamma_s <= 68.0, f"Expected γₛ ≈ 66.8°, but got {gamma_s:.2f}°"

    # 5. Profile angle αp (최종 수정 공식)
    cos_component = math.cos(math.radians(gamma_s) - surface_azimuth)
    alpha_p = math.degrees(math.atan(math.tan(math.radians(alpha_s)) / cos_component))
    assert 25.0 <= alpha_p <= 26.5, f"Expected αp ≈ 25.7°, but got {alpha_p:.2f}°"
