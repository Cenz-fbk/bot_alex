import discord
import emoji

client = discord.Client()


@client.event
async def on_message(comand):
    if comand.content.startswith("!help"):
        channel = comand.channel
        await channel.send("comandos:!desenvolvedor-!regras-!description")


    if comand.content.startswith("!description"):
        channel = comand.channel
        await channel.send("""
    Óla eu sou Alex meu criador meu pediu para, explica qual meu propósito(sendo que até eu não sei ;-;)Bom estou aqui para ajudar meu criador a gerencia o servido dando informações básicas e orientando, vocês 
espero que gostem de mim né(nii-chan-❤️)""")

    if comand.content.startswith("!desenvolvedor"):
        channel = comand.channel
        await channel.send("Óla sou o programador do Alex o bot, está em desenvolvimento espero que gostem e deixem sua,opnião")

    if comand.content.startswith("!regras"):
        channel =  comand.channel
        await channel.send("Não converse com alguém sem ter permissão.")
        await channel.send("Não aceitamos qualquer tipo de preconceito.")
        await channel.send("Brincadeiras sé você tiver o minimo de intimidade com a pessoa")
    

client.run("ODMwNTM1OTEwNDYyNDU1OTA5.YHIG1w.aoetxiltTZxw7fpc5_jkCZ-VRkA")

