import json
import os
from typing import List
import requests
from fastapi import Depends, FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi import FastAPI, HTTPException
from schema.user import User, Users

from fastapi.security import (
    HTTPBasic,
    HTTPBearer,
)

basic_auth = HTTPBasic()
bearer_auth = HTTPBearer(auto_error=False)

async def get_authorization_header(
    request: Request,
):
    token = request.headers.get("Token")
    if token == "1234567890":
        return token
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")

app = FastAPI()

@app.post("/users/")
async def add_one_user(request: Request ,user: User, token: str = Depends(get_authorization_header)):
    try:
        print(await request.json())
        
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})

    except Exception as e:
        return JSONResponse(
            status_code=500, content={"detail": "An error occurred", "error": str(e)}
        )
    

@app.post("/users/multiple")
async def add_multiple_users(users: List[User], token: str = Depends(get_authorization_header)):
    try:
        for user in users:

            open("users/"+ user.user_id + ".json", "w").write(user.model_dump_json())
        return {"status": "OK"}
        
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})

    except Exception as e:
        return JSONResponse(
            status_code=500, content={"detail": "An error occurred", "error": str(e)}
        )



@app.get("/users")
async def get_all_users(token: str = Depends(get_authorization_header)):
    try:
        open("users.json", "r").read()
        
        return {"status": "OK"}
        
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code, content={"error": e.detail})

    except Exception as e:
        return JSONResponse(
            status_code=500, content={"detail": "An error occurred", "error": str(e)}
        )
