from my_utils import userHasRole, addToEconomy, saveDatabase
import interactions as i

class Ecogive(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    
    @i.slash_command(
        name="ecogive",
        description="boop",
        options=[
            i.SlashCommandOption(
                name="who",
                description="Which user or role to give points",
                type=i.OptionType.MENTIONABLE,
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
    async def ecogive(self, ctx: i.SlashContext, who, amount):
        bot = self.client
        await ctx.defer()

        print(str(type(who)))
        if "role" in str(type(who)):  # Mentioned Role ID
            id = who.id

            members = bot.server.members

            for member in members:
                if await userHasRole(member, id, bot):  # Goes through all users and checks if they have the role

                    await addToEconomy(member.id, bot)
                    bot.economy[str(member.id)] += amount

            await saveDatabase(bot)

            role = await bot.server.fetch_role(id)
            print(f"{ctx.author} gave {amount} Points to every user with the {role.name} Role")
            await ctx.send(f"Successfully given {amount} Points to every user with the {role.name} Role")

        else:  # Mentioned User ID

            member = who
            await addToEconomy(member.id, bot)
            bot.economy[str(member.id)] += amount

            await saveDatabase(bot)

            print(f"{ctx.author} gave {amount} Points to {member.display_name}")
            await ctx.send(f"Successfully given {amount} Points to {member.display_name}")