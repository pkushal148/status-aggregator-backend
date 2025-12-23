import httpx

async def fetch_status(url: str):
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            res = await client.get(url)
            res.raise_for_status()
            return res.json()
        except Exception:
            return None
