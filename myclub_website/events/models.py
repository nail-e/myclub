from django.db import models

class Venue(models.Model):
    first_name = models.CharField("First Name", max_length=30)
    address = models.CharField(max_length=300)
    zip_code = models.CharField("Zip Code", max_length=10)
    phone = models.CharField("Contact Number", max_length=25)
    web = models.URLField("Website Address")
    email_address = models.EmailField("Email Address")

    def __str__(self):
        return self.name

class MyClubUsers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField("User Email", max_length=30)

    def __str__(self):
        return self.first_name +" "+ self.last_name

class Event(models.Model):
    name = models.CharField("Event Name", max_length=30)
    event_date = models.DateTimeField("Event Date")
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField("Event Name", max_length=60)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUsers, blank=True)

    def __str__(self):
        return self.name
