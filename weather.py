import requests

def weatherAPI():
    print("WEATHER IN LAGOS, NIGERIA")
    state = "Lagos, Nigeria"    
    url = f"https://open-weather13.p.rapidapi.com/city/{state}/EN"
    headers = {
        "x-rapidapi-key": "4d7f06c497msh8ae3ad75c4ed8a9p1c158fjsn39f68bdb2dc7",
        "x-rapidapi-host": "open-weather13.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    wAPI = dict(response.json())
    # temp_desc = wAPI['weather'][0]['description']
    # temp_desc = temp_desc.capitalize()
    temp = wAPI['main']['temp']
    print(f"Temperature: {temp}°C")
    # print(f"Description: {temp_desc}")