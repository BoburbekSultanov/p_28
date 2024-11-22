import json
import requests
import asyncio
from bs4 import BeautifulSoup
from columnize import columnize

response = requests.get("https://namozvaqti.uz/viloyat")
response.raise_for_status()

html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

d = []
region_list = soup.find('div', class_='container mt-3')
for region_item in region_list.find_all(class_='col-xl-4 col-xs-12 py-1'):
    region_name = region_item.find('a').text
    region_link = region_item.find('a')['href']
    data = {
        'region': region_name,
        'link': region_link
    }
    d.append(data)

with open('namoz_vaqti.json', 'w') as outfile:
    json.dump(d, outfile, indent=3)


class Region:
    def __init__(self, region, link):
        self.region = region
        self.link = link


class Manage:

    def load_regions(self, file_name):
        with open(file_name, 'r') as f:
            data = json.load(f)
        return [Region(region['region'], region['link']) for region in data]

    def get_link_by_city(self, selected_region, file_name):
        regions = self.load_regions(file_name)
        for region in regions:
            if region.region.lower() == selected_region.lower():
                return region.link
        return "City not found"


async def main(file_name):
    manage = Manage()
    regions = manage.load_regions(file_name)

    region_names = [f"{i + 1}. {region.region}" for i, region in enumerate(regions)]
    formatted_regions = columnize(region_names, displaywidth=80, colsep='   ')

    print(formatted_regions)

    key = int(input('Select a city: '))
    selected_region = regions[key - 1].region
    link = manage.get_link_by_city(selected_region, file_name)
    return link


response = requests.get(asyncio.run(main('namoz_vaqti.json')))
html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

d = []
region_list = soup.find('div', class_='container mt-3')
for region_item in region_list.find_all(class_='col-xl-4 col-xs-12 py-1'):
    region_name = region_item.find('a').text
    region_link = region_item.find('a')['href']
    data = {
        'region': region_name,
        'link': region_link
    }
    d.append(data)

with open('namo_vaqti_shaharlar.json', 'w') as outfile:
    json.dump(d, outfile, indent=3)

response = requests.get(asyncio.run(main("namo_vaqti_shaharlar.json")))
html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

d = []

prayer_times = soup.find('div', class_='ad__in')
for prayer_time in prayer_times.find_all('div', class_='ad__item bor'):
    name = prayer_time.find('h2', class_='nam').text
    time = prayer_time.find('p', class_='time').text
    data = [f"{name}: {time}"]
    d.append(data)

formatted_regions = columnize(d, displaywidth=80, colsep='   ')
print(formatted_regions)
