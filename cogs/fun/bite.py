import interactions as i
from animegifs import animegifs


class Bite(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="bite",
        description="boop",
        options=[
            i.SlashCommandOption(
                name="user",
                description="[OPTIONAL] Which user to bite",
                type=i.OptionType.USER,
                required=False,
            ),
        ],
    )
    async def bite(self, ctx: i.SlashContext, user=None):
        await ctx.defer()

        gifs = animegifs.Animegifs()
        gif = gifs.get_gif("bite")

        title = f"{ctx.author.display_name} is gonna bite you!"

        if user:
            title = f"{ctx.author.display_name} bit {user.display_name}!"

        embed = i.Embed(title=title)
        embed.color = self.client.red
        embed.set_image(url=gif)

        await ctx.send(embeds=embed)