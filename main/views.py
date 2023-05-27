from django.shortcuts import render
from django.contrib import messages
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from . models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate,
)

from django.views import generic
from . forms import ContactForm


class IndexView(generic.TemplateView, HitCountMixin):
    """Định nghĩa template cho IndexView (Home Page) """
    template_name = "main/index.html"
    count_hit = True
    
    def get_context_data(self, **kwargs):
        """Truyền dữ liệu vào template"""
        context = super().get_context_data(**kwargs)
        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        user = UserProfile.objects.first()
        hit_count = HitCount.objects.get_for_object(user)
        hit_count_response = HitCountMixin.hit_count(self.request, hit_count)
        
        # hits = hit_count.hits
        # hitcontext = context['hitcount'] = {'pk': hit_count.pk}
        
        # if hit_count_response.hit_counted:
        #     hits = hits + 1
        #     hitcontext['hit_counted'] = hit_count_response.hit_counted
        #     hitcontext['hit_message'] = hit_count_response.hit_message
        #     hitcontext['total_hits'] = hits

        print(hit_count_response)
        
        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        return context


class ContactView(generic.FormView):
    """Định nghĩa template cho ContactView (Contact Page) """
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        """Lưu contact form vào trong database và gửi message cho người truy cập"""
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    """Định nghĩa template cho PortfolioView (Portfolio Page) """
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset()


class PortfolioDetailView(generic.DetailView):
    """Định nghĩa template cho PortfolioDetailView (Portfolio Details Page)"""
    model = Portfolio
    template_name = "main/portfolio-detail.html"


class BlogView(generic.ListView):
    """Định nghĩa template cho BlogView (Blog Page) """
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
    """Định nghĩa template cho BlogDetailView (Blog Details Page) """
    model = Blog
    template_name = "main/blog-detail.html"
