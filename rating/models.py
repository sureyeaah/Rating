from django.db import models
import json
import requests


class User(models.Model):
    username = models.CharField(max_length=200)
    codeforces = models.CharField(max_length=200, blank=True, null=True)
    topcoder = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username


class Site(models.Model):
    handle = models.CharField(max_length=200)
    max_rating = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        abstract = True


class Codeforces(Site):
    def update(self):

        url = "http://codeforces.com/api/user.info"
        req = requests.get(url=url, params=dict(handles=self.handle))
        data = json.loads(req.text)

        if data["status"] == "OK":
            data = data["result"][0]
            if "rating" in data:
                self.rating = data["rating"]
                self.max_rating = data["maxRating"]
                self.save()

    def __str__(self):
        return "%s (Codeforces)" % self.handle


class Topcoder(Site):
    def update(self):

        url = "http://api.topcoder.com/v2/users/{}".format(self.handle)
        req = requests.get(url=url)
        data = json.loads(req.text)

        if "ratingSummary" in data:
            for rating in data["ratingSummary"]:
                if rating["name"] == "Algorithm":
                    self.rating = rating["rating"]
                    self.save()

    def __str__(self):
        return "%s (Topcoder)" % self.handle
