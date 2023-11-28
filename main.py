import tweepy
import requests
from bs4 import BeautifulSoup
import base64
import questions
import time

def downloadImage(fen):

# URL of the website with the data URL
    url = "https://fen2png.com/api/?fen="+fen  # Replace with the actual URL of the website

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the image element (usually an <img> tag)
        img_element = soup.find('img')
        
        # Get the source URL of the image
        if img_element:
            img_src = img_element.get('src')
            
            # Check if the image source is a data URL
            if img_src.startswith("data:image"):
                # Extract the base64-encoded image data
                image_data = img_src.split(",")[1]
                
                # Decode the base64 data
                decoded_image_data = base64.b64decode(image_data)
                
                # Specify the path where you want to save the image
                image_path = "download.png"  # Replace with your desired path and file name
                
                # Save the image to the specified path
                with open(image_path, "wb") as img_file:
                    img_file.write(decoded_image_data)
                    
                print(f"Image downloaded and saved as {image_path}")
            else:
                print("Image source is not a data URL.")
        else:
            print("Image not found on the page.")
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)
def makePost(text):


    media_id = api.media_upload(filename="download.png").media_id_string
    print(media_id)


    # Send Tweet with Text and media ID
    client.create_tweet(text=text, media_ids=[media_id])
    print("Tweeted!")
def getFen(counter):
    return questions.questions[counter]


api_key = "-"
api_secret = "-"
access_token = "-"
access_token_secret = "-"
bearer_token = "-"

# Authenticate using OAuth1UserHandler
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# V2 Twitter API Authentication
client = tweepy.Client(
    bearer_token,
    api_key,
    api_secret,

    access_token,
    access_token_secret,
    wait_on_rate_limit=True,
)

def hourlyFunction():
    global counter
    counter += 1
    question = getFen(counter)
    downloadImage(question[2])
    makePost(f"{question[1]}\nMate in {question[0]}")

counter = -1

while True:
    hourlyFunction()
    time.sleep(60*60)