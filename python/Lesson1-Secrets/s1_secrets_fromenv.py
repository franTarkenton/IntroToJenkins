import os
password = os.environ['BILLS_PASSWORD']
apiKey = os.environ['API_KEY']
print(f"Bill's password is {password}")
print(f"Bill's api key is {apiKey}")

print("... also don't do this ^^^")
