from pathlib import Path
from os.path import join

BASE_DIR = Path(__file__).parent.parent
DB_PATH = join(BASE_DIR, "database")
print(BASE_DIR)
print(DB_PATH)


class File:
    # def file_name(self):
    #     return self.__class__.__name__.lower() + 's.txt'

    def save(self) -> None:
        # self.file_name()
        pass

    def get(self) -> list:
        file_name = self.__class__.__name__.lower() + 's.txt'
        with open(join(DB_PATH, file_name)) as f:
            datas = f.readlines()
        return datas

    def update(self, field, new_value):
        pass

    def delete(self) -> None:
        pass
