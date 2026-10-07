from scripts.search import search
from scripts.hybrid_search import hybrid_search
from src.test.data.golden_hard import GOLDEN_HARD
from run_golden import run
import time
K = 5



if __name__ == "__main__":
    run("vector-only", search, GOLDEN_HARD)

    time.sleep(21)

    run("hybrid", hybrid_search, GOLDEN_HARD)