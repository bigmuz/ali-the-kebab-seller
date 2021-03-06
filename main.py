import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix = '>', intents = discord.Intents.all())

# ON READY
@client.event
async def on_ready():
  print(f"Logged in as {client.user}")

# PING TEST
@client.command()
async def ping(ctx):
  await ctx.send('Pong! - {0}'.format(round(client.latency, 2))+'ms')

# SERVER INFO
@client.command()
async def serverInfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)
  owner = str(ctx.guild.owner)
  serverID = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)
  icon = str(ctx.guild.icon_url)

  embed = discord.Embed(title=name+ " Server Information", description=description, color=discord.Color.blue())
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner: ", value=owner, inline=True)
  embed.add_field(name="Server ID:", value=serverID, inline=True)
  embed.add_field(name="Region: ", value=region, inline=True)
  embed.add_field(name="Member Count: ", value=memberCount, inline=True)

  await ctx.send(embed=embed)

# DELETE MESSAGES - DEFAULTS AS 1 (+1 to delete the command message itself)
@client.command()
async def delete(ctx, amount=1):
  await ctx.channel.purge(limit=amount+1)

# KICK
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)

@client.command()
async def kickAll(ctx):
  for user in ctx.guild.members:
    try:
      await user.kick()
    except:
      pass

# BAN
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)

@client.command()
async def banAll(ctx):
  for user in ctx.guild.members:
    try:
      await user.ban()
    except:
      pass

keep_alive()
client.run(os.getenv('TOKEN'))

#await bot.process_commands(message)