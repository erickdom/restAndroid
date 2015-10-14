from django.conf.urls import patterns, url
from restAndroid import settings
from transactions.views import TransactionREST, TransactionDetailREST

urlpatterns = patterns(
    '',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    url(r'^transactions/$', TransactionREST.as_view()),
    url(r'^transactions/(?P<folio_android>.*)/$', TransactionDetailREST.as_view()),
)