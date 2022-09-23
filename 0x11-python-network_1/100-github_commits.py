<<<<<<< HEAD
#!/usr/bin/python3
'''
Script that list 10 commits from the most recent to oldest of the repository
rails by the user rails
'''

if __name__ == "__main__":
    from sys import argv
    from requests import get
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    req = get(url)

    for i in range(10):
        print("{sha}: {author[login]}".format(**req.json()[i]))
=======
#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the repository and user
sent in as arguments
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    commits = r.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
