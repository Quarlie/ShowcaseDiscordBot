import ast, json

from redvid import Downloader

import interactions as i

#################
# Save and Load #
#################
async def loadDatabase(bot):
    #redis = Redis(
    #    host="containers-us-west-67.railway.app",
    #    port="6998",
    #    password="oeGDqAJVBer0V1pqHJml")

    #for key in redis.scan_iter():
    #    key = await byteToString(key)
    #    value = await byteToString(redis.get(key))
    #    setattr(bot, key, ast.literal_eval(value))
    bot.prefix = "%"
    bot.economy = {
        "430050846999314443": 127,
        "304663636016889857": 227,
        "985856438104625162": 227,
        "989609470147579904": 227
    }

    print(f"{rgb(0, 255, 0)}Successfully loaded Database!{r}")
    await bot.modlogs.send("Successfully loaded Database!")


async def saveDatabase(bot):
    #redis = Redis(
    #    host="containers-us-west-67.railway.app",
    #    port="6998",
    #    password="oeGDqAJVBer0V1pqHJml")

    #for key in redis.scan_iter():
    #    key = await byteToString(key)
    #    value = json.dumps(getattr(bot, key), indent=4)

    #    redis.set(key, value)

    print(f"{rgb(0, 255, 0)}Successfully saved Database!{r}")

##################
# Checking Roles #
##################


async def userHasRole(user, role_id: str, bot):
    return user.has_role(role_id)


async def userHasMod(user, bot):
    return await userHasRole(user, bot.modID, bot) or await userHasRole(user, bot.adminID, bot)


async def userHasAdmin(user, bot):
    if user.id == bot.ownerID or user.id == bot.QuarlieID:
        return True


###################
# Other Functions #
###################

async def cleanID(id):
    id = str(id)
    id = id.replace("@", "")
    id = id.replace("&", "")
    id = id.replace("<", "")
    id = id.replace(">", "")
    return int(id)


def rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


r = "\033[38;2;250;220;160m"


async def addToEconomy(user_id, bot):
    if str(user_id) not in bot.economy:
        bot.economy[str(user_id)] = 100
        user = await bot.fetch_user(user_id)
        print(f"Created new economy account for {user.display_name}!")

async def byteToString(payload):
    payload = str(payload)
    payload = payload.replace("b'", "")
    payload = payload.replace("\\n", "")
    payload = payload.replace("'", "")
    return payload

async def downloadVideoFromURL(url):
    video = Downloader()
    video.url = url
    video.min = True
    video.overwrite = True
    video.filename = "redditVideo"
    video.download()
