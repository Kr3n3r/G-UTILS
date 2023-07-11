from django.apps import AppConfig


class SvnMonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'svn_monitor'

    def ready(self):
        import svn_monitor.signals