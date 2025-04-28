# tests/test_utils.py

import datetime
import math
from solar_radiation.core.utils import (
    day_of_year,
    is_leap_year,
    day_of_year_from_month_day,
    equation_of_time,
    hour_angle,
    solar_time,
    sunrise_sunset_hour_angle,
    minutes_to_time,
    time_to_minutes,
)

def test_day_of_year():
    assert day_of_year(datetime.date(2024, 1, 1)) == 1
    assert day_of_year(datetime.date(2024, 12, 31)) == 366  # 2024년은 윤년
    assert day_of_year(datetime.date(2023, 12, 31)) == 365

def test_is_leap_year():
    assert is_leap_year(2024) is True
    assert is_leap_year(2023) is False
    assert is_leap_year(2000) is True
    assert is_leap_year(1900) is False  # 100년 단위 윤년 예외 처리

def test_day_of_year_from_month_day():
    assert day_of_year_from_month_day(1, 1, 2024) == 1
    assert day_of_year_from_month_day(12, 31, 2024) == 366

def test_equation_of_time():
    n = 80  # 약 3월 20일
    eot = equation_of_time(n)
    assert -15 <= eot <= 15  # 대략적인 범위

def test_hour_angle():
    dt = datetime.datetime(2024, 4, 15, 12, 0)
    omega = hour_angle(dt, longitude=0.0, timezone=0)
    assert -1 <= omega <= 1  # 정오 기준 시간각은 거의 0도

def test_solar_time():
    dt = datetime.datetime(2024, 4, 15, 12, 0)
    solar_dt = solar_time(dt, longitude=0.0, timezone=0, n=105)
    assert 11 <= solar_dt.hour <= 13  # 거의 정오

def test_sunrise_sunset_hour_angle():
    omega_s = sunrise_sunset_hour_angle(latitude=43.0, declination=9.4)
    assert 80 <= omega_s <= 100  # plausible range

def test_minutes_to_time():
    t = minutes_to_time(90)  # 1시간 30분
    assert t.hour == 1
    assert t.minute == 30
    assert t.second == 0

def test_time_to_minutes():
    t = datetime.time(hour=1, minute=30, second=0)
    minutes = time_to_minutes(t)
    assert 89 <= minutes <= 91  # float 소수점 오차 허용
