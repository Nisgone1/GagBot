import discord
from discord.ext import commands

# Intents setup
intents = discord.Intents.default()
intents.message_content = True  # Needed to read user messages

# Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Prevents bot from responding to itself

    # Replace message with "M"
    transformed_message = "M" * len(message.content)

    await message.channel.send(transformed_message)

    # Process commands if needed
    await bot.process_commands(message)

# Run the bot
bot.run("YOUR_BOT_TOKEN")
