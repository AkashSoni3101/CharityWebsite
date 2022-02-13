from operator import mod
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    EDUCATION = 'Education'
    FOOD = 'Food'
    LIVELIHOOD = 'Livelihood'
    DISABILITY = 'Disability'
    MEDICAL = 'Medical'

class Donations(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.EDUCATION)
    thumbnail = models.ImageField(upload_to='photos/%Y/%m/%d')
    excerpt = models.CharField(max_length=200)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    raised = models.CharField(max_length=10)
    goal = models.CharField(max_length=10)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    
    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = Donations.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Donations.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = Donations.objects.get(featured = True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except Donations.DoesNotExist:
                pass
 
        super(Donations, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Events(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to='events/%Y/%m/%d')
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    startTime = models.CharField(max_length=255)
    endTime = models.CharField(max_length=255)
    location = models.CharField(max_length=30)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = Events.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Events.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = Events.objects.get(featured = True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except Events.DoesNotExist:
                pass
 
        super(Events, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=20, default='Gallery')
    slug = models.SlugField()
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='gallery/%Y/%m/%d')
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = Gallery.objects.all().filter(slug__iexact=original_slug).count()

        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Gallery.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug

        if self.featured:
            try:
                temp = Gallery.objects.get(featured = True)
                if self != temp:
                    temp.featured = False
                    temp.save()
            except Events.DoesNotExist:
                pass
 
        super(Gallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.email 

class BecomeVolunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    DOB = models.CharField(max_length=500)
    occupation = models.CharField(max_length=300)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

class Designation(models.TextChoices):
    HEAD = 'Head',
    VOLUNTEEER = 'Volunteer',
    PUBLIC = 'Public',

class OurTeam(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=Designation.choices, default=Designation.HEAD)
    thumbnail = models.ImageField(upload_to='team/%Y/%m/%d')
    message = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

class TestimonialDesignation(models.TextChoices):
    HEAD = 'Head',
    VOLUNTEEER = 'Volunteer',
    PUBLIC = 'Public',
    
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=TestimonialDesignation.choices, default=TestimonialDesignation.HEAD)
    message = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

# class HomeBanner(models.Model):
#     name = models.CharField(max_length=200, default='Home Banner')
#     thumbnail = models.ImageField(upload_to='homeBanner/%Y/%m/%d')


class Order(models.Model):
    order_product = models.CharField(max_length=100)
    order_amount = models.CharField(max_length=25)
    order_payment_id = models.CharField(max_length=100)
    isPaid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_product