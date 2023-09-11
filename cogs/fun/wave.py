import interactions as i
from animegifs import animegifs


class Wave(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="wave",
        description="boop",
        options=[
            i.SlashCommandOption(
                name="user",
                description="[OPTIONAL] Which user to greet",
                type=i.OptionType.USER,
                required=False,
            ),
        ],
    )
    async def wave(self, ctx: i.SlashContext, user=None):
        await ctx.defer()

        gifs = animegifs.Animegifs()
        gif = gifs.get_gif("wave")

        title = f"{ctx.author.display_name} is greeting all of you!"

        if user:
            title = f"{ctx.author.display_name} is waving at {user.display_name}!"

        embed = i.Embed(title=title)
        embed.color = self.client.red
        embed.set_image(url=gif)

        await ctx.send(embeds=embed)