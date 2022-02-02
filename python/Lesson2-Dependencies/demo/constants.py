import dotenv
import os
import sys

# Default Values
SOIL_URL='https://www.env.gov.bc.ca/esd/distdata/ecosystems/Soil_Data/Soil_Data_Pkgs/SOIL_Map_GDB_20160331.zip'
AG_DATA_URL='http://www.env.gov.bc.ca/esd/distdata/ecosystems/Soil_Data/AgricultureCapability/AgCap_Map_GDB_20150923.zip'

# pulling in secrets to env vars

envPath = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(envPath):
    print("loading dot env...")
    dotenv.load_dotenv()

# not used but demo of how to pull in a required value
MY_SECRET = os.environ['MY_SECRET']

# if values are populated in env file they take precidence
optionals = ['SOIL_URL', 'AG_DATA_URL', 'DATADIR', 'OUTPUT_GDB']
module = sys.modules[__name__]
for optional in optionals:
    if optional in os.environ:
        setattr(module, optional, os.environ[optional])
