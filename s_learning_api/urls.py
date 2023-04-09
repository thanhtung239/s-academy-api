"""s_learning_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from django.conf import settings

from .models.User import User
from .models.Course import Course
from .models.Lesson import Lesson
from .models.Document import Document

from .views.Courses import CourseAPIView, GetDetailCourse, AddUserToCourse
from .views.User import UserViewSet
from .views.Lesson import LessonViewSet
from .views.Registration import RegisterView
from .views.Common import LogoutView

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Document)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('lessons', LessonViewSet, basename='lesson')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view()),
    path('api/logout/', LogoutView.as_view()),
    path('api/courses/', CourseAPIView.as_view()),
    path('api/courses/detail/', GetDetailCourse.as_view()),
    path('api/courses/users/', AddUserToCourse.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh')
]

# config URL image
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
