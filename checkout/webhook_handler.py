from django.http import HttpResponse

# Handles stripe webhooks
class StripeWH_Handler:
    
    def __init__(self, request):
        self.request = request

    # Handles unexpected webhook events
    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    # Handles the payment_intent.succeeded webhook from Stripe
    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    # Handles the payment_intent.payment_failed webhook from Stripe
    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)