import os
from fastapi import APIRouter, Depends, Header, HTTPException
from app.database import get_db
from app.models.service import Service
from app.services.poller import poll_service

router = APIRouter()

@router.post("/internal/poll-status")
async def poll_all(
    x_cron_secret: str = Header(None),
    db = Depends(get_db)
):
    if x_cron_secret != os.getenv("CRON_SECRET"):
        raise HTTPException(status_code=401)

    services = db.query(Service).all()

    for service in services:
        await poll_service(service, db)

    return {"status": "polled"}
