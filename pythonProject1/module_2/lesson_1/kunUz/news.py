from datetime import datetime
from typing import List

list_news = List['News']


class News:
    def __init__(self,
                 type_news: str,
                 date: str,
                 term_of_study: int,
                 title: str,
                 article: str,
                 image: str = None,
                 by_image: str = None,
                 video: str = None,
                 by_video: str = None,
                 view: int = 0
                 ):
        self.type_news = type_news
        self.date = date
        self.term_of_study = term_of_study
        self.title = title
        self.article = article
        self.view = view
        self.image = image
        self.by_image = by_image
        self.video = video
        self.by_video = by_video

    def creat_news(self):
        self.type_news = input('Enter Type new: ')
        self.date = input('Enter date: ')
        self.term_of_study = int(input('Enter term of study: '))
        self.title = input('Enter title: ').title()
        self.article = input('Enter article: ')
        self.image = input('Enter image link: ')
        self.by_image = input('Enter by image: ')
        self.video = input('Enter video link: ')
        self.by_video = input('Enter by video: ')
        obj = News(self.type_news,
                   self.date,
                   self.term_of_study,
                   self.title,
                   self.article,
                   self.image,
                   self.by_image,
                   self.video,
                   self.by_video)
        list_news.append(obj)


while True:
    text = input("""
    1) creat type news
    2) search
    3) change news
    4) delete news
    >>> """)
    match text:
        case '1':
            pass
        case '2':
            pass
        case '3':
            pass
        case '4':
            pass
        case '5':
            pass
