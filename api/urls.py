from django.urls import path, include
from api.models import CourseResourse, CategoryResource
from tastypie.api import Api


api = Api(api_name='v1')
api.register(CourseResourse())
api.register(CategoryResource())

# api/v1/courses/        GET, POST
# api/v1/courses/1/      GET, DELETE
# api/v1/categories/     GET
# api/v1/categories/1/   GET

# For POST, DELETE add header
# Key: Authorization
# Values: ApiKey dany:qwerty12345

urlpatterns = [
    path('', include(api.urls), name='index')
]
