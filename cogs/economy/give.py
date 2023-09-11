import interactions as i

from my_utils import addToEconomy, saveDatabase

class Give(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="give",
        description="boop",
        options=[
            i.SlashCommandOption(
                name="user",
                description="Which user to give points",
                type=i.OptionType.USER,
                required=True,
            ),
            i.SlashCommandOption(
                name="amount",
                description="how many points to give",
                type=i.OptionType.INTEGER,
                required=True,
            ),
        ],
    )
    async def give(self, ctx: i.SlashContext, user, amount):
        bot = self.client
        await ctx.defer()

        author = ctx.author
        author_id = str(author.id)
        user_id = str(user.id)

        await addToEconomy(author_id, bot)  # adds user to economy if they aren't already
        await addToEconomy(user_id, bot)  # adds user to economy if they aren't already

        if amount > 0:
            if bot.economy[author_id] >= amount:
                bot.economy[author_id] -= amount
                bot.economy[user_id] += amount

                await saveDatabase(bot)
                await ctx.send(f"{author.display_name} Successfully gave {user.display_name} {amount} Points!")
                print(f"{author.display_name} Successfully gave {user.display_name} {amount} Points!")

            else:
                await ctx.send(
                    "You do not have enough Points in your Balance!")
        else:
            await ctx.send("The amount has to be over 0 Points!")