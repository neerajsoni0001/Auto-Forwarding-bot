from telethon import TelegramClient, events
from env import *
from db import *
# Create the Telethon client
bot = TelegramClient("MSG_PROD", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern="/start"))
async def handle_start(event):
    await event.respond(f"Hello {event.sender.first_name}! \n\nI'm up & running send /help to list all commands")


@bot.on(events.NewMessage(pattern="/help"))
async def handle_help_event(event):

    help_message = """Available Commands are: 
    \n\n/listsource - List all the Source Channel(s)
/listdestination - List the Destination Channel(s)
/addsource - Add a new Source Channel
/removesource - Remove a Source Channel
/adddestination - Add a new Destination Channel
/removedestination - Remove a Destination Channel
/pause - Pause the bot
/resume - Resume the bot
/postimages - Post Images with Caption
/stopimages - Stop Posting Images with Caption
/filterusername - Replace specific usernames in original message
/banurl - Ban this URL from incoming messages.
/seturl - Replace specific Cosmofeed URLs in original message
/banusername - Ban a specific username in incoming messages.
/unbanusername - Remove a username from getting banned in messages.
/setusername - Replace specific usernames in original message.
/help - Show this help message"""

    await event.respond(help_message.strip())


@bot.on(events.NewMessage(pattern="/listsource"))
async def handle_listsource_event(event):
    sources = get_all_sources()
    await event.respond(f"All Source Channels are: {sources}")


@bot.on(events.NewMessage(pattern="/listdestination"))
async def handle_listdestination_event(event):
    destinations = get_all_destinations()
    await event.respond(f"All Destination Channels are: {destinations}")


@bot.on(events.NewMessage(pattern = r"^/addsource\s+t\.me/([\w+-]+)$"))
async def handle_addsource_event(event):
    source = event.pattern_match.group(1)
    if source:
        result = add_source(source)
        await event.respond(result)
    else:
        await event.respond("Please provide a valid source channel.")



@bot.on(events.NewMessage(pattern = r"^/removesource\s+t\.me/([\w+-]+)$"))
async def handle_removesource_event(event):
    source_to_remove = event.pattern_match.group(1)
    if source_to_remove:
        result = remove_source(event.message.id, source_to_remove)
        await event.respond(result)
    else:
        await event.respond("Please provide a valid source channel to remove.")



@bot.on(events.NewMessage(pattern = r"^/adddestination\s+t\.me/([\w+-]+)$"))
async def handle_adddestination_event(event):
    destination = event.pattern_match.group(1)
    result = add_destination(destination)
    await event.respond(result)


@bot.on(events.NewMessage(pattern = r"^/removedestination\s+t\.me/([\w+-]+)$"))
async def handle_removedestination_event(event):
    destination_to_remove = event.pattern_match.group(1)
    if destination_to_remove:
        result = remove_destination(event.message.id, destination_to_remove)
        await event.respond(result)
    else:
        await event.respond("Please provide a valid destination channel to remove.")


@bot.on(events.NewMessage(pattern="/pause"))
async def handle_pause_event(event):
    result = update_status("paused")
    await event.respond(result)


@bot.on(events.NewMessage(pattern="/resume"))
async def handle_resume_event(event):
    result = update_status("running")
    await event.respond(result)


@bot.on(events.NewMessage(pattern="/postimages"))
async def handle_post_images_event(event):
    result = image_status("on")
    await event.respond(result)

@bot.on(events.NewMessage(pattern="/stopimages"))
async def handle_stop_images_event(event):
    result = image_status("off")
    await event.respond(result)


@bot.on(events.NewMessage(pattern=r"^\/banurl\s+(https?:\/\/[\w.-]+\/[\w\/.-]+)$"))
async def handle_ban_url(event):
    ban_url = event.pattern_match.group(1)
    if ban_url:
        result = insert_banned_url(ban_url)
        await event.respond(result)
    else:
        await event.respond("Please provide a valid URL to ban.")


@bot.on(events.NewMessage(pattern=r"^\/seturl\s+(https?:\/\/[\w.-]+\/[\w\/.-]+)$"))
async def handle_filter_url(event):
    update_url = event.pattern_match.group(1)
    if update_url:
        result = update_output_url(update_url)
        await event.respond(result)
    else:
        await event.respond("Please provide a valid URL to update.")


@bot.on(events.NewMessage(pattern=r"^\/banusername\s+(@\w+)$"))
async def handle_ban_username(event):
    result = insert_input_usernames(event.pattern_match.group(1))
    if result:
        await event.respond(result)
    else:
        await event.respond("Please provide a valid username to ban.")


@bot.on(events.NewMessage(pattern=r"^\/unbanusername\s+(@\w+)$"))
async def handle_unban_username(event):
    result = remove_input_username(event.pattern_match.group(1))
    if result:
        await event.respond(result)
    else:
        await event.respond("Please provide a valid username to unban.")


@bot.on(events.NewMessage(pattern=r"^\/setusername\s+(@\w+)$"))
async def handle_set_username(event):
    result = update_output_username(event.pattern_match.group(1))
    if result:
        await event.respond(result)
    else:
        await event.respond("Please provide a valid username to update.")



# Run the bot
print("Bot is running...")
bot.run_until_disconnected()
