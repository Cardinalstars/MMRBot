import json
import os
import asyncio


# At some point
def sanitizeStringForJson(string):
    if len(string) > 32:
        return ""
    else:
        sanitized_string = json.dumps(string)
        return sanitized_string.strip('"')


class discordInfoManager:
    FILE_PATH = "C:\\Users\\ryann\\IdeaProjects\\MMRBot\\DataStore\\DiscordInfo.json"

    def __init__(self):
        self.discordInfo = self.getDiscordInfoFileJson()
        self.lock = asyncio.Lock()

    def getDiscordInfoFileJson(self):
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "r") as file:
                try:
                    return json.load(file)
                except json.decoder.JSONDecodeError:
                    return {"users": []}  # Initialize as empty list if file is empty
        else:
            return {"users": []}

    def addDiscordUsername(self, discordUsername):
        discordId = sanitizeStringForJson(discordUsername)
        if discordId != "":
            if "users" in self.discordInfo and isinstance(self.discordInfo["users"], list):
                # Append username as an object to "users" array
                foundId = False
                for user in self.discordInfo["users"]:
                    if user["username"] == discordUsername:
                        foundId = True
                if foundId:
                    return True
                else:
                    self.discordInfo["users"].append({"username": discordId})
                    return True
            else:
                return False  # Handle the case where "users" is not a list
        else:
            return False  # Handle the case where discordId is empty

    def addSteamId(self, steamId, discordUsername):
        addedId = False
        print(f"Adding SteamId for {discordUsername}")
        if self.addDiscordUsername(discordUsername):
            users = self.discordInfo["users"]
            for user in users:
                if "username" in user and user["username"] == discordUsername:
                    # Add Steam ID to the user object
                    if "steamId" in user:
                        if steamId in user["steamId"]:
                            return False
                        else:
                            user["steamId"].append(steamId)
                    else:
                        user["steamId"] = [steamId]
                    addedId = True
        return addedId

    def writeJsonObjectToFile(self):
        with open(self.FILE_PATH, "w") as file:
            json.dump(self.discordInfo, file, indent=4)


# if __name__ == "__main__":
#     myObject = discordInfoManager()
#     myObject.addSteamId("steamid3", "nutsack2")
#     myObject.writeJsonObjectToFile()
