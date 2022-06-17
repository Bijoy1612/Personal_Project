from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("products/<int:myid>", views.product, name="Product"),
    path("checkout/", views.checkout, name="Checkout"),
    path("tracker/", views.tracker, name="Tracker"),
]