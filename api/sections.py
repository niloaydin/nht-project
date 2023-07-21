import fastapi

router = fastapi.APIRouter()


@router.get("/sections/{id}")
async def section():
    return {"get a section"}


@router.get(f"/sections/{id}/content-block")
async def get_section_content_blocks():
    return {"get a content block of a section "}


@router.get("/content-blocks/{id}")
async def get_content_block():
    return {"get a content block by id"}


