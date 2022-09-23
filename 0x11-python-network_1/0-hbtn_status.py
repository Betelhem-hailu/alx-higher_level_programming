<<<<<<< HEAD
#!/usr/bin/python3
""" Fetching URLs with urllib """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
              .format(type(html), html, html.decode('utf-8')))
=======
#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
use the package urllib
 body of the response must be displayed in tabulation before -
"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()

print('Body response:\n\t- type: {}'.format(type(html)))
print('\t- content: {}'.format(html))
print('\t- utf8 content: {}'.format(html.decode('utf-8')))
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
