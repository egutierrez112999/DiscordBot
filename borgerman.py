from discord.ext import commands
import discord
import asyncio
import factorial as ftl

TOKEN = "OTQ3Njg3MDkwNjAxMjA5ODk2.Yhw4YQ.aWsPyUPwAUTK4llqPsiCzku0Pm8"



#initialize bot and denote command prefix
bot = commands.Bot(command_prefix="!")


#runs when bot successfully connects
@bot.event
async def on_ready():
    print(f"{bot.user} successfully logged in!")

#@client.eventasync
#async def on_member_join(member):
#    await channel.send(f"Hello {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "hello":
        await message.channel.send(f"Hi {message.author}")
    if message.content == "bye":
        await message.channel.send(f"Goodbye {message.author}")

    await bot.process_commands(message)

#argument is text that comes after command !square <arg>
#ctx.send sends in chat

@bot.command()
async def square(ctx, arg):
    print(arg)
    await ctx.send(int(arg) ** 2)

@bot.command()
async def factorial(ctx, arg):
    print(arg)
    f = ftl.factorial(int(arg))
    await ctx.send(f)

#@bot.command()
#async def pow2(ctx):
 #   exponent = randint(0, 10)
 #   num = 2**exponent
 #   await message.channel.send(f"What is 2 to the power of {exponent}?: ")
 #   response = arg
 #   if int(response) == num:
 #       return "correct"
 #   else:
 #       return "failure"
 #   
#def power_tester(ctx, arg):
 #   score = 0
 #   for i in range(10):
 #   point = generate_two_power(arg)
 #       await message.channel.send(point)
 #   point == "correct":
 #       score+=1
 #   await ctx.send(f"Your Total Score was {score}/10")

@bot.command(pass_content=True)
async def inputtrial(ctx):
    await client.say("say yes or no")
    response = client.wait_for_message(author=ctx.message.author, timeout=30)
    if response.clean_content.lower() == 'yes': 
        await client.say('You said yes.') 
    elif response.clean_content.lower() == 'no': 
        await client.say('You said no.') 
    else: 
        await client.say("That isn't a valid response.")

bot.run(TOKEN)

