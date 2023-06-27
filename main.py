import time
import datetime
import discord
from dotenv import load_dotenv
import os
from generateMap import GenerateMap
load_dotenv('.env')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)


@tree.command(name="minesweeper", description="Generate a minesweeper map", guild=discord.Object(id=793884190562582578))
async def MinesweeperMapCommand(interaction, diff: float):
    await interaction.response.send_message(GenerateMap(diff, 7))


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=793884190562582578))
    print("Ready!")



client.run(token=os.getenv('DISCORD_KEY'))