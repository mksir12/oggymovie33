class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "23648338"
    API_HASH = "9b23c1dda0eaf6c48758d4c1e6ae9fe0"

    CASH_API_KEY = "EQ89V39Q0K1S4L9Y"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://vjcofnotoigdas:e40082098bc94b6ac369d40241a73f958a8ebd5afa534d3e4452ca194500df6e@ec2-35-170-235-128.compute-1.amazonaws.com:5432/dbp9j8d25vh2jv"  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1001918056749"  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://OGGYYTT:OGGYYTT@cluster0.yfmak7z.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://graph.org/file/25f27d052ee9bbc7a6c8c.jpg"

    SUPPORT_CHAT = "DevilsHeavenMF"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6157233938:AAGc76r7huHiH1obASDbXhOBhmRMGfFz_VA"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "44WD4VVAR6LR"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "5500931763"  # User id of your telegram account (Must be integer)
    
    ADMINS = "5500931763"
    
    CUSTOM_FILE_CAPTION = "hi helo"

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
