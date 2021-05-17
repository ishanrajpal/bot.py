from logging import exception
import discord
from discord import channel
from discord.ext import commands
from discord.ext.commands.core import guild_only
from discord.utils import get
import youtube_dl
import os
from os import system
from discord import Spotify
import shutil
import spotipy

intents = discord.Intents.all()
client = commands.Bot(command_prefix='', intents=intents)
client.remove_command('help')

global name


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Use help/info'))
    print(f'We have logged in as {client.user}')
    await client.get_channel(723567223192420446).send("Update Deployed For killerfrost")

@client.event
async def on_member_join(member):
    guild=member.guild
    embed=discord.Embed(title="Welcome to",color=0x9208ea,description=f"{guild}")
    await member.send(content=None, embed=embed)        
    #await member.send(str(f'welcome to {guild}'))
    #await member.send(str(f'welcome to {channel}'))
    for channel in member.guild.channels:
        if str(channel) == "welcome":
            #await channel.send(f"""Welcome to the server {member.mention}""")
            #await member.dm_channel.send(str(f"{mention},Welcome to the server{guild}").format(mention=mention,guild=guild))
            #embed.add_field(name="Total Members in this Server is:",value=f" {member_count}")
            #member_count = len(channel.guild.members)
            embed=discord.Embed(title="Welcome to the server",color=0x9208ea,description=f"{member.mention}")
            show_avatar = discord.Embed(
            color = discord.Color.dark_blue()
            )
            show_avatar.set_image(url='{}'.format(member.avatar_url))
            await channel.send(embed=show_avatar)
            await channel.send(content=None, embed=embed)
@client.event
async def on_member_remove(member):
    #try:

    print(f'{member} has left a server.')
    for channel in member.guild.channels:                   #change
        if str(channel) == "general":
            await channel.send(f"""Sayonara{member.mention}""")
            await channel.send("Member -= 1")
            member_count = len(channel.guild.members)
            await channel.send(f"""Total Members in this Server is: {member_count}""")
        guild=member.guild
        embed=discord.Embed(title="We will miss you",color=0x9208ea,description=f"{guild}")
        await member.send(content=None, embed=embed) 
    #except exception as l:
     #   await channel.send(f"{member.mention}Sayonara")
      #  print(f'{member}has left a server.')
       # return(member) 


#@client.event
#async def on_member_remove(member):
 #   embed=discord.Embed(title="We will miss you",color=0x9208ea,description=f"{guild}")
  #  await member.send(content=None, embed=embed)        
   # print(f'{member} has left a server.')
    #for channel in member.guild.channels:                   
     #   if str(channel) == "general":
      #      embed=discord.Embed(title="Sayonara",color=0x9208ea,description=f"{member.mention}")
            #show_avatar = discord.Embed(
            #color = discord.Color.dark_blue()
           # )
            #show_avatar.set_image(url='{}'.format(member.avatar_url))
           # await channel.send(embed=show_avatar)
       #     await channel.send(content=None, embed=embed)
            #await channel.send(f"""Sayonara{member.mention}""")
            #embed.add_field(name="Member",value="-1")
            #member_count = len(channel.guild.members)
            #embed.add_field(name="Total Members in this Server is:",value=f" {member_count}")
            #await channel.send(content=None, embed=embed)
@client.command()
async def nikal(ctx, member : discord.Member, *,reason=None):
    await ctx.channel.purge(limit=2)
    await member.kick(reason=reason)
    await ctx.send(f'kicked{member.mention}')
@client.command()
async def ping(ctx):                        
    #await ctx.send(f"Your ping is :{round(client.latency * 1000)} ms")
    embed=discord.Embed(title="Your ping is",color=0x9208ea,description=f"{round(client.latency * 1000)} ms")
    await ctx.send(content=None, embed=embed)      

