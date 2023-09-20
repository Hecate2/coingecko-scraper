import csv
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

with open('coins-github.csv', 'w') as f:
    w = csv.writer(f)
    for page in range(1, 3, 1):
        print(coins := cg.get_coins_markets('usd', per_page=100, page=page))
        for i, coin in enumerate(coins):
            # There is rate limit for this API, so the requests can be very slow
            print((page-1) * 100 + i + 1, github_links := cg.get_coin_by_id(coin['id'])['links']['repos_url']['github'])
            w.writerow([coin['id'], github_links[0] if len(github_links) else ''])
            f.flush()  # write to disk immediately
# breakpoint()