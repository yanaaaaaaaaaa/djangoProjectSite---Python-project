from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('main', views.main, name='main'),
    path('demand', views.demand, name='demand'),
    path('geography', views.geography, name='geography'),
    path('skills', views.skills, name='skills'),
    path('last_vacancies', views.last_vacancies, name='last_vacancies'),
]
