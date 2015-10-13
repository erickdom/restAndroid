from django.conf.urls import patterns, url
from log_errors.views import Log_ErrosREST

urlpatterns = patterns(
    '',
    url(r'^log_errors/$', Log_ErrosREST.as_view()),
)