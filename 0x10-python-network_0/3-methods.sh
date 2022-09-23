<<<<<<< HEAD
#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -sI "$1" | grep "Allow:" | cut -d " " -f2-
=======
#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
