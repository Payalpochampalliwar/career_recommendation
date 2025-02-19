from django.db import models

# Create your models here.
class CareerCategory(models.Model):
    CATEGORY_CHOICES = [
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
        ('Arts', 'Arts'),
        ('Vocational', 'Vocational'),
        ('Other', 'Other'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name} ({self.category})"

class CareerPath(models.Model):
    CATEGORY_CHOICES = [
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
        ('Arts', 'Arts'),
        ('Vocational', 'Vocational'),
        ('Other', 'Other'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='career_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.category})"

class CareerDetail(models.Model):
    CATEGORY_CHOICES = [
        ('Science', 'Science'),
        ('Commerce', 'Commerce'),
        ('Arts', 'Arts'),
        ('Vocational', 'Vocational'),
        ('Other', 'Other'),
    ]
    career = models.OneToOneField(CareerPath, on_delete=models.CASCADE, related_name="details")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Other')
    description = models.TextField()
    required_courses = models.TextField(help_text="List of Required Courses")
    salary_range = models.CharField(max_length=100)
    top_colleges = models.JSONField(default=list)
    
    def __str__(self):
        return self.career.name

class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    subject = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.country}"