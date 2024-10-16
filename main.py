import parse
import discord
import Config
from discord.ext import commands
from mysql.connector import connect, Error
import asyncio
import nest_asyncio
minute =15
nest_asyncio.apply()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
async def timer():
    await asyncio.sleep(minute*60)
@bot.command()
async def start(ctx):
    while True:
        asyncio.run(timer())
        html = parse.get_html(parse.URL)
        link = parse.get_content(html)
        try:
            with connect(
                    host="localhost",
                    user="Shadow",
                    password="Evropa18",
                    database="newslinks"
            ) as connection:
                check = "select link from links where link = '"+link+"'"
                with connection.cursor(buffered=True) as cursor:
                    cursor.execute(check)
                if cursor.rowcount <1:
                    insert = """
                                        INSERT INTO links
                                        (link)
                                        VALUES ( %s )
                                        """
                    links = [link]
                    with connection.cursor() as cursor:
                        cursor.execute(insert,
                                           links)
                        connection.commit()
                        await ctx.send(link)
        except Error as e:
            print(e)
            await ctx.send('Произошла ошибка, позовите идиота, который меня создал!!')



bot.run(Config.settings)