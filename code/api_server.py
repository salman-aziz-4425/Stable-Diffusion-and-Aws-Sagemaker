from fastapi import FastAPI, Request,HTTPException
from pydantic import parse_obj_as
from controllers.text_to_image_controller import text_to_image_sd1_5,TextToImageInput

app = FastAPI()


@app.get('/ping')
async def ping():
    return {"message": "ok"}

@app.post("/invocations")
async def invocations(request: Request):
    try:
        data = await request.json()
        opt=parse_obj_as(TextToImageInput,data)
        result = await text_to_image_sd1_5(opt)
        print("Final result")
        print(result)
        return {"Output_uri":result}
    except Exception as e:
        return {'error': str(e)}
