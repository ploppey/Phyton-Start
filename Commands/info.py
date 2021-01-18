import discord
from discord.ext import commands

from utils import default

botcolor = 0xFF0040 #type in your color.


class info(info.Cog):
    def __init__(self, bot):
        self.bot = bot
    
###############################################################################################################################################################################   
    @commands.command()
    async def user(self, ctx, *, user: discord.Member = None):
        user = user or ctx.author

        show_roles = ', '.join(
            [f"<@&{x.id}>" for x in sorted(user.roles, key=lambda x: x.position, reverse=True) if
             x.id != ctx.guild.default_role.id]
        ) if len(user.roles) > 1 else 'None'

        embed = discord.Embed(colour=user.top_role.colour.value)
        embed.set_thumbnail(url=user.avatar_url)

        embed.add_field(name="Full name", value=user, inline=True)
        embed.add_field(name="Nickname", value=user.nick if hasattr(user, "nick") else "None", inline=False)
        embed.add_field(name="Account created", value=default.date(user.created_at), inline=False)
        embed.add_field(name="Joined this server", value=default.date(user.joined_at), inline=False)
        embed.add_field(name="Roles", value=show_roles, inline=False)

        await ctx.send(content=f"ℹ About **{user.id}**", embed=embed)
        
###############################################################################################################################################################################   

def setup(bot):
    bot.add_cog(info(bot))
