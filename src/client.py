import requests

NODES = [
    "http://127.0.0.1:5001",
    "http://127.0.0.1:5002"
]

def put(key, value):
    success = 0
    for node in NODES:
        try:
            r = requests.put(
                f"{node}/put",
                json={"key": key, "value": value},
                timeout=2
            )
            if r.status_code == 200:
                success += 1
        except requests.exceptions.RequestException:
            pass

    print(f"Write successful on {success}/{len(NODES)} nodes")


def get(key):
    for node in NODES:
        try:
            r = requests.get(
                f"{node}/get",
                params={"key": key},
                timeout=2
            )
            if r.status_code == 200:
                print(f"Read from {node}: {r.json()['value']}")
                return
        except requests.exceptions.RequestException:
            pass

    print("Failed to read value")


if __name__ == "__main__":
    put("name", "Dastan")
    get("name")
