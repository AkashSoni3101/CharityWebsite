from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from backend.models import Donations, Events, Gallery, Contact, BecomeVolunteer, OurTeam, Testimonial, Order
from backend.serializers import DonationSerializer, EventSerializer, GallerySerializer, ContactSerializer, BecomeVolunteerSerializer, OurTeamSerializer, TestimonialSerializer, OrderSerializer
from django.core.mail import send_mail
import json
import environ
import razorpay

class DonationsListView(ListAPIView):
    queryset = Donations.objects.order_by('-date_created')
    serializer_class = DonationSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class DonationDetailView(RetrieveAPIView):
    queryset = Donations.objects.order_by('-date_created')
    serializer_class = DonationSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class DonationFeaturedView(ListAPIView):
    queryset = Donations.objects.all().filter(featured=True)
    serializer_class = DonationSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class DonationCategoryView(APIView):
    serializer_class = DonationSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = Donations.objects.order_by('-date_created').filter(category__iexact=category)

        serializer = DonationSerializer(queryset, many=True)

        return Response(serializer.data)

class EventListView(ListAPIView):
    queryset = Events.objects.order_by('-date_created')
    serializer_class = EventSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class EventDetailView(RetrieveAPIView):
    queryset = Events.objects.order_by('-date_created')
    serializer_class = EventSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class EventFeaturedView(ListAPIView):
    queryset = Events.objects.all().filter(featured=True)
    serializer_class = EventSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class GalleryListView(ListAPIView):
    queryset = Gallery.objects.order_by('-date_created')
    serializer_class = GallerySerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class ContactCreateView(APIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        try:
            send_mail(
                data['subject'],
                'Name: '
                + data['name']
                + '\nEmail: '
                + data['email']
                + '\n\nMessage:\n'
                + data['message'],
                'akash.soni.3101@gmail.com',
                ['akash.soni.3101@gmail.com'],
                fail_silently=False
            )

            contact = Contact(name=data['name'], email=data['email'], subject=data['subject'], message=data['message'])
            contact.save() 

            return Response({'success': 'Message sent successfully!'})

        except:
            return Response({'error': 'Message failed to send!'})

class BecomeVolunteerListView(ListAPIView):
    serializer_class = BecomeVolunteerSerializer
    permission_classes = (permissions.AllowAny, )

    
    def post(self, request, format=None):
        data = self.request.data

        try:
            details = BecomeVolunteer(name=data['name'], email=data['email'], phonenumber=data['phonenumber'], address=data['address'], DOB=data['DOB'], occupation=data['occupation'], message=data['message'])
            details.save()

            return Response({"Registration successfully"})
        
        except:

            return Response({"Registration Failed"})

class OurTeamListView(ListAPIView):
    queryset = OurTeam.objects.order_by('-date_created').reverse()
    serializer_class = OurTeamSerializer
    permission_classes = (permissions.AllowAny, )

class OurTeamCtaegoryView(ListAPIView):
    serializer_class = OurTeamSerializer
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = OurTeam.objects.order_by('-date_created').filter(category__iexact=category).reverse()

        serializer = OurTeamSerializer(queryset, many=True)

        return Response(serializer.data)

class TestimonialListView(ListAPIView):
    queryset = Testimonial.objects.order_by('-date_created').reverse()
    serializer_class = TestimonialSerializer
    permission_classes = (permissions.AllowAny, )

class TestimonialCtaegoryView(ListAPIView):
    serializer_class = TestimonialSerializer
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = Testimonial.objects.order_by('-date_created').filter(category__iexact=category).reverse()

        serializer = TestimonialSerializer(queryset, many=True)

        return Response(serializer.data)

env = environ.Env()

environ.Env.read_env()

def start_payment(request):
    # request.data is coming from frontend
    amount = request.data['amount']
    name = request.data['name']

    # setup razorpay client this is the client to whome user is paying money that's you
    client = razorpay.Client(auth=(env('PUBLIC_KEY'), env('SECRET_KEY')))

    # create razorpay order
    # the amount will come in 'paise' that means if we pass 50 amount will become
    # 0.5 rupees that means 50 paise so we have to convert it in rupees. So, we will 
    # mumtiply it by 100 so it will be 50 rupees.
    payment = client.order.create({"amount": int(amount) * 100, 
                                   "currency": "INR", 
                                   "payment_capture": "1"})

    # we are saving an order with isPaid=False because we've just initialized the order
    # we haven't received the money we will handle the payment succes in next 
    # function
    order = Order.objects.create(order_product=name, 
                                 order_amount=amount, 
                                 order_payment_id=payment['id'])

    serializer = OrderSerializer(order)

    """order response will be 
    {'id': 17, 
    'order_date': '23 January 2021 03:28 PM', 
    'order_product': '**product name from frontend**', 
    'order_amount': '**product amount from frontend**', 
    'order_payment_id': 'order_G3NhfSWWh5UfjQ', # it will be unique everytime
    'isPaid': False}"""

    data = {
        "payment": payment,
        "order": serializer.data
    }
    return Response(data)

def handle_payment_success(request):
    # request.data is coming from frontend
    res = json.loads(request.data["response"])

    """res will be:
    {'razorpay_payment_id': 'pay_G3NivgSZLx7I9e', 
    'razorpay_order_id': 'order_G3NhfSWWh5UfjQ', 
    'razorpay_signature': '76b2accbefde6cd2392b5fbf098ebcbd4cb4ef8b78d62aa5cce553b2014993c0'}
    this will come from frontend which we will use to validate and confirm the payment
    """

    ord_id = ""
    raz_pay_id = ""
    raz_signature = ""

    # res.keys() will give us list of keys in res
    for key in res.keys():
        if key == 'razorpay_order_id':
            ord_id = res[key]
        elif key == 'razorpay_payment_id':
            raz_pay_id = res[key]
        elif key == 'razorpay_signature':
            raz_signature = res[key]

    # get order by payment_id which we've created earlier with isPaid=False
    order = Order.objects.get(order_payment_id=ord_id)

    # we will pass this whole data in razorpay client to verify the payment
    data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
    }

    client = razorpay.Client(auth=(env('PUBLIC_KEY'), env('SECRET_KEY')))

    # checking if the transaction is valid or not by passing above data dictionary in 
    # razorpay client if it is "valid" then check will return None
    check = client.utility.verify_payment_signature(data)

    if check is not None:
        print("Redirect to error url or error page")
        return Response({'error': 'Something went wrong'})

    # if payment is successful that means check is None then we will turn isPaid=True
    order.isPaid = True
    order.save()

    res_data = {
        'message': 'payment successfully received!'
    }

    return Response(res_data)