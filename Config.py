import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6271908221:AAHpYEiGkHczNDtpGz41LfOHBFHR5YuO020"")
    STRING_SESSION = os.environ.get("STRING_SESSION",1BVtsOLQBu5bRNLne-27dnBwJknnpDIVBVKwxUI3J8-B3XrXx0whVXHXYG-hl4BlXztxI-ooGPUWSdnCyA6Vw64GVbZLvHXwKV34dMZfOfug6G_kwABDBr-lCapOVJp8BvdIRY0J1dY7EuLIw5Xv5TzCQlG8EJGJwpI2TKLOjmJUS6Fz8sVabHeinay3KTYhOMbluntWmb5I7EiYr2wOQrq6DA_akVdz71XUxyRhLehQnrWrEBNWekAdj_mRHhMEjKoxif7X2GjeyElqiCADE6lEFaVqKFiyt0b8iAMwT_EShYItrE5JdeUevb9Y5JWHUNX26MLTxVliAMjAsXxMncy_vQXseLYY= "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
