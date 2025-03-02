import requests
from django.http import JsonResponse

ALPHA_VANTAGE_API_KEY = 'ENTER YOUR API KEY HERE '
BASE_URL = 'https://www.alphavantage.co/query'


def get_multiple_stocks(request):
    symbols = request.GET.getlist('symbols')  # Accept multiple symbols from URL query params
    stock_data = {}

    for symbol in symbols:
        url = f'{BASE_URL}?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={ALPHA_VANTAGE_API_KEY}'
        response = requests.get(url)
        data = response.json()

        if 'Time Series (5min)' in data:
            latest_time = list(data['Time Series (5min)'].keys())[0]
            latest_data = data['Time Series (5min)'][latest_time]
            stock_data[symbol] = {'time': latest_time, 'price': latest_data['4. close']}
        else:
            stock_data[symbol] = {'error': 'Invalid symbol or data not available'}

    return JsonResponse(stock_data)