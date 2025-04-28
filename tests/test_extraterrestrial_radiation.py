# tests/test_extraterrestrial_radiation.py

import math

from solar_radiation.core.extraterrestrial_radiation import (
    extraterrestrial_normal_irradiance,
    extraterrestrial_horizontal_irradiance,
    hourly_extraterrestrial_radiation,
    daily_extraterrestrial_radiation,
)


def test_extraterrestrial_normal_irradiance():
    n = 1
    Gon_start = extraterrestrial_normal_irradiance(n)
    expected = 1367 * (1 + 0.033 * math.cos(math.radians(360 * n / 365)))
    assert math.isclose(Gon_start, expected, abs_tol=1)

    n = 365
    Gon_end = extraterrestrial_normal_irradiance(n)
    expected = 1367 * (1 + 0.033 * math.cos(math.radians(360 * n / 365)))
    assert math.isclose(Gon_end, expected, abs_tol=1)



def test_extraterrestrial_horizontal_irradiance():
    latitude = 37.5665  # 서울
    n = 172  # 6월 21일
    hour_angle = 0  # 정오
    Go = extraterrestrial_horizontal_irradiance(latitude, n, hour_angle)
    assert Go > 0  # 정오에는 일사량이 양수

    # 밤 시간대 (hour_angle=180) 테스트 → 태양이 지평선 아래
    hour_angle_night = 180
    Go_night = extraterrestrial_horizontal_irradiance(latitude, n, hour_angle_night)
    assert Go_night == 0  # 밤에는 일사량이 0이어야 함


def test_hourly_extraterrestrial_radiation():
    latitude = 37.5665
    n = 172
    omega1 = -7.5  # 오전 11:30
    omega2 = 7.5   # 오후 12:30
    Io = hourly_extraterrestrial_radiation(latitude, n, omega1, omega2)
    assert Io > 0  # 양수여야 한다

    # 이상한 구간 (omega1 > omega2) → Io가 0 또는 매우 작아야 한다
    omega1_invalid = 90
    omega2_invalid = -90
    Io_invalid = hourly_extraterrestrial_radiation(latitude, n, omega1_invalid, omega2_invalid)
    assert Io_invalid < 1e-5  # 거의 0이어야 함


def test_daily_extraterrestrial_radiation():
    latitude = 37.5665
    n = 172
    Ho = daily_extraterrestrial_radiation(latitude, n)
    assert Ho > 0

    # 극단 위도 테스트 (북극) 겨울철이면 Ho가 매우 작아야 함
    arctic_latitude = 80.0
    winter_day = 355  # 12월 21일
    Ho_arctic = daily_extraterrestrial_radiation(arctic_latitude, winter_day)
    assert Ho_arctic < 1e6  # 거의 0에 가까워야 함 (J/m²/day 단위 기준)
