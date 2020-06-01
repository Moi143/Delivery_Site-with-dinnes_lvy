from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('register/',views.registerpage,name='register_page'),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('user/',views.userpage,name='user_page'),
    path('customer_profile/<str:pk_text>/',views.customer,name='customer'),
    path('account_setting',views.account_setting,name='customer_account_setting'),
    
    path('create_order/<str:pk>/',views.create_order,name="create_order"),
    path('Update_order/<str:pk1>/',views.update_order,name='update'),
    path('delete_order/<str:pk2>/',views.delete,name='delete'),

        path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),
]