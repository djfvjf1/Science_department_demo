from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [

    path('', views.prehome, name='prehome'),
    path('home/', views.home, name='home'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/', views.profile_view, name='profile'),

    path('KPI/', views.kpi, name='kpi'),

    path('table/', views.new_form, name='create_table'),
    path('table/<int:pk>/', views.table_page, name = 'table_page'),
    path('table/<int:pk>/edit/', views.edit_form, name='edit_form'),

    path('table2/', views.new_form2, name='create_table2'),
    path('table2/<int:pk>/', views.table_page2, name = 'table_page2'),
    path('table2/<int:pk>/edit/', views.edit_form2, name='edit_form2'),

    path('table3/', views.new_form3, name='create_table3'),
    path('table3/<int:pk>/', views.table_page3, name = 'table_page3'),
    path('table3/<int:pk>/edit/', views.edit_form3, name='edit_form3'),

    path('table4/', views.new_form4, name='create_table4'),
    path('table4/<int:pk>/', views.table_page4, name = 'table_page4'),
    path('table4/<int:pk>/edit/', views.edit_form4, name='edit_form4'), 

    path('table5/', views.new_form5, name='create_table5'),
    path('table5/<int:pk>/', views.table_page5, name = 'table_page5'),
    path('table5/<int:pk>/edit/', views.edit_form5, name='edit_form5'), 

    path('table6/', views.new_form6, name='create_table6'),
    path('table6/<int:pk>/', views.table_page6, name = 'table_page6'),
    path('table6/<int:pk>/edit/', views.edit_form6, name='edit_form6'), 

    path('table7/', views.new_form7, name='create_table7'),
    path('table7/<int:pk>/', views.table_page7, name = 'table_page7'),
    path('table7/<int:pk>/edit/', views.edit_form7, name='edit_form7'), 

    path('table8/', views.new_form8, name='create_table8'),
    path('table8/<int:pk>/', views.table_page8, name = 'table_page8'),
    path('table8/<int:pk>/edit/', views.edit_form8, name='edit_form8'), 

    path('table9/', views.new_form9, name='create_table9'),
    path('table9/<int:pk>/', views.table_page9, name = 'table_page9'),
    path('table9/<int:pk>/edit/', views.edit_form9, name='edit_form9'), 

   # path('export/', views.export_data_to_word, name='export_data_to_word'),
    path('export1/', views.export_data_to_word_for_table, name='export_data_to_word'),
    path('export2/', views.export_data_to_word_for_table2, name='export_data_to_word2'),
    path('export3/', views.export_data_to_word_for_table3, name='export_data_to_word3')
    # path('export4/', views.export_data_to_word_for_table4, name='export_data_to_word4')
    # path('export5/', views.export_data_to_word_for_table5, name='export_data_to_word5')
    # path('export6/', views.export_data_to_word_for_table6, name='export_data_to_word6')
    # path('export7/', views.export_data_to_word_for_table7, name='export_data_to_word7')
    # path('export8/', views.export_data_to_word_for_table8, name='export_data_to_word8')
    # path('export9/', views.export_data_to_word_for_table9, name='export_data_to_word9')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)