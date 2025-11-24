import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # API
    API_TITLE: str = "Demand Forecasting Service"
    API_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", False)
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    DATABASE_ECHO: bool = os.getenv("DATABASE_ECHO", False)
    
    # Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    REDIS_CACHE_TTL: int = int(os.getenv("REDIS_CACHE_TTL", 3600))
    
    # JWT
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    
    # ML Model
    MODEL_WINDOW_SIZE: int = int(os.getenv("MODEL_WINDOW_SIZE", 30))
    FORECAST_HORIZON: int = int(os.getenv("FORECAST_HORIZON", 7))
    TRAINING_EPOCHS: int = int(os.getenv("TRAINING_EPOCHS", 50))
    BATCH_SIZE: int = int(os.getenv("BATCH_SIZE", 32))
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
