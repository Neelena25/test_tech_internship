import os
import pytest
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)

@pytest.fixture
def base_url():
    url = os.getenv("BASE_URL")
    assert url is not None, "BASE_URL not found. Check your .env file."
    return url