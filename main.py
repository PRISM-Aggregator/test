
import json
from time import time
from random import choices, random, randint
from string import ascii_uppercase, ascii_lowercase, digits

def rand_str(len, upper=True, lower=True, use_digits=True):
    s = ""
    if use_digits: s+= digits
    if upper: s+= ascii_uppercase
    if lower: s+= ascii_lowercase
    return ''.join(choices(s, k=len))

def make_json():
    with open("data/data.json", "w") as f:
        json.dump(
            {
                "tokens": { 
                    rand_str(randint(4, 8), use_digits=False, upper=False): {
                        "mint": rand_str(45), "ticker": rand_str(randint(3, 6), lower=False, use_digits=False),
                        "price": random()**5 *1000, "mcap": random()**5 *1e9, "24h_vol": random()**5 *1e8,
                        "24h_delta": random()**3 *100 -50,  "last_updated": int(time())-randint(0, 1e6) 
                    }
                    for _ in range(1000)
                },
                "last_updated": int(time())
            }, f, indent=4)





