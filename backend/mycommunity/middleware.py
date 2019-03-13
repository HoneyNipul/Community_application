
#from django.conf import settings

# class LocaleMiddleware(object):
#
#     def process_request(self, request):
#
#         #username = request.Post.get("username")
#         #password = request.Post.get("password")
#         print "middleware"
#
#         if 'locale' in request.cookies:
#             request.locale = request.cookies.locale
#         else:
#             request.locale = None
#
#     def process_response(self, request, response):
#
#         if getattr(request, 'locale', False):
#             response.cookies['locale'] = request.locale