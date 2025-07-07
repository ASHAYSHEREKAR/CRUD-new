from fastapi import APIRouter
from database import get_db
from models import User as crud_user
from schemas import Create_User as user_schema
from datetime import datetime

user = APIRouter(tags=["User"])

@user.get("/get-users")
async def read_users():
    try:
        db = next(get_db())
        users = db.query(crud_user).all()
        print("users are :", users)
        return users
    except Exception as e:
        print("error is :", e)
    finally:
        db.close()

@user.post("/create-users")
async def create_users(user_data: dict):
    try:
        db = next(get_db())
        # Convert dict to Pydantic schema, then to ORM model
        user_obj = user_schema(**user_data)
        db_user = crud_user(**user_obj.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        print("error is :", e)
    finally:
        db.close()

@user.delete("/delete-users")
async def delete_users(name: str):
    try:
        db = next(get_db())
        db_user = db.query(crud_user).filter(crud_user.name==name).first()
        if db_user is None:
            return {"message": "User not found"}
        db.delete(db_user)
        db.commit()
        return {"message": "User deleted successfully"}
    except Exception as e:
        print("error is :", e)
    finally:
        db.close()

@user.post("/update-users")
async def update_users(name: str , mobile_number_input: str, address_input: str):
    try:
        db = next(get_db())
        db_user = db.query(crud_user).filter(crud_user.name==name).first()
        if db_user is None:
            return {"message": "User not found"}
        db_user.mobile_number = mobile_number_input
        db_user.address = address_input
        db_user.updated_at = datetime.now()
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        print("error is :", e)
    finally:
        db.close()