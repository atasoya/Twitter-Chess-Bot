import requests
from bs4 import BeautifulSoup
import base64

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
                image_path = "downloaded_image.png"  # Replace with your desired path and file name
                
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

downloadImage("r1b3kr/ppp1Bp1p/1b6/n2P4/2p3q1/2Q2N2/P4PPP/RN2R1K1 w - - 1 0")