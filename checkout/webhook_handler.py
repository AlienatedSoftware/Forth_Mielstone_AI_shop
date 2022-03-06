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