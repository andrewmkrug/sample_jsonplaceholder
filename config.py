from pydantic import BaseModel


class TestCase(BaseModel):
    name: str
    file_path: str


class LoggingConfig(BaseModel):
    pylog_level: str = 'info'


class Config(BaseModel):
    logging: LoggingConfig = LoggingConfig()
