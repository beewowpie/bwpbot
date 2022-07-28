from aiogram import Bot, Dispatcher, executor, types
import python_weather

bot = Bot(token='5495420930:AAGKfVJBu5JAjcKg1fvffjwrAM6vBNDAHUQ')
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL, locale='ru-Ru')


@dp.message_handler()
async def echo(message: types.Message):
    weather = await client.find(message.text)
    celsius = round((weather.current.temperature - 32) / 1.8)

    resp_msg = weather.location_name + '\n'
    resp_msg += f'Текущая температура:  {celsius} °\n'
    resp_msg += f'Состояние погоды:  {weather.current.sky_text}'

    if celsius <= 10:
        resp_msg += '\n\nСейчас очень холодно, одевайся очень тепло!'
    elif celsius <= 15:
        resp_msg += '\n\nСейчас холодно, одевайся по теплее!'
    else:
        resp_msg += '\n\nТемпература OK, одевай что угодно!'

    await message.answer(resp_msg)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

