# tests/test_example_1102.py

import math

def test_example_1102():
    """
    Example 1.10.2: 시간 간격 (10시–11시) 동안의 외기권 일사량 I₀ 계산 테스트
    """

    # Constants
    latitude = math.radians(43.0)
    declination = math.radians(9.4)
    G_sc = 1367  # Solar constant (W/m²)
    n = 105  # Day of year

    omega1 = math.radians(-30.0)  # ω₁ = -30°
    omega2 = math.radians(-15.0)  # ω₂ = -15°

    dr = 1 + 0.033 * math.cos(math.radians(360 * n / 365))  # eccentricity correction

    Io = (12 * 3600 / math.pi) * G_sc * dr * (
        math.cos(latitude) * math.cos(declination) * (math.sin(omega2) - math.sin(omega1))
        + (math.pi * (math.degrees(omega2) - math.degrees(omega1)) / 180) * math.sin(latitude) * math.sin(declination)
    )

    Io_MJ = Io / 1e6  # W⋅s/m² → MJ/m²

    assert 3.74 <= Io_MJ <= 3.84, f"Expected I₀ ≈ 3.79 MJ/m², but got {Io_MJ:.2f} MJ/m²"
