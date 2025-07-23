from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from backend.schema import User

app = FastAPI()

@app.post("/userdata")
async def userdata(data: User):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'msg': "User data entered",
            'status': True,
            'data': data.model_dump_json()
        }
    )