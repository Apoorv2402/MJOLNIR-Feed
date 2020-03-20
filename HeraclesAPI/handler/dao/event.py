from config.dbconfig import fb_config
from firebase import Firebase
import os
CURRENT = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(CURRENT)
firebase = Firebase(fb_config)
rtdb = firebase.database()
storage = firebase.storage()


if __name__ == '__main__':
    print(rtdb.child("v1").child("profiles").get().val())
