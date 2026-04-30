from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_patients():
    return []

@router.post("/")
async def create_patient():
    return {"message": "patient created"}
