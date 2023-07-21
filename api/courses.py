import fastapi

router = fastapi.APIRouter()


@router.get("/courses")
async def get_courses():
    return {"get courses"}


@router.post("/courses")
async def create_courses():
    return {"create courses"}


@router.get("/courses/{id}")
async def get_course():
    return {"get one course"}


@router.patch("/courses/{id}")
async def update_course():
    return {"update a course"}


@router.delete("/courses/{id}")
async def delete_course():
    return {"delete a course"}
