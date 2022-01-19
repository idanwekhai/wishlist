from django.urls import path


from . import views

app_name = 'wishes'

urlpatterns = [
    path('', views.wish_view, name="wish"),
    path('<int:id>/delete', views.delete_wish, name="delete"),
    path('wish/<slug:s_key>', views.link_view, name="link"),
    path('pdf/<slug:s_key>', views.MyPDFView.as_view(), name="pdf")
]

