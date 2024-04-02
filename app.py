import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
  print('Client started')

@client.event
async def on_member_join(member):
  if member.name.lower().startswith("chienfou") or member.name.lower().startswith("chien fou"):
    await client.ban(member)


client.run("token de ton bot") #ajoute le token de ton bot
