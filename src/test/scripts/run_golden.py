import time

K = 5


def safe_search(search_fn, query, k, retries=3):
    for attempt in range(retries):
        try:
            return search_fn(query, k)

        except Exception as e:
            print(f"Search failed: {e}")

            if attempt < retries - 1:
                print("Retrying in 30 seconds...")
                time.sleep(30)
            else:
                raise


def run(name, search_fn, GOLDEN):
    hit1 = 0
    hit3 = 0
    hit5 = 0
    reciprocal_rank_sum = 0

    for query, expected_id in GOLDEN:

        results = safe_search(search_fn, query, K)

        retrieved_ids = [r["_id"] for r in results[:K]]

        rank = None

        for i, retrieved_id in enumerate(retrieved_ids, start=1):
            if retrieved_id == expected_id:
                rank = i
                break

        if rank is not None:

            if rank <= 1:
                hit1 += 1

            if rank <= 3:
                hit3 += 1

            if rank <= 5:
                hit5 += 1

            reciprocal_rank_sum += 1 / rank

            print(f"HIT | rank={rank} | {query}")

        else:
            print(f"MISS | {query}")

        time.sleep(21)

    total = len(GOLDEN)

    print(f"\n{name}")
    print(f"Hit@1: {hit1}/{total} = {hit1/total:.2f}")
    print(f"Hit@3: {hit3}/{total} = {hit3/total:.2f}")
    print(f"Hit@5: {hit5}/{total} = {hit5/total:.2f}")
    print(f"MRR:   {reciprocal_rank_sum/total:.2f}")