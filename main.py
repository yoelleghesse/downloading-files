url = "https://filesamples.com/samples/audio/mp3/Symphony%20No.6%20(1st%20movement).mp3"

import requests

req = requests.get(url)
content = req.content

with open('dowload.mp3', 'wb') as file:
  file.write(content)