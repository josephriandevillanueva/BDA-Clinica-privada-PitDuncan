from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_appointment():
    return {"message": "appointment created"}
