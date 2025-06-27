from fastapi import APIRouter

user = APIRouter(tags=["User"])

@user.get("/get-users")
async def read_users():
    return {
        "name": "ashay",
        "age": "22"
    }

@user.post("/create-users")
async def create_users():
    return {
        "name": "ashay",
        "age": "22"
    }

@user.delete("/delete-users")
async def delete_users():
    return {
        "name": "ashay",
        "age": "22"
    }

@user.post("/update-users")
async def update_users():
    return {
        "name": "ashay",
        "age": "22"
    }