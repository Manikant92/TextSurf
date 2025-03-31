# TextSurf

<h3 align="center">Browse the web through text messages.</h3>


<p align="center">
  <a href="https://github.com/Manikant92/TextSurf"><img src="assets/logo.jpeg" width="25%"></a>
</p>


## Deploy locally 

### Local setup

After creating a conda/pyenv environment for the project perform the following actions

```
git clone https://github.com/Manikant92/TextSurf.git
cd TextSurf
pip install -r requirements.txt
python main.py
```

Open a seperate terminal window and run the following command

```
ngrok http 4545
```

Then copy the "Forwarding" https address and replace the ngrok_url variable in main.py with it


```python
ngrok_url = 'https://f84f-2405-201-c029-e142-cd42-24ea-2ad1-10ad.ngrok-free.app' # REPLACE THIS WITH YOUR FORWARDING URK
```

Restart the flask server by rerunning the main.py file

Send SMS messages on the following number
```
+18653916070
```

### Twilio setup

Head to Twilio console and select an actie number - click on it and under "Configure" scroll to the bottom. In "Messaging" replace the "A Message comes in" webhook with the same forwarding URL as your set ngrok_url BUT ALSO APPEND '/entry' to it. Click save and it should look like the image below

<img src="assets/twilio.png" width="50%">

### Test

Send a text to the activate number and the system should be up and running


## Commands

In the following table any text starting with '$' is a variable set by the user

| Command                       | Description                                                                                      |
|-------------------------------|--------------------------------------------------------------------------------------------------|
| instagram $USERNAME $PASSWORD | Will log in to instagram and return image of the feed                                            |
| google $SEARCHQUERY           | Will google search and return image                                                              |
| inspect $URL                  | Will load a webpage and return the endpoints webpage contacts during lifecycle                   |
| set $TAG $URL                 | Will save the url in to variable tag. Essentially turning $TAG in to a command that fetches $URL |
| $URL                          | Will return the webpage                                                                          |
| scroll                        | Will scroll down on last page loaded by user (Limited to 3 scrolls per page for demo)            |
