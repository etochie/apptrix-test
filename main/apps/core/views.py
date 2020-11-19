from django.shortcuts import render, redirect
from django.core.mail import send_mail

from apps.core.models import TopBackgroundImage, ItemModel, Block3Image,\
    Reviews, Contacts
from .forms import OrderForm

def landing(request):
    form = OrderForm()
    top_background = TopBackgroundImage.objects.last()
    items = ItemModel.objects.filter(is_main=True)
    block_3_images = Block3Image.objects.last()
    reviews = Reviews.objects.last()
    contacts = Contacts.objects.last()
    context = {
        'top_backgroung': top_background,
        'items': items,
        'block_3_images': block_3_images,
        'reviews': reviews,
        'contacts': contacts,
        'form': form
    }
    return render(request, 'core/landing.html', context)

def order_email(request):
    if request.method == 'POST':
        from_email = Contacts.objects.last().email
        to_email = request.POST['email']
        send_mail(
            'Subject here',
            'Here is the message.',
            from_email=from_email,
            recipient_list=[to_email],
            fail_silently=False,
        )
    return redirect('landing_url')