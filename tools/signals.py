from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from authapp.models import CustomUser
from school.models import School
from students.models import Student
from django.contrib.auth.hashers import make_password

@receiver(pre_save, sender=CustomUser)
def set_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = instance.first_name


@receiver(post_save, sender=CustomUser)
def create_student_account(sender, instance, created, **kwargs):
    if created:
        if instance.user_group_id is not None:
            if instance.user_group_id == "Students":
                student_data = {}
                student_data["first_name"] = instance.first_name
                student_data["last_name"] = instance.last_name
                student_data["email"]=instance.email
                student_data["phone"] = instance.phone
                student_data["username"] = instance.username
                student_data["password"] = instance.password
                student_data["school"] = instance.school
                student_data["gender"] = instance.gender
                student_data["user_id"] = instance.id
                if instance.commune is not None:
                    student_data["commune"] = instance.commune
                if instance.date_of_birth is not None:
                    student_data["date_of_birth"] = instance.date_of_birth
                Student.objects.create(**student_data)

@receiver(post_save, sender=CustomUser)
def update_created_admin(sender, instance, created, **kwargs):
    if created:
        if instance.subdomain:
            school = School.objects.filter(subdomain=instance.subdomain).first()
            instance.school = school
            instance.save()


@receiver(post_save, sender=Student)
def update_student(sender, instance, created, **kwargs):
    if created == False:
        if instance.user:
            student_data = {}
            student_data["first_name"] = instance.first_name
            student_data["last_name"] = instance.last_name
            student_data["email"] = instance.email
            student_data["username"] = instance.username
            student_data["password"] = make_password(instance.password)
            student_data["is_active"] = instance.is_active
            student_data["phone"] = instance.phone
            if instance.commune is not None:
                student_data["commune"] = instance.commune
            if instance.date_of_birth is not None:
                student_data["date_of_birth"] = instance.date_of_birth
            CustomUser.objects.filter(pk=instance.user.id).update(**student_data)


# calculating the number of students in a subject and fill the field


def student_post_save(sender, instance, *args, **kwargs):
    subjects = instance.subjects.all()
    print("subjects are: ", subjects)
    for subject in subjects:
        subject.save()
post_save.connect(student_post_save, sender=Student)

# @receiver(post_save, sender=Student)
    