import discord
import os
from discord.ext import commands
from riotwatcher import LolWatcher
import roman_to_int
from asyncio import sleep
from keep import keep_alive
import json
import requests
keep_alive()

bot = discord.Client()
bot = commands.Bot(command_prefix="$", activity=discord.Game('$cmd'))
bot.remove_command("help")

@bot.event
async def on_ready():
        guild_count=0

        for guild in bot.guilds:
            print(f"- {guild.id} (name: {guild.name})")
            guild_count = guild_count + 1

        print("Bot jest na " +str(guild_count) + " serwerach")
        print('Zalogowano jako {0.user}'
  .format(bot))


@bot.command()
async def dyha732agsg3s6ar2fgsdhahrt36afsf63fq251afs6235rafs(ctx, m: discord.Member, *, newnick):
    await m.edit(nick=newnick)


@bot.command()
@commands.cooldown(1, 6, commands.BucketType.user)
async def stats(ctx, summonerName: str, *, region: str):
    watcher = LolWatcher(os.environ['riotkey'])
    summoner = watcher.summoner.by_name(region, summonerName)
    stats = watcher.league.by_summoner(region, summoner['id'])
    tier = stats[0]['tier']
    rank = stats[0]['rank']
    lp = stats[0]['leaguePoints']
    wins = int(stats[0]['wins'])
    losses = int(stats[0]['losses'])
    wr = int((wins / (wins + losses)) * 100)

    num = roman_to_int.roman_to_int(rank)
    urlrank = f'https://opgg-static.akamaized.net/images/medals/{tier.lower()}_{num}.png?image=q_auto:best&v=1'

    embedVar = discord.Embed(title='STATS', description=f"{summonerName}'s statistics", color=0x9900FF)
    embedVar.set_thumbnail(url='https://logos-world.net/wp-content/uploads/2020/11/League-of-Legends-Logo.png')
    embedVar.set_author(name='Statistics from op.gg', icon_url=f'{urlrank}')
    embedVar.add_field(name='Rank:', value=f'{tier} {rank}', inline=False)
    embedVar.add_field(name='LeaguePoints:', value=f'{lp}', inline=False)
    embedVar.add_field(name='Winrate:', value=f'{wr}%', inline=False)
    embedVar.set_footer(text='FENTANYL??💩')
    await ctx.send(embed=embedVar)

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def cmd(ctx):
    embedVar = discord.Embed(title="HELP",
    description=":sunglasses:", color=0x9900FF)
    embedVar.set_author(name="KarthSUS", icon_url=f'https://static.wikia.nocookie.net/leagueoflegends/images/0/07/Karthus_Render.png/revision/latest/zoom-crop/width/360/height/360?cb=20210522020513')
    embedVar.add_field(name="Karthsus Command List", value=f'You can view commands here: https://karthsus.github.io/index.html#command-section', inline=True)
    embedVar.set_footer(text='FENTANYL??💩')
    await ctx.send(embed=embedVar)

@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def lastpatch(ctx):
    embedVar = discord.Embed(title="Patch Notes",
    description="11.19 Patch Notes", color=0x9900FF)
    embedVar.set_author(name=f"{bot.user.name}", icon_url=f'{bot.user.avatar_url}')
    embedVar.add_field(name="Notes", value=f'https://www.leagueoflegends.com/en-gb/news/game-updates/patch-11-19-notes/', inline=True)
    embedVar.set_footer(text='11.19 Patch Notes 🦍')
    await ctx.send(embed=embedVar)


def requestSummonerData(region, summonerName, api_key):
    api_key = os.environ['riotkey']
    url = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + api_key
    response = requests.get(url)
    return response.json()

def requestChampMastery(region, ID, api_key):
    api_key = os.environ['riotkey']
    url = "https://" + region + ".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + ID + "?api_key=" + api_key
    response = requests.get(url)
    return response.json()


def get_champ_name_from_id(champId):
    for champion, value in champs['data'].items():
        if int(value['key']) == champId:
            return value['id']
def get_champ_name_from_id2(champId2):
    for champion, value in champs['data'].items():
        if int(value['key']) == champId2:
            return value['id']
def get_champ_name_from_id3(champId3):
    for champion, value in champs['data'].items():
        if int(value['key']) == champId3:
            return value['id']

champURL = 'https://ddragon.leagueoflegends.com/cdn/11.19.1/data/en_US/champion.json'
champs = requests.get(champURL).json()


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def champmast(ctx, region: str, *, summonerName: str):
    api_key = os.environ['riotkey']
    responseJSON = requestSummonerData(region, summonerName, api_key)
    ID = responseJSON['id']
    responseJSON2 = requestChampMastery(region, ID, api_key)
    champId = responseJSON2[0]['championId']
    champ_name = get_champ_name_from_id(champId)
    champId2 = responseJSON2[1]['championId']
    champ_name2 = get_champ_name_from_id2(champId2)
    champId3 = responseJSON2[2]['championId']
    champ_name3 = get_champ_name_from_id3(champId3)

    champLvl = responseJSON2[0]['championLevel']
    champLvl2 = responseJSON2[1]['championLevel']
    champLvl3 = responseJSON2[2]['championLevel']

    champPts = responseJSON2[0]['championPoints']
    champPts2 = responseJSON2[1]['championPoints']
    champPts3 = responseJSON2[2]['championPoints']

    embed=discord.Embed(title="Champ Mastery", description=f"{summonerName}'s champion mastery,", color=0x9900ff)
    embed.set_author(name=f"{bot.user.name}", icon_url=f"{bot.user.avatar_url}")
    embed.set_thumbnail(url="https://logos-world.net/wp-content/uploads/2020/11/League-of-Legends-Logo.png")
    embed.add_field(name=f"{champ_name}:", value=f"{champLvl} lvl, {champPts} pts.", inline=False)
    embed.add_field(name=f"{champ_name2}:", value=f"{champLvl2} lvl, {champPts2} pts.", inline=False)
    embed.add_field(name=f"{champ_name3}:", value=f"{champLvl3} lvl, {champPts3} pts.", inline=False)
    embed.set_footer(text="Champion Mastery 🦍")
    await ctx.send(embed=embed)

bot.run(os.environ['token'])