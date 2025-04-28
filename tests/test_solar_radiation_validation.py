# tests/test_solar_radiation_validation.py

import datetime
import pytest
from solar_radiation.solar_radiation import calculate_extraterrestrial_radiation

def test_invalid_start_end_date():
    """
    start_date가 end_date 이후일 때 ValueError 발생해야 한다.
    """
    with pytest.raises(ValueError):
        calculate_extraterrestrial_radiation(
            latitude=0,
            longitude=0,
            start_date=datetime.date(2024, 5, 1),
            end_date=datetime.date(2024, 4, 1),
        )

def test_invalid_latitude():
    """
    latitude 범위 벗어났을 때 ValueError 발생
    """
    with pytest.raises(ValueError):
        calculate_extraterrestrial_radiation(
            latitude=100,
            longitude=0,
            start_date=datetime.date(2024, 4, 1),
            end_date=datetime.date(2024, 4, 2),
        )

def test_invalid_longitude():
    """
    longitude 범위 벗어났을 때 ValueError 발생
    """
    with pytest.raises(ValueError):
        calculate_extraterrestrial_radiation(
            latitude=0,
            longitude=200,
            start_date=datetime.date(2024, 4, 1),
            end_date=datetime.date(2024, 4, 2),
        )

def test_invalid_surface_tilt():
    """
    surface_tilt 범위 벗어났을 때 ValueError 발생
    """
    with pytest.raises(ValueError):
        calculate_extraterrestrial_radiation(
            latitude=0,
            longitude=0,
            start_date=datetime.date(2024, 4, 1),
            end_date=datetime.date(2024, 4, 2),
            surface_tilt=200,
        )

def test_invalid_surface_azimuth():
    """
    surface_azimuth 범위 벗어났을 때 ValueError 발생
    """
    with pytest.raises(ValueError):
        calculate_extraterrestrial_radiation(
            latitude=0,
            longitude=0,
            start_date=datetime.date(2024, 4, 1),
            end_date=datetime.date(2024, 4, 2),
            surface_azimuth=300,
        )

def test_polar_night_condition():
    """
    극지방 겨울: 태양이 뜨지 않아야 하고 결과가 empty
    """
    df = calculate_extraterrestrial_radiation(
        latitude=89.0,
        longitude=0.0,
        start_date=datetime.date(2024, 12, 21),
        end_date=datetime.date(2024, 12, 21),
        time_interval="1h",
        timezone="UTC",  # ✅ 수정
        only_daytime=True,
    )
    assert df.empty

def test_vertical_surface_tilt():
    """
    surface_tilt가 90도 (수직)일 때에도 G_o 계산이 정상 동작하는지 확인
    """
    df = calculate_extraterrestrial_radiation(
        latitude=43.0,
        longitude=0.0,
        start_date=datetime.date(2024, 4, 15),
        end_date=datetime.date(2024, 4, 15),
        time_interval="1h",
        surface_tilt=90,
        surface_azimuth=0,
        timezone="UTC",  # ✅ 수정
    )
    assert not df.empty
    assert "G_o" in df.columns
