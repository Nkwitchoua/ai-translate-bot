import asyncio
from aiogram import Bot
from bot.loader import dp, bot
from bot.handlers import start #, translate, payments
# from bot.middlewares.subscription_check import SubscriptionMiddleware

async def main():
    dp.include_routers(start.router)#, translate.router, payments.router)
    # dp.message.middleware(SubscriptionMiddleware())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
