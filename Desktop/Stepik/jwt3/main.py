from fastapi import Depends, FastAPI, HTTPException, status,Form

from pydantic import BaseModel
import datetime
import jwt
from fastapi.security import HTTPBearer,OAuth2PasswordBearer,HTTPAuthorizationCredentials,OAuth2AuthorizationCodeBearer,OAuth2PasswordRequestForm

from typing import Annotated

app=FastAPI()
security = HTTPBearer()
#scheme = OAuth2PasswordBearer(tokenUrl="loginNew")
Algor="HS256" # Header
SK="sdfsdfsdfsfsdfsdfsfsdfsfkdjgod_dsfsndfjkhdfbwherwe_sdfnsdf54237iyuitvbn"
ACCESS_MINUTES = 15
class Worker(BaseModel):
    username:str
    password:str

    def get(self, field_name: str):
        # Передаем имя поля (например, "username") и получаем его значение
        return getattr(self, field_name, None)
    
user_db:list[Worker]=[]

@app.post('/register')
async def registerNewUser1(user:Worker):

    if user not in user_db:
        user_db.append(user)
        return("Bingo user in Base")
       

    raise ValueError ("User not in Base")


@app.post('/loginNew')
async def login_new1(form_data:Worker):

    exp = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=ACCESS_MINUTES)

    for user in user_db:
        if user.username == form_data.username and user.password == form_data.password:

            payload = {
                "sub": user.username,
                "exp": exp
            }
            token = jwt.encode(payload, SK, algorithm=Algor)
            return {"acces_token":token,"token_type":"byrer"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password"
    )

@app.get('/me')
async def get_current_user1 (credetinals:Annotated[HTTPAuthorizationCredentials,Depends(security)]):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Не удается валидировать")
    token=credetinals.credentials
    
    if not token or token == "Undefined" or not isinstance(token,str):
        raise exception
    
    payload=jwt.decode(token,SK,algorithms=[Algor])
    username:str = payload.get("sub")
    return {"Username":username}

          

@app.get('/test_me')
async def test_me_url(my_token:str):
    payload=jwt.decode(my_token,SK,algorithms=[Algor])
    username:str=payload.get("sub")
    return {"username_from_url":username}