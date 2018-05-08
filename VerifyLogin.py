import requests
import sys

if __name__ == '__main__':
    USER = sys.argv[1]
    USER_PASSWD = sys.argv[2]

    if '@' in USER:
        USER = USER.split('@')[0]
    res = requests.get("http://review.source.spreadtrum.com/gerrit/login/", auth=(USER, USER_PASSWD))
    print res.status_code