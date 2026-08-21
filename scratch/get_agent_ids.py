import asyncio
import os
import sys

# Add current path to sys.path
sys.path.insert(0, os.path.abspath('.'))

from app.database import AsyncSessionLocal
from app.models.agent import Agent
from sqlalchemy import select

async def main():
    async with AsyncSessionLocal() as db:
        res = await db.execute(select(Agent).where(Agent.is_deleted.is_(False)))
        agents = res.scalars().all()
        for a in agents:
            print(f"{a.name}: {a.id}")

if __name__ == "__main__":
    asyncio.run(main())
