import os
class Config(object):
    API_ID = int(os.environ.get("APP_ID", 20481097))
    API_HASH = os.environ.get("API_HASH", "db922b7ec52d5cb27896514f471e5f6b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5837848320:AAE5RjwzcqskPoZ8GZ60flZ6AYnh_UNBHGE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOK8BuxyLFreQKdEY8JWbtb0uS9JVSwTXA91emlPTB-qMl8GWOTjhOn8QT2Yd6UsBIH-L4Pl08E-aoGDJo1WQGINpfF89h7iCVFK2sHul0xcKzGRmf9geJpW_K0Vyu6iy4P6EoTst91gpS785uqLvlJwIKt8xRKbZPOhjrixosWDDtDnkX1BT6uh_nZy_x8tXhJD56g4ye4tRZhquJqBJAdaaRRlwFEgWmU2C6BCKUhfPT5w4d-XtGTklqiB728BPtBIE1eMKmtwTNXoMxgFSwuonhvl5lxBpUj765Xy_l5u3uIX00gm8-iFWQsP6R3neV-0J-Hrep5HVob9N3BNBsIq0CuU=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", "ENABLE")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MUSICBOT_TOYBOT")
    SUPPORT = os.environ.get("SUPPORT", "supportchat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "ourchannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/57c08fd10ced5222e713d.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/dffbf35d137f696bf5219.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", 5837848320)) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
