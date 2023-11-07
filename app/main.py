from fastapi import APIRouter, Depends

router= APIRouter()
app.include_router(api_router, prefix=settings.API_V1_STR)
router.include_router(page)