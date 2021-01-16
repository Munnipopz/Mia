# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os

def get_user_list(config, key):
    with open('{}/miakhalifa/{}'.format(os.getcwd(), config), 'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1594860543:AAHm9EixopNqeJIm2J-r0MbymnnZuuasPi8"
    OWNER_ID = "984441749"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "Munnipopz"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://eyofrnogltxmwz:9f85e8584199a374615a67bfe18f73edc4afaf9451d16eed3aee5b179708589b@ec2-54-243-195-160.compute-1.amazonaws.com:5432/d325npis91qikn'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    GBAN_LOGS = None
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None
    FILTER_LIMIT = os.environ.get('FILTER_LIMIT', None)

    # OPTIONAL
    #ID Seperation format [1,2,3,4]
    SUDO_USERS = get_user_list('984441749.984441749', '984441749')  # List of id's -  (not usernames) for users which have sudo access to the bot.
    DEV_USERS = get_user_list('984441749.984441749', '984441749')  # List of id's - (not usernames) for developers who will have the same perms as the owner
    SUPPORT_USERS = get_user_list('984441749.984441749', '984441749')  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = get_user_list('984441749.984441749', '984441749')  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    SPAMMERS = None
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    STRICT_GMUTE = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAACAgUAAxkBAAIEAl\_\_0GhPXB2TE3pZMragow7ZMOC9AAIoAAOVY606hdlQdCOk4DseBA'  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as /
    CASH_API_KEY = None # Get one from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = None # Get one from https://timezonedb.com/register
    WALL_API = None
    LASTFM_API_KEY = None
    LYDIA_API = None
    API_OPENWEATHER = None
    
   
  
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
