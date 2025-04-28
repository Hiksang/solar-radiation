# examples/example_basic_usage.py

from solar_radiation.solar_radiation import calculate_extraterrestrial_radiation
import datetime

# 대한민국 서울 기준 (Asia/Seoul), 2024년 4월 28일, 1시간 간격으로 계산
df = calculate_extraterrestrial_radiation(
    latitude=70.5,
    longitude=127.0,
    start_date=datetime.date(2024, 4, 28),
    end_date=datetime.date(2024, 4, 28),
    time_interval="1h",
    timezone="Asia/Seoul",  # ✅ 표준 문자열 기반 timezone 지정
    surface_tilt=0.0,       # 수평면 기준
    surface_azimuth=0.0,    # 남향
    only_daytime=True,      # 밤시간 제거
    return_Gon=True,        # G_on도 출력
    return_solar_angles=True,  # Solar Elevation 출력
)

# 결과 출력
print(df)
print("  ")

df = calculate_extraterrestrial_radiation(
    latitude=37.5,
    longitude=127.0,
    start_date=datetime.date(2024, 4, 28),
    end_date=datetime.date(2024, 4, 28),
    time_interval="1h",
    timezone="Asia/Seoul",  # ✅ 표준 문자열 기반 timezone 지정
)

# 결과 출력
print(df)