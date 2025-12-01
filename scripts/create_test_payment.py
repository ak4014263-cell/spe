from speedy_app.core.models import Reservation, Payment
from django.utils import timezone

def run():
    # Create a Reservation if none exists
    reservation, created = Reservation.objects.get_or_create(
        email='testuser@example.com',
        defaults={
            'name': 'Test User',
            'phone': '1234567890',
            'company': 'Test Company',
            'country': 'Testland',
        }
    )
    # Create a Payment for today
    payment = Payment.objects.create(
        reservation=reservation,
        method='PAYPAL',
        amount=100.00,
        paid_at=timezone.now()
    )
    print(f"Created Payment: {payment}")

if __name__ == "__main__":
    run()
