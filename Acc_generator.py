import security
import random


for x in range(10000):
    security.reg(name=f"{str(random.randint(100000, 10000000))}abcd", password=f"{str(random.randint(100000, 10000000))}abcd")
    if x % 500 == 0:
        print("oh yeah!", x)
"""
{
    "all_id": [
        "923330879"
    ],
    "name + pass": {
        "923330879": {
            "name": "test",
            "pass": "a123"
        }
    }
}
"""