from .. import zbot
from telethon import events, Button

@zbot.on(events.NewMessage(incoming=True, pattern="/start"))
async def kk(event):
  k = [[Button.url('Powered By', 't.me/ZYPHERxBOTZ')]]
  if event.sender_id == SUDO_USER:
    return await event.reply('Get Master type /help to know commands')
  else:
    return await event.reply('stay away fucker')
