from django.conf.urls import patterns, url
from transactions.views import TransactionREST, TransactionDetailREST

urlpatterns = patterns(
    '',
    url(r'^transactions/$', TransactionREST.as_view()),
    url(r'^transactions/(?P<folio_android>.*)/$', TransactionDetailREST.as_view()),
)