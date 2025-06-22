from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer

# Room List View (GET Request) - Fetch all rooms or filter by location
def room_list(request):
    query = request.GET.get('location')
    if query:
        rooms = Room.objects.filter(location__icontains=query).values(
            'id', 'location', 'price', 'rating', 'image', 'available', 'landlord_name', 'landlord_phone'
        )
    else:
        rooms = Room.objects.all().values(
            'id', 'location', 'price', 'rating', 'image', 'available', 'landlord_name', 'landlord_phone'
        )
    return JsonResponse(list(rooms), safe=False)

# Room Detail View (GET Request) - Fetch a single room by ID
def room_detail(request, id):
    room = get_object_or_404(Room, id=id)
    return JsonResponse({
        'id': room.id,
        'location': room.location,
        'price': room.price,
        'rating': room.rating,
        'image': room.image.url if room.image else None,
        'available': room.available,
        'landlord_name': room.landlord_name,
        'landlord_phone': room.landlord_phone
    })

# Add Room View (POST Request) - For adding new rooms
@api_view(['POST'])
def add_room(request):
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the room data to the database
            return Response(serializer.data, status=201)  # Return created room data
        return Response(serializer.errors, status=400)  # Bad Request if errors
