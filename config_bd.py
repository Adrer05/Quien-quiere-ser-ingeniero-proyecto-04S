import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


# Construct the SQLAlchemy connection string
DATABASE_URL = os.getenv("DATABASE_URL")
# Create the SQLAlchemy engine
