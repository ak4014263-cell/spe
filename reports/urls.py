from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
	path('', views.reports_login, name='root'),
	path('login/', views.reports_login, name='login'),
	path('logout/', views.reports_logout, name='logout'),
	path('dashboard/', views.dashboard, name='dashboard'),
	# Detail pages
	path('sales/', views.sales_history, name='sales'),
	path('sales/preview/', views.sells_history_preview, name='sales_preview'),
	path('sales/download/xlsx/', views.sells_history_xlsx, name='sales_xlsx'),
	path('sales/download/csv/', views.sells_history_csv, name='sales_csv'),
	path('sales/download/pdf/', views.sells_history_pdf, name='sales_pdf'),

	path('bookings/', views.bookings_list, name='bookings'),
	path('bookings/preview/', views.bookings_list_preview, name='bookings_preview'),
	path('bookings/download/xlsx/', views.bookings_xlsx, name='bookings_xlsx'),
	path('bookings/download/csv/', views.bookings_csv, name='bookings_csv'),
	path('bookings/download/pdf/', views.bookings_pdf, name='bookings_pdf'),

	path('sold/', views.sold_history, name='sold'),
	path('sold/preview/', views.sold_history_preview, name='sold_preview'),
	path('sold/download/xlsx/', views.sold_history_xlsx, name='sold_xlsx'),
	path('sold/download/csv/', views.sold_history_csv, name='sold_csv'),
	path('sold/download/pdf/', views.sold_history_pdf, name='sold_pdf'),
]

