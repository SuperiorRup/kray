﻿import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'A New Wild Member Appeared')
    print('Sent message to ' + member.name)
    await client.change_presence(game=Game(name='Playing Camshitstudio'))
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hello,I Hope You Will like Our Server')
    print('Sent message to ' + member.name)
    await client.change_presence(game=Game(name='Playing Fortnite'))
    await client.change_presence(game=Game(name='Fortnite'))
    print('Ready') 


@client.event
async def on_message(message):
    if ('heck') in message.content:
       await client.delete_message(message)
    if ('fuck') in message.content:
       await client.delete_message(message)
    if ('bitch') in message.content:
       await client.delete_message(message)
    if ('tf') in message.content:
       await client.delete_message(message)
    if message.content == 'Dbz':
        em = discord.Embed(description='SuperiorRup!!!!')
        em.set_image(url='https://ibb.co/zn3RZJk')
        await client.send_message(message.channel, embed=em)
    if message.content == 'ping':
        await client.send_message(message.channel,'pong')
    if message.content == 'hey':
        await client.send_message(message.channel,'hello')
    if message.content == 'yo':
        await client.send_message(message.channel,'yo')
    if message.content == 'watsup':
        await client.send_message(message.channel,'sky')
    if message.content == 'who is your master':
        await client.send_message(message.channel,'SuperiorRup')
    if message.content.startswith('!flipcoin'):
        randomlist = ['Head','tail']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!what should i play'):
        randomlist = ['fortnite','cs:go','pubg','nothing']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '!fact1':
        await client.send_message(message.channel,'Rup real hair colour is black')
    if message.content == '!fact2':
        await client.send_message(message.channel,'Rup is very Lazy')
    if message.content == '!fact3':
        await client.send_message(message.channel,'Rup favorite food is Fast food')
    if message.content == '!fact4':
        await client.send_message(message.channel,'Rup loves pizza')
    if message.content == '!fact5':
        await client.send_message(message.channel,'Rup is working on new video')
    if message.content == '!what rup is doing':
        await client.send_message(message.channel,'Creating new videos for you guys')
    if message.content == 'SUBS4SUBS':
        em = discord.Embed(description='')
        em.set_image(url='')
        await client.send_message(message.channel, embed=em)
    if ('SUBS4SUBS') in message.content:
       await client.delete_message(message)
    if ('Subs4subs') in message.content:
       await client.delete_message(message)
    if ('subs4subs') in message.content:
       await client.delete_message(message)
    if message.content == '!trool me':
        em = discord.Embed(description='LOL')
        em.set_image(url='https://cdn.discordapp.com/attachments/528873517157056532/530968846635630609/Troll_face.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '!lol':
        em = discord.Embed(description='Laugh Out Laugh')
        em.set_image(url='https://cdn.discordapp.com/attachments/528873517157056532/530968826838515713/meme-png-me-gusta-meme-png-png-image-997.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '!superior army':
        em = discord.Embed(description='Laugh Out Laugh')
        em.set_image(url='https://cdn.discordapp.com/attachments/528873517157056532/530968875052040242/Untitled-1.png')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('!what rup is doing'):
        randomlist = ['Nothing','Creating Video','Free']
        await client.send_message(message.channel,(random.choice(randomlist)))
client.run('NTMxNDU1NTc2MzA4NDQ5MzAx.DxONsQ.D4rzI3n4PsrxMmajnPqMkhwNhYk')
