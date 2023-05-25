from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        """Override hàm ready của class MainConfig và gọi đến file signals.py
            khi ứng dụng sẵn sàng"""
        import main.signals