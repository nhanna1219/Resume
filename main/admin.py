import json
from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from . models import (
    UserProfile,
    ContactProfile,
    Testimonial,
    Media,
    Portfolio,
    Blog,
    Certificate,
    Skill
)

# Đăng ký các model ở Admin site

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Đăng ký UserProfile model"""
    list_display = ('id', 'user')


@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
    """Đăng ký Contact model"""
    list_display = ('id', 'timestamp', 'name')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """Đăng ký Testimonial model"""
    list_display = ('id', 'name', 'is_active')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    """Đăng ký Media model"""
    list_display = ('id', 'name')


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    """Đăng ký Portfolio model"""
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """Đăng ký Blog model"""
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    """Đăng ký Certificate model"""
    list_display = ('id', 'name')


@admin.register(Skill)
class Admin(admin.ModelAdmin):
    """Đăng ký Skill model"""
    list_display = ('id', 'name', 'score')
