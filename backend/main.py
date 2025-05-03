from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from datetime import date
from sqlalchemy import select

from sqlalchemy.sql.annotation import Annotated

app = FastAPI()

engine = create_async_engine('sqlite+aiosqlite:///notes.db')

new_sesion = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_sesion() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

class Base(DeclarativeBase):
    pass

class NoteModel(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    date: Mapped[date]

class NoteAddSchema(BaseModel):
    name: str
    description: str
    date: date

class NoteSchema(NoteAddSchema):
    id: int


@app.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


# Разрешить запросы от Vue.js (на порту 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/notes")
async def add_note(data: NoteAddSchema, session: SessionDep):
    new_note = NoteModel(
        name = data.name,
        description = data.description,
        date = data.date
    )
    session.add(new_note)
    await session.commit()
    return {"ok": True}

# @app.get("/notes")
# async def get_note():
#     return {"ok": True}


@app.get("/")
def test():
    return 1