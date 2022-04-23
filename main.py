from collections import UserList
from typing import List
from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4

from models import User, Gender, Role, UserUpdateRequest


app = FastAPI()

# creating db of Users
db: List[User] = [
    User(
        id=UUID("80f549be-a15d-41c0-aa20-9934b2e911c3"), #fixed ids instead of uuid4() which provides random ids.
        first_name="Orion",
        last_name="Ford",
        gender=Gender.male,
        roles=[Role.admin]
    ),

    User(
        id=UUID("a0688974-d881-4fb6-9915-410350c9029c"),
        first_name="Jane",
        last_name="Doe",
        middle_name="Kelly",
        gender=Gender.female,
        roles=[Role.student, Role.user]
    ),

    User(
        id=uuid4(),
        first_name="Barbra",
        last_name="Doe",
        middle_name="Jane",
        gender=Gender.female,
        roles=[Role.student, Role.user]
    ),
    User(
        id=uuid4(),
        first_name="Tom",
        last_name="Doe",
        middle_name="Bobby",
        gender=Gender.male,
        roles=[Role.student, Role.user]
    )
]

# API endpoints 

@app.get("/")
async def root():
    return {"Hello": "World"}

# GET
@app.get("/api/v1/users")
async def fetch_users():
    return db

# POST
@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return{"id": user.id}

# DELETE
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(UserList)
            return
    # Raising execption of a 404 if the user id isn't found
    raise HTTPException( 
        status_code=404,
        detail=f"user with id: {user.id} does not exists."
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return

    raise HTTPException( 
        status_code=404,
        detail=f"user with id: {user.id} does not exists."
    )
