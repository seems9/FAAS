import json
import sys


def get_prd_info(*args):

    sku = args[0]

    with open('products.json', 'r') as f:

        data = json.load(f)

        for d in data:

            if(d['sku'] == sku):

                with open('priceinfo.json', 'w+') as f:

                    json.dump(d, f)

                    sys.stdout.write(str(json.dumps(d)))
                    sys.stdout.flush()
