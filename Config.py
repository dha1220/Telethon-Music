import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 5767182316)
    STRING_SESSION = os.environ.get("STRING_SESSION",1BVtsOLQBu5bRNLne-27dnBwJknnpDIVBVKwxUI3J8-B3XrXx0whVXHXYG-hl4BlXztxI-ooGPUWSdnCyA6Vw64GVbZLvHXwKV34dMZfOfug6G_kwABDBr-lCapOVJp8BvdIRY0J1dY7EuLIw5Xv5TzCQlG8EJGJwpI2TKLOjmJUS6Fz8sVabHeinay3KTYhOMbluntWmb5I7EiYr2wOQrq6DA_akVdz71XUxyRhLehQnrWrEBNWekAdj_mRHhMEjKoxif7X2GjeyElqiCADE6lEFaVqKFiyt0b8iAMwT_EShYItrE5JdeUevb9Y5JWHUNX26MLTxVliAMjAsXxMncy_vQXseLYY= )
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
