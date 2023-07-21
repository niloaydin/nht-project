from fastapi import FastAPI

from api import users,courses,sections

app = FastAPI()


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)
