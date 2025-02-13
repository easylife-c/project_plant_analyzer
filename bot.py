import discord
import os
import config
from plant_api import *
from main import pump_on, pump_off
import time

TOKEN = config.DISCORD_TOKEN

# Set up Discord intents (the message_content intent is required).
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    # Ignore messages from the bot itself.
    if message.author == client.user:
        return

    # Manual pump test command.
    if message.content.startswith("!pump"):
        await message.channel.send("Activating pump for 100 seconds...")
        pump_on()
        time.sleep(100)
        pump_off()
        await message.channel.send("Pump deactivated.")
        return

    # Process image attachments.
    if message.attachments:
        for attachment in message.attachments:
            if attachment.filename.lower().endswith((".jpg", ".jpeg", ".png")):
                await message.channel.send("Processing your plant image...")
                # Save the image temporarily.
                temp_filename = f"temp_{attachment.filename}"
                await attachment.save(temp_filename)
                
                # Identify the plant using the Plant.id API.
                result = identify_plant(temp_filename)
                os.remove(temp_filename)
                
                await message.channel.send(
                f"🌿 {result}"
                           
                        )
                    
client.run(TOKEN)
