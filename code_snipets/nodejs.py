import uuid

def generateUUID():
    return str(uuid.uuid4())

print(generateUUID())