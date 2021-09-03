from datetime import datetime
from typing import Optional
from requests import get
from deta import Deta

from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, HTTPException, status, Form, Response

from ...config import settings
from ...schemas.schemas import UserInDB


router = APIRouter(
    prefix="/wearable/discord",
    tags=["Wearable - Discord"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)



@ router.get("/members")
async def members():
    deta = Deta(settings.DETA_PROJECT_KEY)
    db = deta.Base('members')
    members = next(db.fetch())
    #print(members)

    return JSONResponse(content=members)

@ router.get("/count")
async def count():
    deta = Deta(settings.DETA_PROJECT_KEY)
    db = deta.Base('members')
    members = next(db.fetch())
    #print(members)

    return JSONResponse(content=len(members))