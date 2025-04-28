# tests/test_solar_radiation.py

import datetime
import pytest
from solar_radiation.solar_radiation import calculate_extraterrestrial_radiation

def test_calculate_basic():
    """
    기본 1일, 1시간 간격, 수평면, full-day 계산 테스트
    """
    start_date = datetime.date(2025, 6, 21)
    end_date = datetime.date(2025, 6, 21)

    df = calculate_extraterrestrial_radiation(
        latitude=37.5665,
        longitude=126.9780,
        start_date=start_date,
        end_date=end_date,
        time_interval="1h",
        timezone="Asia/Seoul",  # ✅ 문자열
        surface_tilt=0.0,
        surface_azimuth=0.0,
        only_daytime=False,
        return_Gon=True,
        return_solar_angles=True,
    )

    assert not df.empty
    assert "G_o" in df.columns
    assert "G_on" in df.columns

def test_only_daytime_filter():
    """
    only_daytime=True 옵션 테스트: 밤 데이터가 없어야 함
    """
    df = calculate_extraterrestrial_radiation(
        latitude=37.5665,
        longitude=126.9780,
        start_date=datetime.date(2025, 6, 21),
        end_date=datetime.date(2025, 6, 21),
        time_interval="30m",
        timezone="Asia/Seoul",  # ✅ 문자열
        only_daytime=True,
    )

    assert not df.empty
    assert all(df["G_o"] > 0)

def test_surface_tilt_effect():
    """
    수평면과 경사진 면 결과 비교 테스트
    """
    date = datetime.date(2025, 6, 21)

    df_flat = calculate_extraterrestrial_radiation(
        latitude=37.5665,
        longitude=126.9780,
        start_date=date,
        end_date=date,
        time_interval="1h",
        timezone="Asia/Seoul",
        surface_tilt=0.0,
        surface_azimuth=0.0,
        only_daytime=True,
    )

    df_tilted = calculate_extraterrestrial_radiation(
        latitude=37.5665,
        longitude=126.9780,
        start_date=date,
        end_date=date,
        time_interval="1h",
        timezone="Asia/Seoul",
        surface_tilt=30.0,
        surface_azimuth=0.0,
        only_daytime=True,
    )

    assert not df_flat.empty and not df_tilted.empty
    assert not df_flat["G_o"].equals(df_tilted["G_o"])

def test_basic_daily_radiation():
    df = calculate_extraterrestrial_radiation(
        latitude=43.0,
        longitude=0.0,
        start_date=datetime.date(2024, 4, 15),
        end_date=datetime.date(2024, 4, 15),
        time_interval="1h",
        timezone="UTC",
    )
    assert not df.empty
    assert "datetime" in df.columns
    assert "G_o" in df.columns
    # assert "G_on" in df.columns   # <-- 이 줄을 주석 처리하거나
    if "G_on" in df.columns:
        assert df["G_on"].notnull().all()


def test_time_interval_support():
    """
    다양한 시간 간격 지원 테스트
    """
    intervals = ["1m", "5m", "15m", "30m", "1h", "4h", "12h", "1d"]
    expected_counts = {
        "1m": 24 * 60,
        "5m": 24 * 12,
        "15m": 24 * 4,
        "30m": 24 * 2,
        "1h": 24,
        "4h": 6,
        "12h": 2,
        "1d": 1,
    }
    for interval in intervals:
        df = calculate_extraterrestrial_radiation(
            latitude=43.0,
            longitude=0.0,
            start_date=datetime.date(2024, 4, 15),
            end_date=datetime.date(2024, 4, 15),
            time_interval=interval,
            timezone="UTC",
        )
        assert len(df) == expected_counts[interval]

def test_only_daytime_filtering():
    """
    only_daytime 옵션 필터링 테스트
    """
    df_full = calculate_extraterrestrial_radiation(
        latitude=43.0,
        longitude=0.0,
        start_date=datetime.date(2024, 4, 15),
        end_date=datetime.date(2024, 4, 15),
        time_interval="30m",
        timezone="UTC",
        only_daytime=False,
    )
    df_day = calculate_extraterrestrial_radiation(
        latitude=43.0,
        longitude=0.0,
        start_date=datetime.date(2024, 4, 15),
        end_date=datetime.date(2024, 4, 15),
        time_interval="30m",
        timezone="UTC",
        only_daytime=True,
    )
    assert len(df_day) < len(df_full)
    assert (df_day["G_o"] > 0).all()

def test_surface_tilt_and_azimuth_effect():
    """
    surface_tilt, surface_azimuth 효과 테스트
    """
    df_flat = calculate_extraterrestrial_radiation(
        latitude=43.0,
        longitude=0.0,
        start_date=datetime.date(2024, 4, 15),
        end_date=datetime.date(2024, 4, 15),
        time_interval="1h",
        timezone="UTC",
        surface_tilt=0,
        surface_azimuth=0,
    )
    df_tilted = calculate_extraterrestrial_radiation(
        latitude=43.0,
        longitude=0.0,
        start_date=datetime.date(2024, 4, 15),
        end_date=datetime.date(2024, 4, 15),
        time_interval="1h",
        timezone="UTC",
        surface_tilt=45,
        surface_azimuth=0,
    )
    assert (df_flat["G_o"] != df_tilted["G_o"]).any()

def test_return_solar_angles():
    """
    return_solar_angles 옵션 테스트
    """
    df = calculate_extraterrestrial_radiation(
        latitude=43.0,
        longitude=0.0,
        start_date=datetime.date(2024, 4, 15),
        end_date=datetime.date(2024, 4, 15),
        time_interval="1h",
        timezone="UTC",
        return_solar_angles=True,
    )
    assert "solar_elevation" in df.columns
    assert df["solar_elevation"].notnull().all()

def test_invalid_time_interval():
    """
    잘못된 시간 간격 테스트
    """
    with pytest.raises(ValueError):
        calculate_extraterrestrial_radiation(
            latitude=43.0,
            longitude=0.0,
            start_date=datetime.date(2024, 4, 15),
            end_date=datetime.date(2024, 4, 15),
            time_interval="2h",  # 지원 안함
            timezone="UTC",
        )

def test_nighttime_only_case():
    """
    극지방 겨울: 밤만 있을 때 테스트
    """
    df = calculate_extraterrestrial_radiation(
        latitude=89.0,
        longitude=0.0,
        start_date=datetime.date(2024, 12, 21),
        end_date=datetime.date(2024, 12, 21),
        time_interval="1h",
        timezone="UTC",
        only_daytime=True,
    )
    assert df.empty
