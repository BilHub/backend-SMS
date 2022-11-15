from django.db import models

from school.models import School


class Cycle(models.Model):
    name = models.CharField(default="", max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(default="", max_length=255, null=True, blank=True)
    cycle = models.ForeignKey(Cycle,null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.name

class Subject(models.Model):
    subject_name = models.CharField(default="",  max_length=255, null=True, blank=True)
    level = models.ForeignKey(Level,blank=True, null=True, on_delete=models.SET_NULL)
    cycle = models.ForeignKey(Cycle,null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # teacher = models.ForeignKey(Teacher, blank=True, null=True, on_delete=models.SET_NULL, related_name="subjects")

    class Meta:
        ordering = ['cycle', 'level']

    def __str__(self):
        return self.subject_name

    @property
    def teachers_list(self):
        teachers_list=[]
        print("getting teachers")
        teachers_objs = self.teachers.all()
        if teachers_objs:
            for obj in teachers_objs:
                teachers_list.append(obj.first_name)
        return teachers_list

    @property
    def students_number(self):
        print("getting students number")
        return self.students.count()

    
    
    # def save(self, *args, **kwargs):
    #     if self.id:
    #         self.number_of_students = self.students_number()
    #         super(Subject, self).save(*args,**kwargs)
    #     super(Subject, self).save(*args,**kwargs)
        

class Classroom(models.Model):
    name = models.CharField(default="",  max_length=255, null=True, blank=True)
    capacity = models.IntegerField(default=1)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name





