from django.contrib.auth.models import User

def project_context(request):
    """Thêm context dictionary lấy dữ liệu là user đầu tiên trong User model
        , sau đó có thể truy cập context này từ view hoặc template"""
    context = {
        'me': User.objects.first(),
    }
    
    return context