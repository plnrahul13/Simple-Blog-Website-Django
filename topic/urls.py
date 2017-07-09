from django.conf.urls import url
from . import views

urlpatterns = [
	# /topic/	
	url(r'^$',views.index,name='index'),

	# /topic/<user_id>/
	url(r'^(?P<user_id>[0-9]+)/$',views.detail,name='detail'),

	# /topic/<user_id>/<blog_id>
	url(r'^(?P<user_id>[0-9]+)/(?P<blog_id>[0-9]+)/$',views.content,name='content'),

	# /topic/allblogs
	url(r'^allbloggers/$',views.allbloggers,name='bloggers'),

	# /topic/addblogs
	url(r'^addblogs/$',views.addblogs,name='addblogs'),

	# /topic/addblog
	url(r'^addblog/$',views.addblog,name='addblog'),
]