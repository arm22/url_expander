from django.db import models
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import os
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from shortner import settings

class Post(models.Model):
    org_url = models.URLField()
    fin_url = models.URLField(blank=True, null=True)
    resp_code = models.IntegerField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    pic = models.URLField(blank=True, null=True)

    def publish(self):
        page = requests.get(self.org_url)
        soup = BeautifulSoup(page.text, "html.parser")
        driver = webdriver.PhantomJS(service_log_path=os.path.devnull)
        driver.get(page.url)
        temp = soup.title.string
        name = temp.lower()
        name = name.replace(" ", "")
        driver.save_screenshot('/tmp/' + name + '.png')
        driver.close()

        conn = S3Connection(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY )
        b = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
        k = Key(b)
        k.key = '/img/' + name + '.png'
        k.set_contents_from_filename('/tmp/' + name + '.png')
        b.set_acl('public-read', '/img/' + name + '.png')
        os.remove('/tmp/' + name + '.png')

        self.fin_url = page.url
        self.resp_code = page.status_code
        self.title = soup.title.string
        self.pic = 'https://s3.amazonaws.com/auzbucket-ml11/img/' + name + '.png'
        self.save()

    def __str__(self):
        return self.title