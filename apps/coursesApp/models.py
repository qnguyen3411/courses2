from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def length_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Course name must be more than 5 characters"
        if len(postData['description']) < 15:
            errors['description'] = "Description must be more than 15 characters"
        return errors

class CommentManager(models.Manager):
    def length_validator(self, postData):
        errors = {}
        if len(postData['comment']) < 1:
            errors['comment'] = "Comment must not be empty"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()

class Description(models.Model):
    content = models.TextField()
    course = models.OneToOneField(Course, related_name="description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.TextField()
    course = models.ForeignKey(Course, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CommentManager()
    