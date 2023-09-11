import interactions as i
from animegifs import animegifs


class Pat(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="pat",
        description="boop",
        options=[
            i.SlashCommandOption(
                name="user",
                description="[OPTIONAL] Which user to pat",
                type=i.OptionType.USER,
                required=False,
            ),
        ],
    )
    async def pat(self, ctx: i.SlashContext, user=None):
        await ctx.defer()

        gifs = animegifs.Animegifs()
        gif = gifs.get_gif("pat")

        title = f"{ctx.author.display_name} is giving out free pats"

        if user:
            title = f"{ctx.author.display_name} is patting {user.display_name}!"

        embed = i.Embed(title=title)
        embed.color = self.client.red
        embed.set_image(url=gif)

        await ctx.send(embeds=embed)