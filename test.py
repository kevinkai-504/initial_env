import os
from dotenv import load_dotenv
load_dotenv
a = os.environ.get("CODE", "None")
print(a)