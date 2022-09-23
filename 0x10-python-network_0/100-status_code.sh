<<<<<<< HEAD
#!/bin/bash
# Takes a URL and sends a request to it and displays the status code of the response
curl -s -w "%{http_code}" "$1" -o /dev/null
=======
#!/bin/bash
# sends a request to a URL passed as an argument, and displays only the status code of the response
curl -so /dev/null --write-out "%{http_code}" "$1"
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
