import os
from dotenv import load_dotenv

load_dotenv()


class Data:

    LOGIN = os.getenv("LOGIN")    # "Admin"
    PASSWORD = os.getenv("PASSWORD")     # "admin123"