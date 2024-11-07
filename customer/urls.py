# core/urls.py
from django.urls import path
from core.views import test_view
from customer.views import get_my_profile, create_profile

urlpatterns = [
    path('profile', get_my_profile, name='Get my profile'),
    path('signup', create_profile, name='Sign Up Profile'),
    path('update_profile', test_view, name='Sign Up Profile'),
    path('give_permission', test_view, name='Give Permission to a new/old user'),
    path('generate_qr_code', test_view, name='Generate QR Code'),
    path('revoke_permission', test_view, name='Remove trip permission'),
    path('trips/in_progress/vehicles', test_view, name='Get All Vehicles for my Trip'),
    path('trips/in_progress/vehicles', test_view, name='Get All Vehicles for my Trip'),
    path('customer/complaints/<int:vehicle_id>/', test_view, name='view_complaints_by_vehicle'),

    # View all complaints
    path('customer/complaints/', test_view, name='view_all_complaints'),

    # Register a new complaint
    path('customer/complaints/post/', test_view, name='register_complaint'),

    # Perform actions (close, escalate, feedback) on a specific complaint
    path('customer/complaints/<int:id>/<str:action>/', test_view, name='complaint_action'),

]



# /customer/ get -> my_profile
# /customer/ post -> register self
# / customer/ patch -> update profile
# /customer/give_permission post -> give permission to another mobile number to share QR
# /customer/generate QR post -> Generate QR code for driver scan or onboard for owner
# /customer/generate OTP post for driver and Owner
# /customer/revoke_permission post -> revoke QR permission
# /customer/trips/in_progress -> all vehicle for my work will list
# /customer/trip/in_progress/{vehicle_id}/{track or details or pass}
# / customer/complaints/{vehicle_id}
# /customer/complaints/
# /customer/complaints/post -> register a complaint
# /customer/complaints/{id}/{close/escalate/feedback}