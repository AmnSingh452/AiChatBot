from fastapi import APIRouter,Request

router = APIRouter()

@router.post("/ask")

async def chat_with_bot(req:Request):
    body = await req.json()
    user_msg = body.get("message")

    return {"reply": f"You said: {user_msg}. I’ll reply soon!"}