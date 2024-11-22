
import bcrypt


hash = '$2b$12$r9k0IK6eR2SzLzdP32UoJuZYG5R6mEpo0zTrkMS1dbcEKfHaZuf9W'
print(bcrypt.checkpw('1234'.encode(), hash.encode()))
