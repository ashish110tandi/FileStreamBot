# (c) @AvishkarPatil | @EverythingSuckz

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('API_ID', '11004381'))
    API_HASH = str(getenv('API_HASH', '8e0588044fcf7672cfe1341185bfc94c'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '5678837203:AAFYUqUYoxdEPSKjVGJPWcdOYjZn3D1wQCo'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'BQCn6d0AOpqIw4Gnyi0lj3BjF_AF6det4xXEeomkMgS4vkyeNyJwbO8iN2RqQqG7iWazBUWamXfwXjNLNTbC11axbuqTwvoLkV9KxXDVIICGa4ntXvv2KINFHwSS_A9dABwzDYsPYaUgsnoZhTxktL8R4hUaFu4_rRtlCjNeykyQqQnHBQz9tx3pV_YGi46CimyV4AIjJ9xEz9J3-1Czs9lhO-i8C2e32RfxOaajoTXAqWN54frep2RpxVedE88-sZlzuB05L6TTJ2zUE5hgMfJ7cwy6SFOkvsADVqI7dLMp9J4cVt4EoYiFIS5iyIBy9UDz_dm12QvrMmNpWn19QGrzYmz_BAAAAABLJNQ2AA'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001585763504'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = int(getenv('OWNER_ID', '1260704822'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
        "http://{}:{}/".format(FQDN, PORT)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://ashishtandi:ashishtandi@cluster0.p2gli.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'))
    PING_INTERVAL = int(getenv('PING_INTERVAL', '500'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))
