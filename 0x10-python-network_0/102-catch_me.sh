<<<<<<< HEAD
#!/bin/bash
# Takes in a URL and sends a request to it and displays the response message You got me!
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin: HolbertonSchool" -d "user_id=98"
=======
#!/bin/bash
# script that was a fun effort in breaking to http protocols on holberton servers
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
