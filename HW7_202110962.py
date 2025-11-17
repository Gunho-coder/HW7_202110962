import requests
import json

# ✔ 본인 서비스키로 변경해야 함
SERVICE_KEY = "bac69055b2df789699e37e6353d7c0a5b8801cd0749166c643e02e735a3da94f"

def get_weather(start_dt, start_hh, end_dt, end_hh, stn=108):
    url = "http://apis.data.go.kr/1360000/AsosHourlyInfoService/getWthrDataList"

    params = {
        "serviceKey": SERVICE_KEY,
        "numOfRows": 999,
        "pageNo": 1,
        "dataType": "JSON",
        "dataCd": "ASOS",
        "dateCd": "HR",
        "startDt": start_dt,
        "startHh": start_hh,
        "endDt": end_dt,
        "endHh": end_hh,
        "stnIds": stn,
    }

    response = requests.get(url, params=params)
    return response.json()

# -----------------------------------------------
# ① 2024-12-04 (15~18시)
data1 = get_weather("20241204", "15", "20241204", "18")

# ② 2025-06-04 (12~16시)
data2 = get_weather("20250604", "12", "20250604", "16")

# 결과 출력
print("\n=== 2024년 12월 04일 15~18시 ===")
print(json.dumps(data1, indent=2, ensure_ascii=False))

print("\n=== 2025년 06월 04일 12~16시 ===")
print(json.dumps(data2, indent=2, ensure_ascii=False))
