<<<<<<< HEAD
#!/usr/bin/python3
""" Fetching URLs with Requests library """
import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    t = r.text
    print("Body response:")
    print("\t- type: {}\n\t- content: {}"
          .format(type(t), t))
=======
#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests
    req = requests.get('https://alx-intranet.hbtn.io/status')
    response = req.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
