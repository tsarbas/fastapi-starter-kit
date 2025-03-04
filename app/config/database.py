from typing import Any, TypeAlias

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.config.settings import get_settings

settings = get_settings()

# Define a type alias for the database
DB: TypeAlias = AsyncIOMotorDatabase[dict[str, Any]]
DBClient: TypeAlias = AsyncIOMotorClient[dict[str, Any]]


class Database:
    def __init__(self) -> None:
        self.client: DBClient | None = None
        self.db: DB | None = None

    async def connect(self) -> None:
        self.client = AsyncIOMotorClient(settings.MONGODB_URL)
        self.db = self.client[settings.MONGODB_DB_NAME]

    async def close(self) -> None:
        if self.client:
            self.client.close()
            self.client = None
            self.db = None

    def get_db(self) -> DB:
        if self.db is None:
            raise RuntimeError("Database not initialized")
        return self.db


# Create a single instance
db = Database()


async def init_db() -> None:
    await db.connect()


async def close_db() -> None:
    await db.close()


async def get_database() -> DB:
    return db.get_db()
