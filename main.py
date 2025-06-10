from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def welcome():
    return "<h1>مرحبا تسنيم!</h1>"
