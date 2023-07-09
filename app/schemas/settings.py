from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = "a49412347d7c0dedca17b4402a0484a969ba8b969bfcf7f44cb5579f9d9f3c18"
