from django.urls import path
from collab_app import views

app_name = 'collab_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact_us/', views.contact_us, name='contact_us'),

    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login, name='login'),
    path('<slug:account_name_slug>/', views.my_account, name='my_account'),

    # General pages
    path('general/', views.general, name='general'),
    path('general/add_category/', views.add_category,
          name='add_general_category'),
    path('general/<slug:category_name_slug>', views.show_category,
          name='show_general_category'),
    path('general/<slug:category_name_slug>/add_page/', views.add_page,
          name='add_general_page'),
    path('general/<slug:category_name_slug>/<slug:page_name_slug>/',
          views.show_page, name='show_general_page'),

    # University pages
    path('universities/', views.universities, name='universities'),
    
    path('universities/add_university/', views.add_university,
          name='add_university'),
    path('universities/<slug:university_name_slug>/',
          views.show_university, name='show_university'),

    path('universities/<slug:university_name_slug>/add_category/',
          views.add_category, name='add_university_category'),
    path('universities/<slug:university_name_slug>/<slug:category_name_slug>/',
          views.show_category, name='show_university_category'),

    path('universities/<slug:university_name_slug>/<slug:category_name_slug>/add_page',
          views.add_page, name='add_university_page'),
    path('universities/<slug:university_name_slug>/<slug:category_name_slug>/<slug:page_name_slug>/',
          views.show_page, name='show_university_page')
]