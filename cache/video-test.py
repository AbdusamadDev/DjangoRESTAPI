# import os

with open("testing.mp4", mode="rb") as video:
    content = video.read()
    with open("video.mp4", mode="wb") as file:
        file.write(content)

# Success!
# It did work as I expected/