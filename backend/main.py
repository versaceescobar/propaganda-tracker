from fastapi import FastAPI
from scraper import scrape_page

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Propaganda Tracker API is running."}

@app.get("/scrape")
def run_scraper(page_url: str):
    result = scrape_page(page_url)
    return {"status": "completed", "posts": result}
