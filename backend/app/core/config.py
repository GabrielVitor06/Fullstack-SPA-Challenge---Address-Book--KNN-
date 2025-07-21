DATABASE_URL = "postgresql+asyncpg://postgres:523079GJ@db.xplpbktjaomsjvvygjwv.supabase.co:5432/postgres"
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
