from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

# Create your models here.


class Skill(models.Model):
    """Skill model"""
    class Meta:
        """Tên số nhiều và số ít của Skill model"""
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        """Lấy tên của Skill"""
        return self.name


class UserProfile(models.Model):
    """UserProfile model"""
    class Meta:
        """Tên số nhiều và số ít của UserProfile model"""
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        """Lấy họ và tên của User"""
        return f'{self.user.first_name} {self.user.last_name}'


class ContactProfile(models.Model):
    """Contact model"""
    class Meta:
        """Tên số nhiều và số ít, sắp xếp theo mốc thời gian của Contact model"""
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]
        
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        """Lấy tên của người gửi form"""
        return f'{self.name}'


class Testimonial(models.Model):
    """Testimonial model"""
    class Meta:
        """Tên số nhiều và số ít, sắp xếp theo tên của Testimonial model"""
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ["name"]
    thumbnail = models.ImageField(
        blank=True, null=True, upload_to="testimonial")
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """Lấy tên của người lấy lời chứng thực"""
        return self.name


class Media(models.Model):
    """Media model"""
    class Meta:
        """Tên số nhiều và số ít, sắp xếp theo tên của Media model"""
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ["name"]

    image = models.ImageField(blank=True, null=True, upload_to="media")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """Lưu thông tin tệp vào database"""
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        """Lấy tên của tệp đa phương tiện"""
        return self.name


class Portfolio(models.Model):
    """Portfolio model"""
    class Meta:
        """Tên số nhiều và số ít, sắp xếp theo tên của Portfolio model"""
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]
        
    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """Lưu thông tin dự án vào database và slugify tên dự án"""
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        """Lấy tên của dự án"""
        return self.name

    def get_absolute_url(self):
        """Lấy đường dẫn tuyệt đối của dự án"""
        return f"/portfolio/{self.slug}"


class Blog(models.Model):
    """Blog model"""
    class Meta:
        """Tên số nhiều và số ít, sắp xếp theo mốc thời gian của Blog model"""
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """Lưu thông tin blog vào database và slugify tên blog"""
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        """Lấy tên của bài blog"""
        return self.name

    def get_absolute_url(self):
        """Lấy đường dẫn tuyệt đối của blog"""
        return f"/blog/{self.slug}"


class Certificate(models.Model):
    """Certificate model"""
    class Meta:
        """Tên số nhiều và số ít của Certificate model"""
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """Lấy tên của chứng chỉ"""
        return self.name
