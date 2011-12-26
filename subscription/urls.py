from django.conf.urls.defaults import *

urlpatterns = patterns('subscription.views',
    url(r'unsubscribe/(?P<content_type>\d+)/(?P<object_id>\d+)/', 
        'unsubscribe', {
        },
        'subscription_unsubscribe'),
    url(r'subscribe/(?P<content_type>\d+)/(?P<object_id>\d+)/', 
        'subscribe', {
        }, 'subscription_subscribe'),
    url(r'^dropdown/ajax/$', 'dropdown_ajax', {
        'dropdowns': ['other', 'friends', 'messages'],
        'states': ['undelivered', 'unacknowledged', 'acknowledged'],
        'push_states': {
            'undelivered': 'unacknowledged',
        },
        'counter_state': 'unacknowledged',
    }, 'subscription_dropdown_ajax'),
    url(r'^dropdown/open/$', 'dropdown_open', {
        'push_states': {
            'unacknowledged': 'acknowledged',
        },
    }, 'subscription_dropdown_open'),
    url(r'^dropdown/more/$', 'dropdown_more', {
        'push_states': {
            'undelivered': 'acknowledged',
            'unacknowledged': 'acknowledged',
        },
    }, 'subscription_dropdown_more'),
    url(r'^$', 'list', {
        'keys': ['dropdown=other', 'dropdown=friends', 'dropdown=messages'],
        'states': ['undelivered', 'unacknowledged', 'acknowledged'],
        'push_states': {
            'undelivered': 'acknowledged',
            'unacknowledged': 'acknowledged',
        },
    }, 'subscription_list'),
)
