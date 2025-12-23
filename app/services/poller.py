from datetime import datetime
from app.models.uptime_check import UptimeCheck
from app.models.incident import Incident
from app.services.normalizer import normalize_status
from app.services.fetcher import fetch_status

async def poll_service(service, db):
    data = await fetch_status(service.status_api_url)

    if not data:
        current_status = "DEGRADED"
    else:
        indicator = data["status"]["indicator"]
        current_status = normalize_status(indicator)

    prev_status = service.current_status

    db.add(UptimeCheck(
        service_id=service.id,
        status=current_status,
        checked_at=datetime.utcnow()
    ))

    if prev_status != current_status:
        db.add(Incident(
            service_id=service.id,
            title=f"{service.name} changed to {current_status}",
            started_at=datetime.utcnow()
        ))

    service.current_status = current_status
    service.last_checked_at = datetime.utcnow()

    db.commit()
