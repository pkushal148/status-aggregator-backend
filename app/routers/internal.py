from fastapi import APIRouter

router = APIRouter()

@router.post("/internal/poll-status")
def poll_status():
    return {"message": "Polling endpoint reached"}
