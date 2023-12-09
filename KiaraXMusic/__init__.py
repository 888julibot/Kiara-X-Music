from KiaraXMusic.core.bot import Kiara
from KiaraXMusic.core.dir import dirr
from KiaraXMusic.core.git import git
from KiaraXMusic.core.userbot import Userbot
from KiaraXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Kiara()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
