from pydantic import BaseModel, StrictInt, field_validator

class FormatRequest(BaseModel):
    text: str
    limit: StrictInt = 40

    @field_validator("limit")
    def check_non_negative(cls, v):
        if v < 0:
            raise ValueError("Limit deve ser positivo")
        return v
