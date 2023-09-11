from PIL import Image, ImageFont, ImageDraw
import requests

import interactions as i

class Test(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="test",
        description="boop",
    )
    async def test(self, ctx: i.SlashContext):
        bot = self.client
        await ctx.defer()

        path = bot.path+"image/MemberCard/"
        user = await bot.fetch_user(ctx.author.id)
        url = user.avatar_url

        img = Image.open(path+"blank.png")
        profilePic = Image.open(requests.get(url, stream=True).raw)
        font = ImageFont.truetype(path+"comici.ttf", 16)

        authorText = f"Your name is {ctx.author.display_name}"
        pointsText = f"You currently have {str(bot.economy[str(ctx.author.id)])} Points!"
        
        txt = Image.new('RGBA', img.size, (255,255,255,0))
        txtDraw = ImageDraw.Draw(txt) 

        profilePic = profilePic.resize((250, 250))

        img = img.convert("RGBA")
        profilePic = profilePic.convert("RGBA")

        img.paste(profilePic, (0, 50), profilePic)
        
        txtDraw.text((0, 0), authorText, fill=(0, 0, 0, 255), font=font)
        txtDraw.text((0, 24), pointsText, fill=(0, 0, 0, 255), font=font)

        combined = Image.alpha_composite(img, txt)
        combined.save("membercard.png")

        files=[i.File(bot.path+"membercard.png")]
        await ctx.send(files=files)