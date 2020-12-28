import discord
from discord.ext import commands
import time
import os
import smtplib
import random
import json
import asyncio
import requests


bot = commands.Bot(command_prefix="*", help_command=None, self_bot=True)


def show_on():
    os.system("cls")

    print("""
 ██████╗ ██╗███╗   ██╗███████╗███████╗███╗   ██╗███████╗ ██████╗ 
██╔════╝ ██║████╗  ██║██╔════╝██╔════╝████╗  ██║██╔════╝██╔═══██╗
██║  ███╗██║██╔██╗ ██║███████╗█████╗  ██╔██╗ ██║█████╗  ██║   ██║
██║   ██║██║██║╚██╗██║╚════██║██╔══╝  ██║╚██╗██║██╔══╝  ██║   ██║
╚██████╔╝██║██║ ╚████║███████║███████╗██║ ╚████║██║     ╚██████╔╝
 ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                                 
""")
    print('SelfBot Made by Ginsenfo')
    print()
    print(f'Connected as {bot.user.name} ')
    print('>> SelfBot')
    print(f">> Name: {bot.user.name}")
    print(f">> ID: {bot.user.id}")
    print()


@bot.event
async def on_ready():
    os.system('cls')
    show_on()


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if "ginsenfo" in message.content and message.author != bot.user:
        await message.channel.send('who called me lol')

    if "karmah" in message.content:
        await message.channel.send('Cosa vuoi dal mio lord')

    if "autodestroyginsenfo" in message.content:
        await message.channel.send("autodestroyginsenfo")
    
    if "gay" in message.content:
        response = await message.channel.send("no u")
        await asyncio.sleep(13)
        response.delete()
        
    if "beef" in message.content:
        await message.channel.send("BEEEF")

        

@bot.command(aliases=['aiuto'])
async def help(ctx):
    help_mess = """1. spam (number) (message) (time between mess) \n2. clear (number) \n3. shit \n4. emailspammer (email) (message)\n5. noia (number) (message)"""
    await ctx.send(f"```{help_mess}```")


@bot.command()
async def spam(self, ctx,  amount, *args):
    await ctx.channel.purge(limit=1)
    amount = int(amount)
    mesg = ' '.join(args)

    if amount > 1:
        for i in range(amount):
            await ctx.send(mesg)
            time.sleep(0.8)
    else:
        await ctx.send(mesg)


@bot.command(aliases=['noia', "bored"])
async def boring(self, ctx, amount, *args):
    await ctx.channel.purge(limit=1)
    amount = int(amount)
    mesg = ' '.join(args)
    for i in range(amount):
        await ctx.channel.send(mesg)
        await ctx.channel.purge(limit=1)
    await ctx.channel.purge(limit=1)


def is_me(m):
    return m.author == bot.user


@bot.command(aliases=['delete', 'elimina'])
async def purge(ctx, amount:int=None):
    await ctx.channel.purge(limit=1)
    try:
        if amount is None:
            await ctx.send("Invalid amount")
        else:
            amount += 1
            deleted = await ctx.channel.purge(limit=amount, before=ctx.message, check=is_me)
            
    except:
        try:
            await asyncio.sleep(1)
            c = 0
            async for message in ctx.message.channel.history(limit=amount):
                if message.author == bot.user:
                    c += 1
                    await message.delete()
                else:
                    pass
            
        except Exception as e:
            await ctx.send(f"Error: {e}")



@bot.command(aliases=['webdel', 'delweb'])
async def deletewebhook(ctx, url):
    await ctx.channel.purge(limit=1)
    try:
        requests.delete(url)
        temp_mess = await ctx.send("```-Webhook terminated successfully```")
        asyncio.sleep(10)
        temp_mess.delete()
    except:
        temp_mess = await ctx.send("```-Can't terminate the webhook! \n Check if the url is valide or probalby the webhook does not exist ```")
        asyncio.sleep(10)
        temp_mess.delete()
    

@bot.command()
async def terminate_token(ctx, token2destroy):
    await ctx.send(f"No shut up")



@bot.command(aliases=['stream'])
async def streaming(ctx, link ,status: str=None):
    if status is None:
        await ctx.send(f"Invalid argument")
    else:
        try:
            game = discord.Activity(type=1, name=f"{status}", url=link)
            await bot.change_presence(activity=game)
            await ctx.send(f"Status changed to: `Streaming {status}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")


@bot.command(aliases=['play', 'p'])
async def playing(ctx, *,status: str=None):
    if status is None:
        await ctx.send(f"Invalid argument")
    else:
        try:
            game = discord.Activity(type=0, name=f"{status}")
            await bot.change_presence(activity=game)
            await ctx.send(f"Status changed to: `Playing {status}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")
        
@bot.command(aliases=['watch'])
async def watching(ctx, status):
    try:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await ctx.send(f"Status changed to: `Watching {status}`")

    except Exception as e:
        await ctx.send(f"Error: {e}")


@bot.command(aliases=['remstatus','rem_status', 'remstat'])
async def removestatus(ctx):

    try:
        temp_mess = discord.Activity(type=-1)
        await bot.change_presence(activity=temp_mess)
        await ctx.send(f"Status removed")
    except Exception as e:
        await ctx.send(f"Error: {e}")

#create cmd for change status to random states


@bot.command(aliases=['e-spammer','spamemail'])
async def emailspammer(ctx, emaildest, *args):

    await ctx.send(f"Spamming `{emaildest}`")

    mesg = ' '.join(args)

    with open("config.json") as f:
        email_addr = json.load(f)["email_addr"]
        f.close()

    with open("config.json") as f:
        email_pass = json.load(f)["email_pass"]
        f.close()


    message_spammed = 0

    while True:

        try:
            email = smtplib.SMTP("smtp.gmail.com", 587)
            email.ehlo()  # effettuo l'hello col Server
            email.starttls()  # avvio il canale TLS
            email.login(email_addr, email_pass)  # login
            email.sendmail(email_addr, emaildest, mesg)
            email.quit()
            print("Messagge sended!")
            message_spammed += 1

        except KeyboardInterrupt:
            await ctx.send(f"Spam terminated with `{message_spammed}` emails!")






with open("config.json") as f:
    token = json.load(f)
    bot.run(token["token"], bot=False)
