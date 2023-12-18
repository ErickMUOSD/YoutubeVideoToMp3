import clipboard
import asyncio
import re

REGEX = "^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
FILE = "clipboard.txt"
# Exemple function.
async def your_function():

    print("Running...")


async def wait4update(value):
    while True:
        if clipboard.paste() != value : # If the clipboard changed.
            return

async def main():
    value = clipboard.paste() # Set the default value.
    while True :
        update = asyncio.create_task(wait4update(value))
        await update
        value = clipboard.paste() # Change the value.
        if re.match(REGEX,value):
            asyncio.create_task(your_function()) #Start your function.
        else:
            print("Not a youtube link")

asyncio.run(main())