import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from schema import User

app = FastAPI()

@app.post("/userdata")
async def userdata(data: User):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'msg': "User data entered",
            'status': True,
            # 'data': data.model_dump_json()
        }
    )



# input_json = {
#     "name": "test1",
#     "email": "test1@klizos.com",
#     "phone_no": 7063315080,
#     "password": "Klizos@123"
# }

