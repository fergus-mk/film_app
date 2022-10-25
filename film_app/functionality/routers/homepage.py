from fastapi import APIRouter

from ..helpers import homepage_helpers


router = APIRouter(tags=["homepage"])


@router.get("/")
async def root():
    "Returns hello world message on homepage"
    return homepage_helpers.root_get()