@client.command()
async def avatar(ctx, member: discord.Member):
    show_avatar = discord.Embed(

        color = discord.Color.dark_blue()
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)
@client.command()
async def abrakadabra(ctx,amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def khela(ctx):
    await ctx.channel.send("if you want to play you can call me")
   
@client.command()
async def aaja(ctx):
    await ctx.channel.send("if you want to play you can call me")

@client.command()
async def phone(ctx):
    await ctx.channel.send("if you don't have my Phone no Then don't Bothere")

@client.command()
async def what(ctx):
    await ctx.channel.send("nothing")

@client.command()
async def users(ctx):
    member_count = len(ctx.guild.members)
    await ctx.channel.send(f"""Total Members in this Server is: {member_count}""")
@client.command()
async def hi(ctx):
    await ctx.channel.send("hello")
@client.command()
async def no(ctx):
    await ctx.channel.send("ok")
@client.command()
async def all(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.channel.send("@everyone Khele?")
  
@client.command()
async def help(ctx):  
    embed = discord.Embed(title="What can killer Frost do?",description="Some useful commands")
    embed.add_field(name="hi",value="Greets the user")
    embed.add_field(name="users",value="Prints no of users")
    embed.add_field(name="khela",value="message")
    embed.add_field(name="join",value="add bot to voice channel")
    embed.add_field(name="leave",value="remove bot from voice channel")
    embed.add_field(name="play youtube/Spotify link..",value="play the song")   ##to be 
    embed.add_field(name="pause",value="pause the song")
    embed.add_field(name="resume",value="resume the song")
    embed.add_field(name="stop",value="stop the song")
    embed.add_field(name="info",value="some basic details")
    embed.add_field(name="all",value="mention everyone to play")
    embed.add_field(name="avatar@user",value="pop up his/her display")
    
    
    embed.add_field(name="ping",value="Tells you ping/Current Latency")
    
    await ctx.channel.send(content=None, embed=embed)
@client.command()
async def git(ctx):
    await ctx.channel.send("https://github.com/ishanrajpal")

@client.command()
async def info(ctx):  
    embed = discord.Embed(title="About Killerfrost?",description="Some details")
    embed.add_field(name="Owner",value="Ishan rajpal")
    embed.add_field(name="Creater Discord I'd",value='UchihaMadara#9884')        ##
    embed.add_field(name="Main server",value="Hellplay")
    embed.add_field(name="Github",value="https://github.com/ishanrajpal")                        ##to be added
    embed.add_field(name="Capabilities",value="play music and do some stuffs")
    embed.add_field(name="Instagram",value="ishan_rajpal")
    await ctx.channel.send(content=None, embed=embed)
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('valid command use karo please')

@client.command()
async def chutia(ctx):
    await ctx.channel.send("Tu chutia")
@client.command(pass_context=True,aliases=['j', 'Join'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"the bot is connected to {channel}\n")

    await ctx.send(f"joined{channel}")

@client.command(pass_context=True)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    
    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"the bot has left{channel}")
        await ctx.send(f"left{channel}")
    else:
        print("not in one")
        await ctx.send("not in one")

@client.command(pass_context=True)
async def play(ctx, url: str):
    
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file,but it is being played")
        await ctx.send("Error: Music playing")
        return
    
    await ctx.send("Getting everything ready now")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format':'bestaudio/best',
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192',
        }],
    }
    
    try:    
       with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([url])
            pass
    except Exception as o:
        print("Fallback: youtube-dl does not support this url ,using spotify")
        system("spotdl -f " + '"' + "./" + '"' + " -s " + url +" -i " +"automatic")
        
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")
    
    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Played the song"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.9

    try:
        nname = name.rsplit("-", 2)
        await ctx.send(f"Playing: {nname[0]}")
    except:
        await ctx.send(f"Playing Song")

    print("playing\n")
    await ctx.send(f"Playing: {nname[0]}")
    
@client.command(pass_context=True, aliases=['p', 'pau'])
async def pause(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music Paused")
        voice.pause()
        await ctx.send("Music paused")
    else:
        print("Music not playing failed pause")
        await ctx.send("Music not playing failed pause ")

@client.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print("Resumed music")
        voice.resume()
        await ctx.send("Resumed music")
    else:
        print("Music is not pause")
        await ctx.send("Music is not pause ")

@client.command(pass_context=True, aliases=['s', 'sto'])
async def stop(ctx):

    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print("Music Stopped")
        voice.stop()
        await ctx.send("Music Stopped")
    else:
        print("No Music playing failed to Stop")
        await ctx.send("No Music playing failed to Stop")

client.run(os.environ['Discord_token'])

