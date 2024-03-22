from typing import Any

import discord
from discord import Intents
import CommandHandler

class MyClient(discord.Client):

    textChannels = []

    def __init__(self, *, intents: Intents, **options: Any):
        super().__init__(intents=intents, **options)
        self.commandHandler = CommandHandler.CommandHandler()

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        channelList = self.get_all_channels()
        for channel in channelList:
            if channel.type == discord.ChannelType.text:
                self.textChannels.append(channel)

        for channel in self.textChannels:
            print(f'Channel Name: {channel.name} (ID: {channel.id})')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        await message.channel.send(self.commandHandler.parseMessage(message))

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True



client = MyClient(intents=intents)
client.run('MTIwODk5NzEzMTE5MzU1NzA3Mg.GdBR5M.XzqJVU0l-_GCdNLdOSSTLO7ZMghIceqqmOF0sU')