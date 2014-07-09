from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cntrct.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^widget/campaigns/', 
        'campaigns.views.campaigns_widget'),
    url(r'^widget/add/',
        'campaigns.views.add_widget'),
    url(r'^widget/addfromurl/',
        'campaigns.views.add_from_url_widget'),
)

