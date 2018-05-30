import json
import sys


def get_tax_info(*args):

    with open('totpriceinfo.json', 'r') as f:

        data = json.load(f)

    tax = 0.10
    pricetax = (data["tot_price"] * tax) + data["tot_price"]

    with open('taxpriceinfo.json', 'w+') as f:

        d = {
            "sku": data["sku"],
            "name": data["name"],
            "orig_price": data["orig_price"],
            "tot_price": data['tot_price'],
            "pricetax": pricetax
        }

        json.dump(d, f)

        sys.stdout.write(str(json.dumps(d)))
        sys.stdout.flush()
