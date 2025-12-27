from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from src.schemas import Post_Format
from src.models import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/upload")
async def upload_file(
    caption: str = Form(...),
    file: UploadFile = File(...),
    session: AsyncSession = Depends(get_async_session)
):
    try:
        os.makedirs("files", exist_ok=True)
        contents = await file.read()
        file_location = f"files/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(contents)

        new_post = Post(
            caption=caption,
            url=file_location,
            file_type=file.content_type
        )
        session.add(new_post)
        await session.commit()
        await session.refresh(new_post)

        return {"id": new_post.id, "caption": new_post.caption, "url": new_post.url, "file_type": new_post.file_type}
    except Exception as e:
        print("UPLOAD ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session)
    ):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]

    post_data = []
    for post in posts:
        post_data.append(
            {
                "id": str(post.id),
                "caption": post.caption,
                "url": post.url,
                "file_type": post.file_type,
                "created_at": post.created_at.isoformat()
            }
        )
    return {"posts": post_data}