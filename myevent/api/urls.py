from rest_framework.routers import SimpleRouter
from api import views


router = SimpleRouter()

router.register(r'category', views.CategoryViewSet, 'Category')
router.register(r'country', views.CountryViewSet, 'Country')
router.register(r'city', views.CityViewSet, 'City')
router.register(r'event', views.EventViewSet, 'Event')
router.register(r'ticket', views.TicketViewSet, 'Ticket')
router.register(r'registration', views.RegistrationViewSet, 'Registration')
router.register(r'payment', views.PaymentViewSet, 'Payment')

urlpatterns = router.urls
