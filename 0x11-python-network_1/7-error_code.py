<<<<<<< HEAD
#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the body of the response with Requests library.
"""
import requests
import sys

if __name__ == "__main__":

    error = requests.get(sys.argv[1])
    if error.status_code >= 400:
        print('Error code: {}'.format(error.status_code))
    else:
        print(error.text)
=======
#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL & displays the body of the response
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
