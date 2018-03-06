from django.conf.urls import include, url
from django.contrib import admin
from mainsite.views import *
urlpatterns = [
    # Examples:
    url(r'^$', homepage),
    url(r'^tel$',Add),
    url(r'^luckydraw$',luckydraw),
    url(r'^luckynumber$',luckynumber),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
