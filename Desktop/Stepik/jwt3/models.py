from pydantic import BaseModel



class LoginRequest(BaseModel):
    username:str
    password:str

    def get(self, field_name: str):
        # Передаем имя поля (например, "username") и получаем его значение
        return getattr(self, field_name, None)