import os

from dotenv import load_dotenv


class EnvironmentReader:

    @staticmethod
    def get(s: str):
        load_dotenv()
        return os.getenv(s)
