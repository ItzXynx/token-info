import sys
import base64

def decode(token):
    parts = token.split(".")
    uid = base64.b64decode(parts[0] + "==").decode()
    return uid

if __name__ == "__main__":
    token = sys.argv[1]
    try:
        uid = decode(token)
        print(f"user id: {uid}")
    except:
        print("couldnt decode token")
# updated
