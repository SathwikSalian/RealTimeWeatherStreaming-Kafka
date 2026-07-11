from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Bangalore"
BOOTSTRAP_SERVER = "localhost:9092"
TOPIC_NAME = "weather-data"