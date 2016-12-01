from django.shortcuts import render, get_object_or_404
# from app.models import About
# from app.models import AboutFeed
# from app.models import Service
# from app.models import Staff
# from app.models import Consultancyservice
# from blog.models import Categories, Posts
from app.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse


# Create your views here.
def index(request):
    home = "Welcome to Cygnal System"
    # homeabout = About.objects.get(title='Aimurafaty')
    # homeservices = Service.objects.all()[:6]
    # categories = Categories.objects.all()
    # posts = Posts.objects.all()[:5]
    context_dict = {'home': home}
    # context_dict = {'about': homeabout, 'services': homeservices,
    #                 'categories': categories, 'posts': posts}
    return render(request, 'app/index.html', context=context_dict)


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" + '',
                ['jattoade@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            messages.success(request, 'Your Message was sent successfully')
            return redirect('contact')
    return render(request, 'app/contact.html', {'form': form_class})