import interactions as i
from animegifs import animegifs


class Flirt(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="flirt",
        description="boop",
        options=[
            i.SlashCommandOption(
                name="user",
                description="[OPTIONAL] Which user to flirt with",
                type=i.OptionType.USER,
                required=False,
            ),
        ],
    )
    async def flirt(self, ctx: i.SlashContext, user=None):
        await ctx.defer()

        gifs = animegifs.Animegifs()
        gif = gifs.get_gif("flirt")

        title = f"{ctx.author.display_name} is flirting with all of you!"

        if user:
            title = f"{ctx.author.display_name} is flirting with {user.display_name}!"

        embed = i.Embed(title=title)
        embed.color = self.client.red
        embed.set_image(url=gif)

        await ctx.send(embeds=embed)