import asyncio
from utilities import utilities


async def run(message, matches, chat_id, step, crons=None):
    response = []
    if not (message.out):
        message = await message.reply(matches)
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌖▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌍▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌒▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️🌖▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌏▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️🌒▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️🌖▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌎▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️🌒▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️🌖▪️\r\n▪️▪️▪️🌍▪️▪️▪️\r\n▪️🌒▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️🌒▪️🌎▪️🌖▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️🌒▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌏▪️▪️▪️\r\n▪️▪️▪️▪️▪️🌖▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️🌒▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌍▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️🌖▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️🌒▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌏▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️🌖▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌒▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌎▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌖▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️🌒▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌍▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️🌖▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️🌒▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌎▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️🌖▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️🌒▪️\r\n▪️▪️▪️🌏▪️▪️▪️\r\n▪️🌖▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️🌖▪️🌍▪️🌒▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️🌖▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌎▪️▪️▪️\r\n▪️▪️▪️▪️▪️🌒▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️🌖▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌏▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️🌒▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️🌖▪️▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌎▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️▪️🌒▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    msg = "▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌖▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌍▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️\r\n▪️▪️▪️🌒▪️▪️▪️\r\n▪️▪️▪️▪️▪️▪️▪️"
    response.append(message.edit(msg))
    response.append(asyncio.sleep(0.5))
    return response


plugin = {
    "name": "Earth Animation",
    "desc": "Earth with moon and sun turn around it.",
    "usage": ["[!/#]earth Earth with moon and sun turn around it."],
    "run": run,
    "sudo": True,
    "patterns": ["^[!/#]earth$"],
}

