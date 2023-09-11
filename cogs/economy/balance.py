import interactions as i

from my_utils import addToEconomy


class Balance(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="balance",
        description="boop",
        options=[
            i.SlashCommandOption(
                name="user",
                description="[OPTIONAL] Which user to get the balance of",
                type=i.OptionType.USER,
                required=False,
            ),
        ],
    )
    async def balance(self, ctx: i.SlashContext, user = None):
        bot = self.client
        await ctx.defer()

        # Get proper User ID
        if user == None:
            user_id = ctx.author.id
            user = ctx.author
        else:
            user_id = user.id
            user = user

        await addToEconomy(user_id, bot)  # adds user to economy if they aren't already

        await ctx.send(f"{user.display_name} currently has {bot.economy[str(user_id)]} points!")