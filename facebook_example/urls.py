from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #(r'^accounts/', include('registration.backends.default.urls')),
    (r'^facebook/', include('django_facebook.urls')),
    
    #what to do with these?
    (r'', include('django_facebook.auth_urls')),
    (r'^accounts/', include('userena.urls')),
    # Example:
    # (r'^django_facebook_test/', include('django_facebook_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
