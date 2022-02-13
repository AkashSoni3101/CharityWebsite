from django.urls import path
from .views import DonationsListView, DonationDetailView, DonationFeaturedView, DonationCategoryView, EventListView, EventDetailView, EventFeaturedView, GalleryListView, ContactCreateView, BecomeVolunteerListView, OurTeamListView, OurTeamCtaegoryView, TestimonialListView, TestimonialCtaegoryView, start_payment, handle_payment_success

urlpatterns = [
    path('donation', DonationsListView.as_view()),
    path('donation/featured', DonationFeaturedView.as_view()),
    path('donation/category', DonationCategoryView.as_view()),
    path('donation/<slug>', DonationDetailView.as_view()),
    path('event', EventListView.as_view()),
    path('event/<slug>', EventDetailView.as_view()),
    path('featured', EventFeaturedView.as_view()),
    path('gallery', GalleryListView.as_view()),
    path('contact', ContactCreateView.as_view()),
    path('becomevolunteer', BecomeVolunteerListView.as_view()),
    path('ourteam', OurTeamListView.as_view()),
    path('ourteam/category', OurTeamCtaegoryView.as_view()),
    path('testimonial', TestimonialListView.as_view()),
    path('testimonial/category', TestimonialCtaegoryView.as_view()),
    path('pay/', start_payment, name="payment"),
    path('payment/success/', handle_payment_success, name="payment_success")
]