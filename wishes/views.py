from django.shortcuts import (get_object_or_404, render,
                            HttpResponseRedirect)
from django.views.generic.base import View
#from easy_pdf.views import PDFTemplateView
from wkhtmltopdf.views import PDFTemplateResponse

from .models import Wish
from .forms import WishForm
# Create your views here.



def wish_view(request):
    wishes = Wish.objects.all()
    wish_form = WishForm()

    if not request.session.session_key:
        request.session.create()
    s_key = request.session.session_key

    if request.method == 'POST':

        name = request.POST['name']
        price = request.POST['price']
        link = request.POST['link']


        new_wish = Wish(name=name, price=price, link=link, sess_key=s_key)
        new_wish.save()
        wish_form = WishForm()
    else:
        wish_form = WishForm()

    baseurl = request.build_absolute_uri()

    context = {"wishes": wishes,
                "wish_form": wish_form,
                 "s_key": s_key,
                 "baseurl": baseurl[:-1]}

    return render(request, "wishes/index.html", context)


def delete_wish(request, id):
    context = {}

    obj = get_object_or_404(Wish, id = id)


    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "wishes/index.html", context)


def link_view(request, s_key):

    wishes = Wish.objects.filter(sess_key=s_key)

    context = {"wishes":wishes}

    return render(request, "wishes/list.html", context)


class MyPDFView(View):
    template= "wishes/list.html"


    def get(self, request, s_key):

        wishes = Wish.objects.filter(sess_key=s_key)

        self.context= {"wishes":wishes}

        response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       filename="wishlist.pdf",
                                       context= self.context,
                                       show_content_in_browser=True,
                                       cmd_options={'margin-top': 50,},
                                       )
        return response
