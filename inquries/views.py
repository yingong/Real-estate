from django.shortcuts import render, redirect
from .models import Inquiry
from django.core.mail import send_mail, EmailMessage
# Create your views here.


def make_inquiry(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        name = request.POST['username']
    if request.user.is_authenticated:
        uid = request.user.id
        re_inq = Inquiry.objects.filter(listing_id=listing_id, user_id=uid)
        if re_inq:
            # already existss
            return redirect('/listings/'+listing_id)
    else:
        uid = ""
    iq = Inquiry(listing=listing, email=email, phone=phone, message=message, name=name,
                 listing_id=listing_id, user_id=uid)

    iq.save()

    # send email
    msg = "Hello "+name+", we've go your inquiry, our stuff will be contacting you within two work days. Thanks for your choice!"

    email = EmailMessage(
        subject="Inquiry Made - Yin's Real Estate",
        body=msg,
        to=[email],
    )
    email.send(fail_silently=False)

    return redirect('dashboard')
