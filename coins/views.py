from django.views.generic import TemplateView
from .services import get_coins
from .models import Currency

class GetCoinInfo(TemplateView):
    template_name = 'coins/coinslist.html'

    def get_context_data(self, *args, **kwargs):
        get_coins()
        context = {
            'coins': Currency.objects.all(),
        }
        return context

