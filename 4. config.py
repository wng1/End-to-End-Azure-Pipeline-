# Fetch secrets
TRANSLATOR_ENDPOINT = os.getenv("TRANSLATOR_ENDPOINT")
TRANSLATOR_KEY = client.get_secret("TranslatorKey").value
TEXT_ANALYTICS_ENDPOINT = os.getenv("TEXT_ANALYTICS_ENDPOINT")
TEXT_ANALYTICS_KEY = client.get_secret("TextAnalyticsKey").value
ADX_CLUSTER = os.getenv("ADX_CLUSTER")
ADX_DATABASE = os.getenv("ADX_DATABASE")
ADX_TABLE = os.getenv("ADX_TABLE")
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))
