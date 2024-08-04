from django.db import models

class Student(models.Model):
    uid = models.IntegerField(unique=True, primary_key=True, editable=False, default=10)
    mail = models.CharField(max_length=40, unique=True, default='student@example.com')
    password = models.CharField(max_length=50, default='temporary_password')
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    registration_number = models.CharField(max_length=50, null=True, blank=True)
    parent = models.ForeignKey('Parent', on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.uid:
            last_student = Student.objects.all().order_by('uid').last()
            self.uid = (last_student.uid + 1) if last_student else 11
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.name if self.name else self.mail


class Parent(models.Model):
    uid = models.AutoField(primary_key=True)
    mail = models.CharField(max_length=40, unique=True, default='parent@example.com')
    password = models.CharField(max_length=50, default='temporary_password')
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else self.mail


class Faculty(models.Model):
    uid = models.IntegerField(unique=True, primary_key=True, editable=False, default=1001)
    mail = models.CharField(max_length=40, unique=True, default='faculty@example.com')
    password = models.CharField(max_length=50, default='temporary_password')
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.uid:
            last_faculty = Faculty.objects.all().order_by('uid').last()
            self.uid = (last_faculty.uid + 1) if last_faculty else 1001
        super(Faculty, self).save(*args, **kwargs)

    def __str__(self):
        return self.name if self.name else self.mail



class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    sender_uid = models.IntegerField(default=0)  # Example default value
    receiver_uid = models.IntegerField(default=0)  # Example default value
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Transaction #{self.transaction_id}"