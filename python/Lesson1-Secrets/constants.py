import os
import dotenv
import sys

# looking for a .env file in the directory that this module is located
envFileName = '.env-tj'
secretsDir = r'/mnt/c/junk/secrets'
currentDirectory = os.path.dirname(__file__)
envPath = os.path.join(secretsDir, envFileName)
print(envPath)

# if the .env file is found then load it
if os.path.exists(envPath):
    print('loading env vars')
    dotenv.load_dotenv(envPath)

BILLS_PASSWORD = os.environ['BILLS_PASSWORD']
API_KEY = os.environ['API_KEY']



# optional params: if they are defined in env vars, the are populated into
# variables for this module.
optionals = ['TEST_OBJ_NAME', "SUPERSECRET", 'CRAZYENV', 'ETC', 'DEMO']
module = sys.modules[__name__]
for optional in optionals:
    if optional in os.environ:
        setattr(module, optional, os.environ[optional])


if __name__ == '__main__':
    print(f"the demo var is {os.environ['DEMO']}")

