import os


def load_settings() -> dict:
    return {
        "debug": os.getenv("DEBUG").lower() == "true",
        "region": os.getenv("APP_REGION", "eu-west-1"),
    }
