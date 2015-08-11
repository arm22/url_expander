from django.db import models
from bs4 import BeautifulSoup
import requests

class Post(models.Model):
    org_url = models.URLField()
    fin_url = models.URLField(blank=True, null=True)
    resp_code = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)

    def publish(self):
        page = requests.get(self.org_url)
        soup = BeautifulSoup(page.text, "html.parser")
        self.fin_url = page.url
        self.resp_code = page.status_code
        self.title = soup.title.string
        self.save()

    def __str__(self):
        return self.title
