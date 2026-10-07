from scripts.search import search
from scripts.hybrid_search import hybrid_search
import time

QUERY = "new records cannot be created because an integer identifier reached its maximum value"
EXPECTED_ID = "1d6c07a2aa98"
K = 10


def test_search(name, search_fn):
    results = search_fn(QUERY, K)

    print(f"\n{name}")
    print(f"Query: {QUERY}")
    print(f"Expected ID: {EXPECTED_ID}")

    found = False

    for rank, r in enumerate(results, start=1):
        print(
            f"{rank}. id={r['_id']} | "
            f"company={r.get('company')} | "
            f"category={r.get('category')}"
        )

        if r["_id"] == EXPECTED_ID:
            print(f"--> EXPECTED INCIDENT FOUND AT RANK {rank}")
            found = True

    if not found:
        print(f"--> EXPECTED INCIDENT NOT FOUND IN TOP {K}")


if __name__ == "__main__":
    test_search("vector-only", search)

    time.sleep(21)

    test_search("hybrid", hybrid_search)