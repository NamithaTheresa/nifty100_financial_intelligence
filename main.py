from dotenv import load_dotenv
import os

load_dotenv()
print("Project Started")
print(os.getenv("PROJECT_NAME"))

