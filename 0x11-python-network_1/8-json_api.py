<<<<<<< HEAD
#!/usr/bin/python3
"""
This Python script takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) != 1:
        q = sys.argv[1]
    else:
        q = ""
    try:
        req = requests.post(url, data={'q': q}).json()
        if len(req) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(req.get('id'), req.get('name')))
    except:
        print('Not a valid JSON')
=======
#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r_dict = r.json()
        id = r_dict.get('id')
        name = r_dict.get('name')
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except:
        print("Not a valid JSON")
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
