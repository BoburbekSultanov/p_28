import requests
from bs4 import BeautifulSoup


def ob_havo_ol():
    url = 'https://obhavo.uz/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    # Veb-sahifani olish uchun so'rov yuboriladi
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Sahifani olishda xatolik yuz berdi")
        return

    # Tarkibni BeautifulSoup bilan tahlil qilish
    soup = BeautifulSoup(response.text, 'html.parser')

    # Sahifadagi kerakli ma'lumotlarni topish
    # Bu kod sahifadagi ob-havo va harorat ma'lumotlariga mos CSS selektorlarini izlaydi
    # Sayt tuzilishi o'zgarsa, selektorlarni yangilash kerak bo'lishi mumkin

    try:
        shahar = soup.find_all('div', {'class': 'current-city'})
        harorat = soup.find_all('div', {'class': 'current-forecast__temp'})
        holat = soup.find_all('div', {'class': 'current-forecast__comment'})
        test = soup.find('div', {'class': 'current-forecast'}).text

        print(shahar)
        print(harorat)
        print(holat)
        print(test)
        # print(f"Shahar: {shahar}")
        # print(f"Harorat: {harorat}")
        # print(f"Holat: {holat}")

    except AttributeError:
        print("Ob-havo ma'lumotlarini topib bo'lmadi. Sahifa tuzilishi o'zgargan bo'lishi mumkin.")


# Funksiyani ishga tushiramiz
ob_havo_ol()
