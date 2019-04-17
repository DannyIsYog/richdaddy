import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

TOKEN = 'NTY3NzUyODcyNjc0OTgzOTQ2.XLYHcw.ZG_KpkU6IecoG7z6rZLy-Bjagec'

subscription_channel = 'subscrições'

@client.event
async def on_ready():
    print('Bot is ready!')

@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)
    await channel.send(hash(payload.emoji))


@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount)

@client.command()
async def change_sub_channel(ctx):
    if ctx.message.author.top_role == 'Mod':
        await ctx.send(ctx.message.author.top_role)
    await ctx.send(ctx.message.author.top_role)
@client.command()
async def subscribe(ctx, wanted_role):
    if ctx.message.channel.name == subscription_channel:
        role = discord.utils.get(ctx.guild.roles, name=wanted_role)
        member = ctx.message.author
        try:
            await member.add_roles(role)
            await ctx.send(member.name + ' subscreveu a notificações de ' + wanted_role)
        except:
            await ctx.send('subscrição ' + wanted_role + ' inexistente')

@client.command()
async def unsubscribe(ctx, wanted_role):
    if ctx.message.channel.name == subscription_channel:
        role = discord.utils.get(ctx.guild.roles, name=wanted_role)
        member = ctx.message.author
        try:
            await member.remove_roles(role)
            await ctx.send(member.name + ' cancelou a subscrição a notificações de ' + wanted_role)
        except:
            await ctx.send('subscrição ' + wanted_role + ' inexistente')

client.run(TOKEN)
