<<<<<<< HEAD
#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response with Requests library
"""
import requests
import sys

if __name__ == "__main__":

    email = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], email)
    print(r.text)
=======
#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    payload = {'email': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
