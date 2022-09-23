<<<<<<< HEAD
#!/usr/bin/python3
"""Get id
"""

if __name__ == "__main__":
    import requests
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    req = requests.get('https://api.github.com/user', auth=(user, passwd))
    print(req.json().get('id'))
=======
#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
