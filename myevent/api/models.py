from django.db import models
from django.contrib.auth.models import User

# class SiidaaUser(AbstractUser):
#     is_organizer = models.BooleanField(null=True, blank=True)
#     is_attendee = models.BooleanField(null=True, blank=True)
#     organizer_name = models.CharField( max_length=200,null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=50 , default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Country(models.Model):
    country = models.CharField( max_length=50, default=False)
    def __str__(self):
        return self.country
    
class City(models.Model):
    city = models.CharField( max_length=50, default=False)
    country  = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.city
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE,null=True, blank=True)
    country = models.ForeignKey(Country,  on_delete=models.CASCADE,null=True, blank=True)
    city = models.ForeignKey(City,  on_delete=models.CASCADE,null=True, blank=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    registration_required = models.BooleanField(default=False)
    registration_limit = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    

class Ticket(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    total_slot = models.PositiveIntegerField(null=True,blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class Registration(models.Model):
    attendee = models.ForeignKey(User, on_delete=models.CASCADE,related_name='attending_events')
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    attendance_collected_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_attended = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    

class Payment(models.Model):
    registration = models.OneToOneField(Registration, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.registration
    


