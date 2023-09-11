import interactions as i
from animegifs import animegifs


class Poke(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="poke",
        description="boop",
        options=[
            i.SlashCommandOption(
                name="user",
                description="[OPTIONAL] Which user to poke",
                type=i.OptionType.USER,
                required=False,
            ),
        ],
    )
    async def poke(self, ctx: i.SlashContext, user=None):
        await ctx.defer()

        gifs = animegifs.Animegifs()
        gif = gifs.get_gif("poke")

        title = f"{ctx.author.display_name} is gonna poke you!"

        if user:
            title = f"{ctx.author.display_name} is poking {user.display_name}!"

        embed = i.Embed(title=title)
        embed.color = self.client.red
        embed.set_image(url=gif)

        await ctx.send(embeds=embed)