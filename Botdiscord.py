import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

# คำสั่ง chatbot
@bot.event
async def on_message(message):
    mes = message.content # ดึงข้อความที่ถูกส่งมา
    if mes == 'hello':
        await message.channel.send("Hello It's me") # ส่งกลับไปที่ห้องนั่น


# รายการชื่อที่กำหนดไว้
allowed_names = ["ชื่อ1", "ชื่อ2", "ชื่อ3"]  # เปลี่ยนเป็นชื่อที่ต้องการ
registered_names = {}

@bot.command()
async def register(ctx, name: str):
    user_id = ctx.author.id

    # ตรวจสอบว่าผู้ใช้ได้ลงทะเบียนแล้วหรือยัง
    if user_id in registered_names:
        await ctx.send(f'คุณได้ลงทะเบียนชื่อ "{registered_names[user_id]}" เรียบร้อยแล้ว!')
        return

    # ตรวจสอบว่าชื่อถูกใช้แล้วหรือยัง
    if name in registered_names.values():
        await ctx.send(f'ชื่อ "{name}" ถูกใช้ไปแล้ว! กรุณาเลือกชื่ออื่น.')
        return

    if name in allowed_names:
        registered_names[user_id] = name
        await ctx.send(f'คุณได้ลงทะเบียนชื่อ "{name}" เรียบร้อยแล้ว!')
    else:
        await ctx.send(f'ชื่อ "{name}" ไม่ถูกต้อง! กรุณาใช้ชื่อที่กำหนดไว้.')


server_on()

bot.run(os.getenv('TOKEN'))