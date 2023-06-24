import httpx
import requests
from io import BytesIO
from PIL import Image
from uuid import uuid4


# Note :
# if api not working
# head over to this site :- https://rapidapi.com/TTKTrungKien/api/phototoanime/
# then change the X-RapidAPI-Key token with your own token


# Using httpx + async
async def photo_to_anime(image_url : str) -> str:
    
    url = "https://phototoanime.p.rapidapi.com/draw"
    querystring = {"url":image_url}

    headers = {
	    "X-RapidAPI-Key": "b6b36ec1c8mshe665493313de0e6p1b01b4jsn0c9846988c66",
	    "X-RapidAPI-Host": "phototoanime.p.rapidapi.com"
    }

    async with httpx.AsyncClient(timeout=20) as client:
        try:
            response = await client.get(url, params=querystring ,headers =headers)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            path = f"photo_to_anime_{uuid4()}.jpg"
            img.save(path)
            return path
        except Exception as e:
            return str(e)




# Using Requests + sync
def photo_to_anime(image_url : str) -> str:
    url = "https://phototoanime.p.rapidapi.com/draw"
    querystring = {"url":image_url}

    headers = {
	    "X-RapidAPI-Key": "b6b36ec1c8mshe665493313de0e6p1b01b4jsn0c9846988c66",
	    "X-RapidAPI-Host": "phototoanime.p.rapidapi.com"
    }

    try:
        response = requests.get(url, params=querystring ,headers =headers)
        img = Image.open(BytesIO(response.content))
        path = f"photo_to_anime_{uuid4()}.jpg"
        img.save(path)
        return path
    except Exception as e:
        return str(e)        
    

photo_to_anime("https://cdn.britannica.com/30/182830-050-96F2ED76/Chris-Evans-title-character-Joe-Johnston-Captain.jpg")
