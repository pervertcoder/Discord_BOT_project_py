import requests
import os
from dotenv import load_dotenv
load_dotenv()

CWB_API_KEY = os.getenv("CWB_API_KEY")
url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0002-001?Authorization={CWB_API_KEY}"
url2 = ""

req = requests.get(url, verify=False, timeout=5)
response = req.json()

ans = response["records"]["Station"]


arrStation = []
def findTu(arr:list, location:str)->int:
    for i in arr:
        result = i["StationName"]
        arrStation.append(result)
    
    ans = arrStation.index(location)
    return ans

found_index = findTu(ans, "土城")

answer = ans[found_index]
print(answer)
weather_result = {
    "rain_percentage" : answer["RainfallElement"]["Now"]["Precipitation"],
    "max-temparature" : "test",
    "min-temparature" : "test"
}
print("==========")
print(weather_result)

# https://opendata.cwa.gov.tw/dist/opendata-swagger.html?urls.primaryName=openAPI#/%E9%A0%90%E5%A0%B1/get_v1_rest_datastore_F_D0047_069