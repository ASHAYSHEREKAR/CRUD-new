from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    database_url = "mysql+pymysql://ashay:ashay123@localhost:3306/crud_users"  # Replace with your actual database URL
    engine = create_engine(database_url)
    SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
except Exception as e:
    print("error is :", e)

def get_db():
    db = SessionLocal()
    try:
        yield db 
    except Exception as e:
        print("error is :", e)
    finally:
        db.close()