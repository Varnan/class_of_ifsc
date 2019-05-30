from django.conf.urls import include, url

import indian_banks.views as views

urlpatterns = [

    # Server Landing Page
    url(r'^$', views.ServerLanding, name='landing'),

    # Server Health Check Page
    url(r'^health$', views.HealthChecking, name='health_check'),

    # Server Health Check Page
    url(r'^health/$', views.HealthChecking, name='health_check_url'),

    # API for List all branches
    url(r'^branches/$', views.ListAllBranches.as_view(), name='list_all_branches'),

    # API for get branch details from IFSC code
    url(r'^branches/(?P<ifsc>\w+)/$',views.BranchDetails.as_view(), name='branch_details'),


]




