import os

from dotenv import load_dotenv
from supabase import create_client


# Loads .env locally.
# On Render, variables already exist in the environment.
load_dotenv()


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


if not SUPABASE_URL:
    raise ValueError("SUPABASE_URL is not configured")


if not SUPABASE_KEY:
    raise ValueError("SUPABASE_KEY is not configured")


supabase_obj = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)