from celery import shared_task
from articles.scraper import scrape_all_articles

@shared_task
def scrape_articles_task():
    scrape_all_articles()
    pass
