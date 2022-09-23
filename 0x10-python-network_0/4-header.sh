<<<<<<< HEAD
#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
curl -sH "X-HolbertonSchool-User-Id: 98" -X GET "$1"
=======
#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable X-School-User-Id must be sent with the value 98
curl -sX GET -H "X-School-User-Id: 98" "$1"
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
