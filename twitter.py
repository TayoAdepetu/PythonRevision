import re

url = input("What's your twitter profile url? ").strip()

# find and replace using reg expression
# username = re.sub(r"^(https?://(www\.)?)?twitter\.com/", "", url)

# username = url.replace("https://twitter.com/","")

# username = url.removeprefix("https://twitter.com/")

# capture the user's username as a group
matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    # print what was captured, knowing that it's at the second group inside the reg expression
    print(f"Your username is ", matches.group(2))

# OR - changing the group and also trying to customize the username part to exactly what twitter uses
matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE)
if matches:
    # print what was captured, knowing that it's at the first group inside the reg expression
    print(f"Your username is ", matches.group(1))

