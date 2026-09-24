import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / ".env"
print(f"Env path: {env_path}")
print(f"Exists: {env_path.exists()}")
load_dotenv(env_path)
print(f"GROQ: {os.getenv('GROQ_API_KEY')}")
