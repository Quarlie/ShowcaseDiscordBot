import interactions as i
from animegifs import animegifs


class Dance(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="dance",
        description="boop",
        options=[
            i.SlashCommandOption(
                name="user",
                description="[OPTIONAL] Which user to dance with",
                type=i.OptionType.USER,
                required=False,
            ),
        ],
    )
    async def dance(self, ctx: i.SlashContext, user=None):
        await ctx.defer()

        gifs = animegifs.Animegifs()
        gif = gifs.get_gif("dance")

        title = f"{ctx.author.display_name} is dancing for all of you!"

        if user:
            title = f"{ctx.author.display_name} is dancing with {user.display_name}!"

        embed = i.Embed(title=title)
        embed.color = self.client.red
        embed.set_image(url=gif)

        await ctx.send(embeds=embed)