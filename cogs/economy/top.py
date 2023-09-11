import copy
import interactions as i

class Top(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="top",
        description="boop",
    )
    async def top(self, ctx: i.SlashContext):
        bot = self.client
        await ctx.defer()

        ecoCopy = copy.deepcopy(bot.economy)
        topList = []
        topNum = 5

        if(len(ecoCopy) < topNum):
            topNum = len(ecoCopy)
    
        curTop = [None, -100000]
    
        for j in range(topNum):
            for key, value in ecoCopy.items():
                if value > curTop[1]:
                    curTop[0] = key
                    curTop[1] = value
    
            topList.append(curTop[0])
            del ecoCopy[curTop[0]]
    
            curTop = [None, -100000]
    
        finString = ""
    
        for j in range(topNum):
            user = await bot.fetch_user(int(topList[j]))
            finString += f"{j + 1}. {user.display_name} with {bot.economy[str(topList[j])]} points!"

    
            if (j != topNum - 1):
                finString += "\n"

        embed = i.Embed()
        embed.color = bot.red
        embed.add_field(name="Top Users", value=finString)
        await ctx.send(embeds=embed)