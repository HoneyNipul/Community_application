

from django.conf.urls import url



from rest_framework.authtoken import views as authviews

from mycommunity import search as cust_search

from mycommunity import views
from mycommunity import middleware

urlpatterns = [
    url(r'^add_address', views.add_address , name='add_address'),

    url(r'^add_member', views.add_member, name='add_member'),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    url(r'^searchRelation', cust_search.searchRelation, name='searchRelation'),
    url(r'^findRelatedPerson', cust_search.findRelatedPerson, name='findRelatedPerson'),
    url(r'^search',cust_search.searchMember, name='search'),
    url(r'^eventDetails/([0-9]+)/',views.get_eventDetail,name='eventDetails'),
    url(r'^member_detail/([0-9]+)/', views.get_detail, name='member_detail')
]
