from .models import Site

def update_all():
    for site in Site.__subclasses__():
        for handle in site.objects.all():
            handle.update()
