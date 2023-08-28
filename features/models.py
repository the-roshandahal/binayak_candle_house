from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import User

class CompanySetup(models.Model):
    data_set = models.CharField(max_length=200)
    company_logo = models.ImageField(upload_to="logos",verbose_name="Company Logo (163*36)")

    company_name = models.CharField(max_length=255)

    location = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
    facebook_url = models.URLField(null=True,blank=True)
    instagram_url = models.URLField(null=True,blank=True)
    linkedin_url = models.URLField(null=True,blank=True)
    youtube_url = models.URLField(null=True,blank=True)
    
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "01. Company Setup" 



class HomeContent(models.Model):
    data_set = models.CharField(max_length=200)

    header_heading = models.CharField(max_length=150)
    header_text = models.TextField()
    header_image = models.ImageField(upload_to="home_images/", verbose_name="Hero Section Image (1920*800)")
    header_button_text = models.CharField(max_length=100)
    header_button_url = models.URLField()

    about_title = models.CharField(max_length=255)
    about_text = models.TextField()
    about_image = models.ImageField(upload_to="home_images/", verbose_name="About Image (500*600)")

    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "02.Home Page Content" 

class Product(models.Model):
    featured_image = models.ImageField(upload_to="products_images/", verbose_name="Featured Image (200*200)")
    product_title = models.CharField(max_length=255)
    product_description = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_title
    class Meta:
        verbose_name_plural = "04. Products" 

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="gallery_images/", verbose_name="Gallery Image (860*860)")
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "05. Gallery" 


class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    contact = models.TextField()
    subject = models.TextField(null=True, blank=True)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "05. Contact"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    blog = models.TextField()
    image = models.ImageField(upload_to="blogs_images/",verbose_name="Blog Image (600*450)")
    slug = AutoSlugField(populate_from='title', unique=True)
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "06. Blogs" 

class AboutPageContent(models.Model):
    data_set = models.CharField(max_length=200)

    title = models.CharField(max_length=150)
    title_description = models.TextField()
    title_image = models.ImageField(upload_to="about_images/",verbose_name="Image (720*720)")
    fet_video = models.URLField(null=True,blank=True)

    sub_title = models.CharField(max_length=150)
    sub_image = models.ImageField(upload_to="about_images/",verbose_name="Image (500*600)")
    
    mission = models.TextField()
    vision = models.TextField()
    goal = models.TextField()

    out_story = models.TextField()

    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "03.About Page Content" 

class WeBelieveIn(models.Model):
    data_set = models.CharField(max_length=200)

    
    title_1 = models.CharField(max_length=150)
    text_1 = models.TextField()

    title_2 = models.CharField(max_length=150)
    text_2 = models.TextField()

    title_3 = models.CharField(max_length=150)
    text_3 = models.TextField()

    def __str__(self):
        return self.data_set
    class Meta:
        verbose_name_plural = "04.We Believe In" 
