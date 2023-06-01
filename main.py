from utils import wordpress
from utils import ai
from dotenv import load_dotenv
import os

load_dotenv()

url_api_wordpress_posts = os.getenv('url_api_wordpress_posts')
api_key_openai          = os.getenv('api_key_openai')

titre_article   = wordpress.get_random_wordpress_post(url_api_wordpress_posts)[0]
contenu_article = wordpress.get_random_wordpress_post(url_api_wordpress_posts)[1]
first_word_titre = titre_article.split()[0]
lien_article    = f"https://linux-man.fr/index.php/{first_word_titre}"

response_openai = ai.generate_linkedin_post(titre_article,contenu_article,lien_article,api_key_openai)

print(response_openai)
