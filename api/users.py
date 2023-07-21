import fastapi
from pydantic import BaseModel
from typing import Optional, List

router = fastapi.APIRouter()



users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users", response_model=User)
async def create_user(user: User):
    users.append(user)
    return user


@router.get("/users/{id}", response_model=User)
async def get_user(id: int):
    return users[id]