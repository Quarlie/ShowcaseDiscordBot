import interactions as i
from animegifs import animegifs


class Kiss(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="kiss",
        description="boop",
        options=[
            i.SlashCommandOption(
                name="user",
                description="[OPTIONAL] Which user to kiss",
                type=i.OptionType.USER,
                required=False,
            ),
        ],
    )
    async def kiss(self, ctx: i.SlashContext, user=None):
        await ctx.defer()

        gifs = animegifs.Animegifs()
        gif = gifs.get_gif("kiss")

        title = f"{ctx.author.display_name} is gonna kiss you!"

        if user:
            title = f"{ctx.author.display_name} gave {user.display_name} a kiss!"

        embed = i.Embed(title=title)
        embed.color = self.client.red
        embed.set_image(url=gif)

        await ctx.send(embeds=embed)