import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TW2EN: int = 0
    EN2TW: int = 1
    LINEBOT_EN2TW_ACCESS_TOKEN: str = os.environ.get("LINEBOT_EN2TW_ACCESS_TOKEN", "")
    LINEBOT_EN2TW_CHANNEL_SECRET: str = os.environ.get(
        "LINEBOT_EN2TW_CHANNEL_SECRET", ""
    )
    LINEBOT_TW2EN_ACCESS_TOKEN: str = os.environ.get("LINEBOT_TW2EN_ACCESS_TOKEN", "")
    LINEBOT_TW2EN_CHANNEL_SECRET: str = os.environ.get(
        "LINEBOT_TW2EN_CHANNEL_SECRET", ""
    )
    EN2TW_OPENAI_API_KEY: str = os.environ.get("EN2TW_OPENAI_API_KEY", "")
    TW2EN_OPENAI_API_KEY: str = os.environ.get("TW2EN_OPENAI_API_KEY", "")


settings = Settings()
