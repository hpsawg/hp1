import discord
from discord.ext import commands
import requests
from datetime import datetime

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='город')
async def get_time(ctx, city=None):
    if city is None:
        await ctx.send('Необходимо указать город: Москва, Якутск или Красноярск')
    elif city.lower() == 'москва':
        #  время
        time_url = "http://worldtimeapi.org/api/timezone/Europe/Moscow"
        time_response = requests.get(time_url)
        time_data = time_response.json()

        if 'datetime' in time_data:
            time_str = time_data['datetime']
            time_obj = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%f%z')
            time_moscow = time_obj.strftime('%H:%M:%S')
        else:
            time_moscow = 'Ошибка получения данных о времени. Пожалуйста, попробуйте позже.'

        #  температуру
        temp_url = "http://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=848ba6c47ca624745d144f63606bd664"
        temp_response = requests.get(temp_url)
        temp_data = temp_response.json()

        if temp_data['cod'] == 200:
            temp_kelvin = temp_data['main']['temp']
            temp_celsius = round(temp_kelvin - 273.15, 2)
            temp_message = f'Текущая температура в Москве: {temp_celsius}°C'
        else:
            temp_message = 'Ошибка получения данных о температуре.'

        await ctx.send(f'Текущее время в Москве: {time_moscow}\n{temp_message}')

    elif city.lower() == 'якутск':
        #  время
        time_url = "http://worldtimeapi.org/api/timezone/Asia/Yakutsk"
        time_response = requests.get(time_url)
        time_data = time_response.json()

        if 'datetime' in time_data:
            time_str = time_data['datetime']
            time_obj = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%f%z')
            time_yakutsk = time_obj.strftime('%H:%M:%S')
        else:
            time_yakutsk = 'Ошибка получения данных о времени. Пожалуйста, попробуйте позже.'

        #  температуру
        temp_url = "http://api.openweathermap.org/data/2.5/weather?q=Yakutsk&appid=848ba6c47ca624745d144f63606bd664"
        temp_response = requests.get(temp_url)
        temp_data = temp_response.json()

        if temp_data['cod'] == 200:
            temp_kelvin = temp_data['main']['temp']
            temp_celsius = round(temp_kelvin - 273.15, 2)
            temp_message = f'Текущая температура в Якутске: {temp_celsius}°C'
        else:
            temp_message = 'Ошибка получения данных о температуре.'

        await ctx.send(f'Текущее время в Якутске: {time_yakutsk}\n{temp_message}')

    elif city.lower() == 'красноярск':
        # время и температура для Красноярска
        time_url = "http://worldtimeapi.org/api/timezone/Asia/Krasnoyarsk"
        time_response = requests.get(time_url)
        time_data = time_response.json()

        if 'datetime' in time_data:
            time_str = time_data['datetime']
            time_obj = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%f%z')
            time_krasnoyarsk = time_obj.strftime('%H:%M:%S')
        else:
            time_krasnoyarsk = 'Ошибка получения данных о времени. Пожалуйста, попробуйте позже.'

        #  температура
        temp_url = "http://api.openweathermap.org/data/2.5/weather?q=Krasnoyarsk&appid=848ba6c47ca624745d144f63606bd664"
        temp_response = requests.get(temp_url)
        temp_data = temp_response.json()

        if temp_data['cod'] == 200:
            temp_kelvin = temp_data['main']['temp']
            temp_celsius = round(temp_kelvin - 273.15, 2)
            temp_message = f'Текущая температура в Красноярске: {temp_celsius}°C'
        else:
            temp_message = 'Ошибка получения данных о температуре.'

        await ctx.send(f'Текущее время в Красноярске: {time_krasnoyarsk}\n{temp_message}')

    else:
        await ctx.send('Укажите один из доступных городов: Москва, Якутск или Красноярск')

bot.run('токен бота')
