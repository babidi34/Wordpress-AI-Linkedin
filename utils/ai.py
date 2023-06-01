import openai

def generate_linkedin_post(title, content, lien_article,api_key_openai):
    openai.api_key = api_key_openai
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role":"user", "content":f"You’re a linkedin expert, write a linkedin post to talk about the article \"{title}\", the post must have a catchphrase, in french, must use a relaxed style, use tutoring, some emojis, line break between each sentence and have a little humourist side if possible. (does not place a variable the text will be posted as is on linkedin).insert the link of the article at the bottom of the post ({lien_article})"}
      ],
      temperature=0.5,
      max_tokens=200
    )

    return completion['choices'][0]['message']['content']