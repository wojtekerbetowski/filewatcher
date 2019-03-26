import os

for filename in os.walk("."):
    print(filename)
