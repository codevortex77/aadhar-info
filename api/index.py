from fastapi import FastAPI, HTTPException
import httpx
import json
from datetime import datetime

app = FastAPI()

# 30 Days Validity (Expiring August 3, 2026)
EXPIRY_DATE = datetime(2026, 8, 3)

TARGET_URL = "https://rootx-osint.in/"
ORIGINAL_KEY = "swayam"

@app.get("/api")
async def clone_api(key: str = "", query: str = ""):
    # Validate the key "July"
    if key != "July":
        raise HTTPException(status_code=403, detail="Invalid or Missing API Key")
        
    # Check 30-day validity
    if datetime.now() > EXPIRY_DATE:
        raise HTTPException(status_code=403, detail="API Key 'July' has expired.")

    if not query:
        raise HTTPException(status_code=400, detail="Query parameter is required")

    # High-speed asynchronous fetch
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                TARGET_URL,
                params={"type": "hiteck_aadhar", "key": ORIGINAL_KEY, "query": query},
                timeout=10.0
            )
            data = response.json()
            
            # Remove unwanted metadata keys
            keys_to_remove = ["req_left", "req_total", "expiry", "developer"]
            for k in keys_to_remove:
                data.pop(k, None)
                
            # Add custom branding
            data["Credit"] = "@RichUniversal"
            
            # Global string replacement for any missed handles
            data_str = json.dumps(data)
            data_str = data_str.replace("@simpleguy444", "@RichUniversal")
            
            return json.loads(data_str)
            
        except httpx.RequestError:
            raise HTTPException(status_code=502, detail="Upstream API connection error")
        except json.JSONDecodeError:
            raise HTTPException(status_code=502, detail="Invalid data returned from upstream")
