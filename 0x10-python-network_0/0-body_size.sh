<<<<<<< HEAD
#!/bin/bash
# Display the size of the body of a request
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
=======
#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
