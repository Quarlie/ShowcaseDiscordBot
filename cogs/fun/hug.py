import interactions as i
from animegifs import animegifs


class Hug(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="hug",
        description="boop",
        options=[
            i.SlashCommandOption(
                name="user",
                description="[OPTIONAL] Which user to hug",
                type=i.OptionType.USER,
                required=False,
            ),
        ],
    )
    async def hug(self, ctx: i.SlashContext, user=None):
        await ctx.defer()

        gifs = animegifs.Animegifs()
        gif = gifs.get_gif("hug")

        title = f"{ctx.author.display_name} is gonna hug you!"

        if user:
            title = f"{ctx.author.display_name} is hugging {user.display_name}!"

        embed = i.Embed(title=title)
        embed.color = self.client.red
        embed.set_image(url=gif)

        await ctx.send(embeds=embed)