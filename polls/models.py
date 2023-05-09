from django.db import models


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Question(models.Model):
    question_text = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField('date published', auto_now_add=True, null=True)

    def __str__(self):
        return self.question_text



class Choice(models.Model):
    choice_text = models.CharField(max_length=200, null=True)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text    
    



class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None, mobile_number=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            mobile_number=mobile_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, mobile_number=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            mobile_number=mobile_number,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_add=True
    )
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
