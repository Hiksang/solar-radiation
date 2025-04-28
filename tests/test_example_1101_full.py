# tests/test_example_1101_full.py

import math

def test_example_1101_full():
    """
    Example 1.10.1: Sunset hour angle ωₛ, 그리고 H₀ (일평균 외기권 일사량) 계산 테스트
    """

    # Constants
    latitude = math.radians(43.0)
    declination = math.radians(9.4)
    G_sc = 1367  # Solar constant (W/m²)
    n = 105  # Day of year (April 15)

    # 1. Sunset hour angle ωₛ
    cos_omega_s = -math.tan(latitude) * math.tan(declination)
    cos_omega_s = max(min(cos_omega_s, 1), -1)  # Clamp
    omega_s = math.degrees(math.acos(cos_omega_s))
    assert 98.4 <= omega_s <= 99.4, f"Expected ωₛ ≈ 98.9°, but got {omega_s:.2f}°"

    # 2. Day extraterrestrial radiation H₀ (in MJ/m²)
    dr = 1 + 0.033 * math.cos(math.radians(360 * n / 365))  # eccentricity correction
    Ho = (24 * 3600 / math.pi) * G_sc * dr * (
        math.cos(latitude) * math.cos(declination) * math.sin(math.radians(omega_s))
        + (math.pi * omega_s / 180) * math.sin(latitude) * math.sin(declination)
    )

    Ho_MJ = Ho / 1e6  # W⋅s/m² → MJ/m²

    assert 33.3 <= Ho_MJ <= 34.3, f"Expected H₀ ≈ 33.8 MJ/m², but got {Ho_MJ:.2f} MJ/m²"
