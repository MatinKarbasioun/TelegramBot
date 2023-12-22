import aiohttp
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Message(BaseModel):
    token: str
    chat_id: str
    message: str


class Response(BaseModel):
    status: str


async def send_telegram_message(token, chat_id, message):
    api_url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, json=payload) as response:
            return await response.text(), response.status


@app.get("/")
async def read_root():
    return {"app": "publisher is up and running"}


@app.post("/v1/message", status_code=status.HTTP_200_OK)
async def send_message(message: Message) -> Response:
    try:
        result, status_code = await send_telegram_message(message.token, message.chat_id, message.message)

        if status_code == 200:
            return Response(status="Message sent successfully")
        else:
            raise HTTPException(status_code=status_code, detail=f"Failed to send message: {result}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))









