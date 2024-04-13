import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesion con {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un {bot.user} y fui creado para dar consejos de la contaminacion!')


consejo = [
    'Usa bolsas reutilizables para tus compras',
    'Evita los productos de un solo uso como sorbetes y cubiertos de plastico',
    'opta por caminar, andar en bicicleta o trasporte publico en lugar de conducir solo un automovil',
    'separa tus residuos en reciclables y no reciclables y asegurate de utilizar contenedores de reciclaje adecuado',
    'cierra el grifo mientras lavas los platos, te cepilles los dientes o enjabones en la ducha para ahorrar agua',
]
@bot.command()
async def consejodeldia(ctx):
    consejo = random.choice(consejo)
    await ctx.send(consejo)

# Funcion que explica que es la contaminacion
@bot.command()
async def contaminacion(ctx):
    definicion = "La contaminacion es la introduccion de sustancias o agentes nocivos en el medio ambiente, causando efectos addversos en la calidad del aire, agua y suelo, asi como en la salud de los seres vivos"
    await ctx.send(definicion)

materiales = {
    'platico': random.randint(100, 1000), #Tiempo de degradación de 100 y 1000 años
    'neumatico': random.randint(500, 1000),  
    'Metal': random.randint(20,90),  
    'Vidrio': random.randint(4000), 
}
bot.command()
async def consejodeldia(ctx):
    consejo = random.choice(materiales)
    await ctx.send(consejo)

bot.run("token")
