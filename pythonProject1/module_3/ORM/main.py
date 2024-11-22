from dataclasses import dataclass
from pathlib import Path
from os.path import join
from typing import Optional
from json import load, loads, dumps, dump

BASE_DIR = Path(__file__).parent.parent
DB_PATH = join(BASE_DIR, 'ORM')


# print(BASE_DIR)
# print(DB_PATH)

class File:
    async def write(self):
        pass

    def save(self):
        with open(join(DB_PATH, self.__class__.__name__.lower() + 's.json')) as f:
            data = load(f)
        self._id = 1 if not data else data[-1]._id + 1
        data.append(self)
        # with open(join(DB_PATH, self.__class__.__name__.lower() + 's.json'), 'w') as f:
        #     f.write(data)



        # return join(DB_PATH, self.__class__.__name__.lower() + 's.json')

    def delete(self):
        pass

    def update(self, new_value, value):
        pass

    def get(self):
        pass


@dataclass
class User(File):
    _id: Optional[str] = None
    name: Optional[str] = None


@dataclass
class Product(File):
    _id: Optional[str] = None
    name: Optional[str] = None


user = User(name='Bobur')
print(user.save())
user1 = User(name='Komil')
print(user1.save())
