from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_token: str
    user_id: str
    bot_name: str
    llm_api_url: str
    llm_api_key: str
    llm_model: str
    whisper_model: str
    whisper_language: str
    whisper_device: str

    class Config:
        env_file = ".env"


settings = Settings()
