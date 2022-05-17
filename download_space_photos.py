import requests
import os
from os.path import splitext
from datetime import datetime
from dotenv import load_dotenv
from urllib.parse import urlsplit


def download_img(url, filename):
    os.makedirs('images', exist_ok=True)
    path = f'images/{filename}'

    response = requests.get(url)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    launch_number = 100
    url = 'https://api.spacexdata.com/v4/launches'
    response = requests.get(url)
    response.raise_for_status()
    img_urls = response.json()[launch_number]['links']['flickr']['original']

    for img_url_number, img_url in enumerate(img_urls):
        download_img(img_url, f'spacex_launch{img_url_number}.jpg')


def get_image_extension(url):
    return splitext(urlsplit(url).path)[1]


def fetch_nasa_pictures_of_the_day(api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params={'api_key': api_key, 'count': '20'})
    response.raise_for_status()

    pictures_of_the_day = response.json()
    for picture_number, picture_of_the_day in enumerate(pictures_of_the_day):
        url_picture_of_the_day = picture_of_the_day['url']
        download_img(
            url_picture_of_the_day,
            f'nasa_picture_of_the_day{picture_number}{get_image_extension(url_picture_of_the_day)}'
        )


def fetch_nasa_epic(api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    response = requests.get(url, params={'api_key': api_key})
    response.raise_for_status()

    for i in range(5):
        epic_info = response.json()[i]
        converted_date = datetime.strptime(epic_info['date'], '%Y-%m-%d %H:%M:%S').strftime('%Y/%m/%d')
        download_url = f'https://api.nasa.gov/EPIC/archive/natural/{converted_date}/png/{epic_info["image"]}.png?api_key={api_key}'
        download_img(download_url, f'nasa_epic{i}.png')


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.getenv("NASA_API_KEY")
    fetch_spacex_last_launch()
    fetch_nasa_pictures_of_the_day(nasa_api_key)
    fetch_nasa_epic(nasa_api_key)
