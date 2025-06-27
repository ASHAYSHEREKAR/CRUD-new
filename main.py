from fastapi import FastAPI
from views import user

app = FastAPI()
app.include_router(user)