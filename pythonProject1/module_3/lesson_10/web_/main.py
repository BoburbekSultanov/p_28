import httpx
from bs4 import BeautifulSoup
from tabulate import tabulate
import asyncio
import aiofile


class Weather:

    async def main(self):
        design = [
            ['1', 'Toshkent', '2', "Farg'ona"],
            ['3', 'Andijon', '4', 'Namangan'],
            ['5', 'Sirdaryo', '6', 'Jizzax'],
            ['7', 'Samarqand', '8', 'Navoiy'],
            ['9', 'Qashqadaryo', '10', 'Surxandaryo'],
            ['11', 'Buxoro', '12', 'Xorazm'],
            ['13', 'Qoraqolpoqiston']
        ]
        print(tabulate(design, tablefmt='heavy_grid'))
        key = input("Choose number: ")
        match key:
            case '1':
                print('Toshkent')
                print(await self.info_weather('https://obhavo.uz/tashkent'))
                await  self.main()
            case '2':
                print('Farg\'ona')
                print(await  self.info_weather('https://obhavo.uz/ferghana'))
                await self.main()
            case '3':
                print('Andijon')
                print(await self.info_weather('https://obhavo.uz/andijan'))
                await self.main()
            case '4':
                print('Namangan')
                print(await self.info_weather('https://obhavo.uz/namangan'))
                await self.main()
            case '5':
                print('Sirdaryo')
                print(await self.info_weather('https://obhavo.uz/gulistan'))
                await self.main()
            case '6':
                print('Jizzax')
                print(await self.info_weather('https://obhavo.uz/jizzakh'))
                await self.main()
            case '7':
                print('Samarqand')
                print(await self.info_weather('https://obhavo.uz/samarkand'))
                await self.main()
            case '8':
                print('Navoiy')
                print(await self.info_weather('https://obhavo.uz/navoi'))
                await self.main()
            case '9':
                print('Qashqadaryo')
                print(await self.info_weather('https://obhavo.uz/karshi'))
                await self.main()
            case '10':
                print('Surxandaryo')
                print(await self.info_weather('https://obhavo.uz/termez'))
                await self.main()
            case '11':
                print('Buxoro')
                print(await self.info_weather('https://obhavo.uz/bukhara'))
                await self.main()
            case '12':
                print('Xorazm')
                print(await self.info_weather('https://obhavo.uz/urgench'))
                await self.main()
            case '13':
                print('Qoraqolpoqiston')
                print(await self.info_weather('https://obhavo.uz/nukus'))
                await self.main()

    async def info_weather(self, url: str = None) -> str:
        # url = 'https://obhavo.uz/'
        async with httpx.AsyncClient() as coonect:
            response = await coonect.get(url)
        html_code = response
        soup = BeautifulSoup(html_code, 'html.parser')  # noqa
        day = soup.find('div', {'class': 'current-day'}).text.replace(',', ':')
        temp = ' '.join(soup.find("div", {"class": "current-forecast"}).text.split())
        condition = soup.find('div', {'class': 'current-forecast-desc'}).text
        result = f'{day}\nHolat: {condition.lower()}\nHarorat: {temp}'
        return result
        # result = ' '.join(temp.split())
        # return result
        # for card in cards:
        #     print(card.find('span', {}))


asyncio.run(Weather().main())
# asyncio.run(Weather().info_weather())
