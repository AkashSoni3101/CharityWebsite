from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Donations, Events, Gallery, Contact, BecomeVolunteer, OurTeam, Testimonial, Order

class DonationAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'category', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content', )

admin.site.register(Donations, DonationAdmin)


class EventAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content', )

admin.site.register(Events, EventAdmin)


class GalleryAdmin(SummernoteModelAdmin):
    exclude = ('slug', )
    list_display = ('id', 'title', 'date_created')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    
admin.site.register(Gallery, GalleryAdmin)


class ContactAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')
    list_display_links = ('id', 'name')
    search_field = ('name', 'email', 'subject')
    list_per_page = 25
    
admin.site.register(Contact, ContactAdmin)


class BecomeVolunteerAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'email', 'phonenumber')
    list_display_links = ('id', 'name')
    search_field = ('name', 'email', 'phonenumber')
    list_per_page = 25
    
admin.site.register(BecomeVolunteer, BecomeVolunteerAdmin)


class OurTeamAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'category' )
    list_per_page = 25
    
admin.site.register(OurTeam, OurTeamAdmin)


class TestimonialAdmin(SummernoteModelAdmin):
    list_display = ('id', 'name', 'category')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'category' )
    list_per_page = 25
    
admin.site.register(Testimonial, TestimonialAdmin)

admin.site.register(Order)