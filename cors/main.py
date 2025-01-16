from fastapi import FastAPI
import httpx


app = FastAPI()
service_url="http://localhost:8001"

@app.get("/get-users")
async def get_users():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{service_url}/get-users")
        return response.json()


    


