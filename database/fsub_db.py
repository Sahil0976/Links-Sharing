
import motor.motor_asyncio
from config import DB_URI, DB_NAME

dbclient = motor.motor_asyncio.AsyncIOMotorClient(DB_URI)
database = dbclient[DB_NAME]

fsub = database['fsub']

async def add_fsub(chat_id: int):
    await fsub.update_one({'_id': 'fsub_chat'}, {'$set': {'chat_id': chat_id}}, upsert=True)

async def rm_fsub():
    await fsub.delete_one({'_id': 'fsub_chat'})

async def get_fsub():
    return await fsub.find_one({'_id': 'fsub_chat'})
