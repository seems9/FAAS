import json
import sys


def get_price_info(*args):

    qty = args[0]

    with open('priceinfo.json', 'r') as f:

        data = json.load(f)

    tot_price = data["price"] * qty

    with open('totpriceinfo.json', 'w+') as f:

        d = {
            "sku": data["sku"],
            "name": data["name"],
            "orig_price": data["price"],
            "tot_price": tot_price
        }

        json.dump(d, f)

        sys.stdout.write(str(json.dumps(d)))
        sys.stdout.flush()
