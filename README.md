# Automatisation des publications LinkedIn avec OpenAI GPT-4 et l'API WordPress

Ce projet est un script Python qui utilise l'API GPT-4 d'OpenAI et l'API WordPress pour générer et publier des posts LinkedIn basés sur des articles de blog.

## Fonctionnalités

- Récupère un article aléatoire à partir d'un site WordPress
- Utilise l'API GPT-4 d'OpenAI pour générer un texte de post LinkedIn à partir de l'article
- Publie le post sur LinkedIn

## Installation

1. Clonez ce dépôt :
    ```bash
    git clone https://github.com/votre_nom_utilisateur/votre_projet.git
    ```
2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```
3. Configurez vos variables d'environnement dans un fichier `.env` :
    ```bash
    api_key_openai=your_api_key
    url_api_wordpress_posts=url_api_wordpress
    # Ajoutez toutes les autres variables d'environnement nécessaires ici
    ```

## Utilisation

Pour exécuter le script, utilisez la commande suivante :
```bash
python main.py
