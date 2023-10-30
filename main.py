from fastapi import APIRouter, Depends
from Routes import page
router= APIRouter()

router.include_router(page)