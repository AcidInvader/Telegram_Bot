from config import API_TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from controller import ModelProcessor


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = ModelProcessor()

# create handler for "start" command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Укажите ваш никнейм")
    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегестрированы", reply_markup=nav.mainMenu)
                          
@dp.message_handler()
async def bot_message(message: types.Message):
    await bot.send_message(message.from_user.id, "Ща подумаю...")
    if message.chat.type == 'private':
        if message.text == 'ПРОФИЛЬ':
            user_nickname = "Ваш Nickname " + db.get_nickname(message.from_user.id)
            await bot.send_message(message.from_user.id, user_nickname)
        else:
            if db.get_signup(message.from_user.id) == 'setnickname':
                if(len(message.text) > 15):
                    await bot.send_message(message.from_user.id, "Никнейм не должен превышать 15 символов")
                elif "@" in message.text or "/" in message.text:
                    await bot.send_message(message.from_user.id, "Вы ввели запрещенный символ")
                else:
                    db.set_nickname(message.from_user.id, message.text)
                    print('nickname seted')
                    db.set_signup(message.from_user.id, "done")
                    await bot.send_message(message.from_user.id, "Вы успешно зарегались", reply_markup=nav.mainMenu)
            else:
                await bot.send_message(message.from_user.id, "Что? Вообще не понимаю!")




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)




