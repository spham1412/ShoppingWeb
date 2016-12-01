from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


@login_required
def checkout(request):
    publish_key = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = request.user.userstripe.stripe_id
    if request.method == 'POST':
        print 'request.POST', request.POST
        token = request.POST.get('stripeToken')
        print 'token', token
        # Create a charge: this will charge the user's card
        try:
            customer = stripe.Customer.retrieve(customer_id)
            customer.sources.create(source=token)
            charge = stripe.Charge.create(
                amount=1000000,  # Amount in cents
                currency="usd",
                customer=customer,
                description="Example charge"
            )
        except stripe.error.CardError as e:
            # The card has been declined
            pass
    context = {'publish_key': publish_key}
    template = 'checkout.html'
    return render(request, template, context)
