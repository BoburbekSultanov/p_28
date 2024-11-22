from dataclasses import dataclass
from typing import Optional

from utils import File


@dataclass
class User(File):
    id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    card_id: Optional[int] = None

    def is_validation(self):
        pass

    def login(self):
        pass


print(User().get())
