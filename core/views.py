from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Movie, Show, Booking
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer, MovieSerializer, ShowSerializer, BookingSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    @action(detail=False, methods=["post"], permission_classes=[AllowAny])
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "User registered successfully."},
            status=status.HTTP_201_CREATED,
        )


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=["get"])
    def shows(self, request, pk=None):
        shows = Show.objects.filter(movie_id=pk)
        serializer = ShowSerializer(shows, many=True)
        return Response(serializer.data)


class ShowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def book(self, request, pk=None):
        show = get_object_or_404(Show, id=pk)
        seat_number = int(request.data.get("seat_number"))

        if seat_number < 1 or seat_number > show.total_seats:
            return Response({"error": "Invalid seat number"}, status=400)
        if Booking.objects.filter(show=show, seat_number=seat_number, status="booked").exists():
            return Response({"error": "Seat already booked"}, status=400)
        
        booking = Booking.objects.create(
            user=request.user,
            show=show,
            seat_number=seat_number,
        )
        return Response(BookingSerializer(booking).data, status=201)


class BookingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def my_bookings(self, request):
        bookings = Booking.objects.filter(user=request.user, status="booked")
        return Response(BookingSerializer(bookings, many=True).data)
    
    @action(detail=True, methods=["post"])
    def cancel(self, request, pk=None):
        booking = get_object_or_404(Booking, id=pk)
        if booking.user != request.user:
            return Response({"error": "Not allowed"}, status=403)

        booking.status = "cancelled"
        booking.save()
        return Response({"message": "Booking cancelled"}, status=200)
        
