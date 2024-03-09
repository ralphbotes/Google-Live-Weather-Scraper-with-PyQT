from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def weather(city):
    try:
        location_values = []
        city=city.replace(" ","+")
        res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
        soup = BeautifulSoup(res.text, features="html.parser")
        location = soup.select('#wob_loc')[0].getText().strip()  
        time = soup.select('#wob_dts')[0].getText().strip()       
        info = soup.select('#wob_dc')[0].getText().strip() 
        weather = soup.select('#wob_tm')[0].getText().strip()
        humidity = soup.select('#wob_hm')[0].getText().strip()
        wind = soup.select('#wob_ws')[0].getText().strip()
        location_values.append(location)
        location_values.append(time)
        location_values.append(info)
        location_values.append(weather+"°C")
        location_values.append("Humidity: "+humidity)
        location_values.append("Wind: "+wind)

        return location_values
    except Exception as e:
        print(e)
        return