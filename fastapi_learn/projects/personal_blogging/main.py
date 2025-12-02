from fastapi import FastAPI

app = FastAPI()

'''
List of responsibilities
    Return a list of articles. You can add filters such as publishing date, or tags.

    Return a single article, specified by the ID of the article.

    Create a new article to be published.

    Delete a single article, specified by the ID.

    Update a single article, again, you’d specify the article using its ID.

'''

list_article_info_template = {
    id: None,
    "name":str,
    "article":str,
}


@app.get("/")
async def root():
    return {"message" : "Hello World!"}


@app.get("/list_articles")
async def list_all_articles():
    # for data in list_json:
        pass


