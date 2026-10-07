from scripts.search import search
from scripts.hybrid_search import hybrid_search
import time
GOLDEN = [
    ("database transaction ID wraparound causing outage", "Database"),
    ("primary key integer overflow", "Database"),
    ("MySQL replica crash during migration", "Database"),
    ("config change broke DNS resolution", "Config Errors"),
    ("configuration rollout caused health check failures", "Config Errors"),
    ("policy change blocked access to resources", "Config Errors"),
    ("datacenter cooling system failure", "Hardware/Power Failures"),
    ("generator failed to start during power outage", "Hardware/Power Failures"),
    ("race condition during failover caused split brain", "Conflicts"),
    ("network partition caused two masters", "Conflicts"),
    ("leap second caused DNS resolver to crash", "Time"),
    ("certificate expiry caused mass outage", "Time"),
    ("attacker compromised support engineer laptop", "Security"),
    ("parser bug leaked private memory", "Security"),
    ("DDoS attack overwhelmed network", "Networking"),
    ("kubernetes upgrade broke pod networking", "Networking"),
    ("sudden traffic spike exhausted capacity", "Capacity/Overload"),
    ("queue backed up under peak load", "Capacity/Overload"),
    ("operator ran wrong command and deleted data", "Operational/Human Error"),
    ("engineer's mistake caused data loss", "Operational/Human Error"),
]

K = 5


def hit_at_k(results, expected_category):
    return any(r["category"] == expected_category for r in results[:K])


def run(name, search_fn):
    hits = 0
    for query, expected in GOLDEN:
        results = search_fn(query, K)  # adjust args to match each function's signature
        if hit_at_k(results, expected):
            hits += 1
        time.sleep(21)
    print(f"{name}: {hits}/{len(GOLDEN)} = {hits/len(GOLDEN):.2f}")

if __name__ == "__main__":
    run("vector-only", search)
    run("hybrid", hybrid_search)