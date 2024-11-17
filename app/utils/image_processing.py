import requests
from PIL import Image
from io import BytesIO
import pytesseract

def download_image(url, save_path):
    """
    Downloads an image from a URL and saves it locally.
    
    :param url: str, the URL of the image
    :param save_path: str, the local path to save the image
    """
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded and saved to {save_path}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

def extract_text_from_image(image_path):
    """
    Extracts text from an image using pytesseract.
    
    :param image_path: str, the path to the image file
    :return: str, extracted text
    """
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

