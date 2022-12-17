import os

from dotenv import load_dotenv

 

load_dotenv() # take environment variables from .env.

 

print('User: ', os.getenv('PORT_MQTT')) # Return your system USERNAME configuration.

