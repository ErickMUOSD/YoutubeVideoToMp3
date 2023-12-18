import clipboard
import asyncio
import re

REGEX = "^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$"
FILE_DESTINATION = "clipboard.txt"
URL_IN_MEMORY = []
# Exemple function.
async def save_valid_url(url):

    print("Running...")
    with open(FILE_DESTINATION, 'a') as outfile:
        outfile.write(f"{url}\n")
        print("Done")


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
            if value in URL_IN_MEMORY:
                print('Already saved')
                continue
            URL_IN_MEMORY.append(value)
            asyncio.create_task(save_valid_url(value)) #Start your function.
        else:
            print("Not a youtube link")
asyncio.run(main())