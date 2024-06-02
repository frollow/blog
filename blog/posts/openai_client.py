import logging
import requests
import time
from openai import OpenAI
from django.conf import settings

logger = logging.getLogger('posts')

OPENAI_API_KEY = settings.OPENAI_API_KEY
client = OpenAI(api_key=OPENAI_API_KEY)
HEADERS = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json",
}


def request_to_openai(prompt, model, max_retries=5):
    retry_count = 0
    while retry_count < max_retries:
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content
        except Exception as e:
            if "429 Too Many Requests" in str(e):
                retry_count += 1
                wait_time = 20 * retry_count
                logger.warning(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                logger.error(f"Failed to generate response from OpenAI: {e}")
                return None
    return None


def generate_image_from_openai(text, max_retries=5):
    retry_count = 0
    prompt = (
        f"Create a masthead image for a news article titled '{text}'. "
        f"The image should be visually appealing and relevant to the article's title. "
        f"If any text appears in the image, ensure it is in English and grammatically correct."
    )
    while retry_count < max_retries:
        try:
            response = requests.post(
                "https://api.openai.com/v1/images/generations",
                headers=HEADERS,
                json={
                    "model": "dall-e-3",
                    "prompt": prompt,
                    "n": 1,
                    "size": "1024x1024",
                    "quality": "standard",
                },
            )
            response.raise_for_status()
            image_url = response.json()["data"][0]["url"]
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                return image_response.content
            else:
                logger.error(f"Failed to retrieve image from URL: {image_url}")
                return None
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                retry_count += 1
                wait_time = 20 * retry_count
                logger.warning(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                logger.error(f"Failed to generate image from OpenAI: {e}")
                return None
    return None
