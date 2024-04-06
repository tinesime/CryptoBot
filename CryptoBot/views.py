import ccxt
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def get_eth_price(request):
    exchange = ccxt.bitmex()
    ticker = exchange.fetch_ticker('ETH/EUR')
    return JsonResponse({'price': ticker['last']})