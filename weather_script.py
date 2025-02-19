# openweather api로 요청을 해서
# 그 결과를 csv로 저장하는 파이썬 파일
import requests
import csv
from datetime import datetime
import os

CITY = "Seoul"
API_KEY = os.getenv("OPENWEATHER_API_KEY")
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()
temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]
print(temp, humidity, description)
timezone = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 위의 4개의 데이터를 가지는 csv 파일 생성
csv_filename = "seoul_weather.csv"
header = ["timezone", "temp", "humidity", "description"]

# csv가 존재하면 True
# 존재하지 않으면 False 반환
file_exist = os.path.isfile(csv_filename)

# mode = "a" 일 때-> if not is file -> create
#                 -> if is file -> write
with open(csv_filename, "a", newline="") as file:
    writer = csv.writer(file)

    # 파일이 존재하지 않으면 -> 헤더를 작성
    if not file_exist:
        writer.writerow(header)

    writer.writerow([timezone, temp, humidity, description])
    
    print("csv 저장 완료")
