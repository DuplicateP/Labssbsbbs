import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("26792945"))
    API_HASH = os.environ.get("6be4bc36c6a70c269f80a7388e59e150")
    VIP_USER = os.environ.get('VIP_USERS', '').split(',')
    VIP_USERS = [int(7357284659) for user_id in VIP_USER]
