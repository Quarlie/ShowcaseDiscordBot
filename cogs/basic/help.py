import json, os

import interactions as i
from interactions.api.events import Component
from my_utils import userHasMod, userHasAdmin

class Help(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    length = 0
    reply = i.Message
    reply.cur = 0

    @i.slash_command(
        name="help",
        description="boop",
        options=[
            i.SlashCommandOption(
                name="subcommand",
                description="get help on a specific command",
                type=i.OptionType.STRING,
                required=False
            )
        ]
    )
    async def help(self, ctx, subcommand = None):
        bot = self.client
        await ctx.defer(ephemeral=True)
        subcom = subcommand

        buttonBack = i.Button(
            style=i.ButtonStyle.PRIMARY,
            label="<-",
            custom_id="back",
        )

        buttonForward = i.Button(
            style=i.ButtonStyle.PRIMARY,
            label="->",
            custom_id="forward",
        )

        buttons = [buttonBack, buttonForward]

        author = ctx.author

        helpPath = bot.path + "data/constants/help.json"

        helpFile = open(helpPath, "r")
        helpDict = json.loads(helpFile.read())

        self.length = len(helpDict)-1

        if not userHasMod(author.id, bot):
            self.length = self.length - 1

        reply = await ctx.send(content="boop", components=buttons)

    @i.listen(Component)
    async def on_component(self, event: Component):
        ctx = event.ctx

        dict = {}

        for cogDir in os.listdir("./cogs"):
            dict[str(cogDir)] = {}
            for filename in os.listdir(f"./cogs/{cogDir}"):
                if filename.endswith(".py"):
                    for command in self.bot.application_commands:
                        if(str(command.name) == filename[:-3]):
                            dict[str(cogDir)][str(command.name)] = {}
                            text = "/"+str(command.name) + " "
                            if(command.options):
                                for option in command.options:
                                    if option.required:
                                        text += "<"
                                    else:
                                        text += "["

                                    text += str(option.name)

                                    if option.required:
                                        text += ">"
                                    else:
                                        text += "]"
                                    text += " "
                            dict[str(cogDir)][str(command.name)]["command"] = text
                            dict[str(cogDir)][str(command.name)]["description"] = str(command.description)

        print(dict)

        """
        
        {
            "Economy" : {"balance" : "text", "give": "", "top" : ""},
            
        
        }
        
        
        
        if ctx.custom_id == "back":

            ctx.message.cur -= 1
            ctx.edit(message=ctx.message, content="test1")
            print(ctx.message.cur)

        elif ctx.custom_id == "forward":

            ctx.message.cur += 1
            print(ctx.message.cur)
            ctx.edit(message=ctx.message, content="test2")"""
    async def HelpMessage(self, page:int, maxLength:int):
        return " "