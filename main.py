from binance.spot import Spot as Client

key='3nM52scGguNWEC2yyImui4CWWohYJT5t6oIyLohd9vSeznRbKflBb378qcpNs4Sx'
secret='XG944FnF7FmFbwIKgMNQRKLMIuzOezkp7lXbHPJ4HIiDGZvqAwdUphYEgurux1UW'

client = Client(key, secret, base_url='https://testnet.binance.vision')

print(*client.ticker_price(), sep='\n')
print()
print(*client.account()['balances'], sep='\n')