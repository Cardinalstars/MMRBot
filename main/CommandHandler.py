import discord
import AccessApi
from DiscordInfoManager import discordInfoManager


class CommandHandler:
    """
    Handles commands for the bot
    """
    def __init__(self):
        pass

    def mmr(self, message):
        pass

    def addAlias(self):
        pass

    def addSteamId(*args):
        DIM = discordInfoManager()
        if DIM.addSteamId(args[1], args[0]):
            DIM.writeJsonObjectToFile()
            return "Steam Id Successfully added!"
        else:
            return "Steam Id couldn't be added..."


    def showAlias(self):
        pass

    def lastMatch(self):
        pass

    def theWord(self):
        pass

    def Sanne(self):
        pass

    def fortune(self):
        pass

    def dickSize(self):
        pass

    def ballCircumference(self):
        pass

    def bored(self):
        pass

    def ipooped(self):
        pass

    def patch(self):
        pass

    commandToFunctionMap = {
        "!mmr": mmr,
        "!addAlias": addAlias,
        "!addSteamId": addSteamId,
        "!showAlias": showAlias,
        "!lastMatch": lastMatch,
        "!theWord": theWord,
        "!Sanne": Sanne,
        "!fortune": fortune,
        "!dickSize": dickSize,
        "!ballCircumference": ballCircumference,
        "!bored": bored,
        "!ipooped": ipooped,
        "!patch": patch
    }

    def parseMessage(self, message: discord.Message):
        for command, function in self.commandToFunctionMap.items():
            if message.content.startswith(command):
                args = message.content.split()[1:]
                args = (f"{message.author}",) + tuple(args)
                return function(*args)
