from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register("users", views.UserViewSet, basename="users")
router.register("movies", views.MovieViewSet, basename="movies")
router.register("shows", views.ShowViewSet, basename="shows")
router.register("bookings", views.BookingViewSet, basename="bookings")
urlpatterns = [
    path('', include(router.urls)),
    path("signup/", views.UserViewSet.as_view({"post": "signup"}), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("my-bookings/", views.BookingViewSet.as_view({"get": "my_bookings"}), name="my-bookings"),
    # path("movies/<int:pk>/shows/", views.MovieViewSet.as_view({"get": "shows"}), name="movie-shows"),
]
