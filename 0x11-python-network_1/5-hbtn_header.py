<<<<<<< HEAD
#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response with Requests library
"""
import requests
import sys

if __name__ == "__main__":
    argument = sys.argv[1]
    r = requests.get(argument)
    print(r.headers.get('X-Request-Id'))
=======
#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
