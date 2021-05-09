import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Hazir ve Nazir, Sir')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.ğ'):
        await message.channel.send('Ğ')

    if message.content.startswith('.engin'):
        await message.channel.send('https://i.imgur.com/AkSgxrm.jpg')

    if message.content.startswith('.music'):
        await message.channel.send('https://open.spotify.com/playlist/6VJFobUvRw2l36ypJk8YpS?si=44c221743dde4267')

    if message.content.startswith('31'):
        await message.channel.send('https://www.memesmonkey.com/images/memesmonkey/43/43724deb70139932dd8ddd92005e3ebc.jpeg')

    if message.content.startswith('akın'):
        await message.channel.send('Nasılım?')

    if message.content.startswith('.bakruu'):
        await message.channel.send('https://media.discordapp.net/attachments/715115812930977867/837039187412516944/162931981_277935690440226_3073440298636252425_n.jpg?width=682&height=682')

    if message.content.startswith('selam'):
        await message.channel.send('Selamlar Dostum!')

    if message.content.startswith('selamlar'):
        await message.channel.send('Selamlar Dostum!')

    if message.content.startswith('iyi geceler'):
        await message.channel.send('Tatlı Rüyalar!')

    if message.content.startswith('ig'):
        await message.channel.send('Tatlı Rüyalar!')














client.run('Nzg5NTA3NTYxOTU4MTQ2MDkw.X9zENw.LV_X02VHlMP9ErbUXzEVQ17Cy2U')