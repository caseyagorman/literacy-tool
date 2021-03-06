from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "students"



urlpatterns = [
url(r'^$', views.IndexView.as_view(), name= "index"),

url(r'student/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='student_detail'),

url(r'student/add/$', views.StudentCreate.as_view(), name='student-add'),

# url(r'student/(?P<pk>[0-9]+)/$', views.StudentUpdate.as_view(), name='student-update'),

url(r'student/delete/(?P<pk>[0-9]+)/$', views.StudentDelete.as_view(), name='student-delete'),

url(r'word/$', views.WordListView.as_view(), name='word_index'),

url(r'word/(?P<pk>[0-9]+)/$', views.WordDetailView.as_view(), name='word_detail'),

url(r'word/add/$', views.WordCreate.as_view(), name='word-add'),

url(r'student/student_edit/(?P<pk>[0-9]+)/$', views.student_edit, name='form'),

url(r'word/delete/(?P<pk>[0-9]+)/$', views.WordDelete.as_view(), name='word-delete'),] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
