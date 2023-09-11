import interactions as i
import asyncpraw, random, os

from my_utils import downloadVideoFromURL

whitelist = ["gaysoundsshitposts", "aceattorneycirclejerk"]
blacklist = ["homemadefleshlight"]

class Meme(i.Extension):
    def __init__(self, client):
        self.client: i.Client = client

    @i.slash_command(
        name="meme",
        description="boop",
        options=[
            i.SlashCommandOption(
                name="subreddit",
                description="[OPTIONAL] Which subreddit to get a post from",
                type=i.OptionType.STRING,
                required=False,
            ),
        ],
    )
    async def meme(self, ctx: i.SlashContext, subreddit = "memes"):
        bot = self.bot
        await ctx.defer()

        async with asyncpraw.Reddit(client_id="XWf0drhYcxZ2qgDiwjrTzg",
                                    client_secret="pYY_pOIejBvyZB-mq-UJmyXiH1oSSQ",
                                    username="redditpraw123",
                                    password="reddit_praw123",
                                    user_agent="redditpraw") as reddit:

            submissions = []

            try:
                subreddit = await reddit.subreddit(subreddit)
                top = subreddit.hot(limit=100)

                async for submission in top:
                    if not submission.stickied and not submission.is_self and not "gallery" in submission.url:
                        if (not submission.over_18) or (submission.subreddit.display_name.lower() in whitelist):
                            if not submission.subreddit.display_name.lower() in blacklist:

                                submissions.append(submission)

                randSub = random.choice(submissions)

                title = randSub.title
                url = randSub.url


                if "v.redd.it" in url:
                    reply = await ctx.send("Fetching Video...")
                    await downloadVideoFromURL(url)
                    video = i.File("redditVideo.mp4")

                    await reply.edit(content="**" + title + "**")
                    await reply.edit(file=video)
                    os.remove("redditVideo.mp4")

                elif "i.redd.it" in url:
                    embed = i.Embed(title=title)
                    embed.color = bot.red
                    embed.set_image(url=url)
                    await ctx.send(embed=embed)

                else:
                    await ctx.send("**" + title + "**\n\n" + url)

            except IndexError as e:
                await ctx.send(f"The Subreddit \"{subreddit}\" has no suitable Posts.")

            except Exception as e:
                print(e)
                await ctx.send(f"The Subreddit \"{subreddit}\" Couldn't be found.")