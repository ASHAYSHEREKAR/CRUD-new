from fastapi import FastAPI
from views import user
import models
from database import engine  # <-- Fix this line

app = FastAPI()
app.include_router(user)

models.Base.metadata.create_all(bind=engine)