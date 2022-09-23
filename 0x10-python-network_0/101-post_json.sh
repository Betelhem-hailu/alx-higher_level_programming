<<<<<<< HEAD
#!/bin/bash
# Takes a URL and a JSON filename, and sends a POST request to the URL
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
=======
#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
