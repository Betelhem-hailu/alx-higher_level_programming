<<<<<<< HEAD
#!/bin/bash
# bash script that takes a URL & sends a POST request to the URL
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
=======
#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, and displays the body of the response. A variable email must be sent with the value test@gmail.com. A variable subject must be sent with the value I will always be here for PLD
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
>>>>>>> 5ebb21c2aa1f7cc42f43f117b30146995d9f9405
