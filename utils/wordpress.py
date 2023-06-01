import requests
import random

def get_random_wordpress_post(url):
    response = requests.get(url).json()
    total_posts = len(response)

    random_post_id = random.randint(1, total_posts)

    post_random = response[random_post_id]

    return post_random['post_title'], post_random['post_content'], post_random['guid']
