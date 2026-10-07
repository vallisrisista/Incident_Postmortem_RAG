from scripts.search import search
from scripts.hybrid_search import hybrid_search
from src.test.data.golden_keyword import GOLDEN_KEYWORD
from run_golden import run
import time
K = 5



if __name__ == "__main__":
    run("vector-only", search, GOLDEN_KEYWORD)

    time.sleep(21)

    run("hybrid", hybrid_search, GOLDEN_KEYWORD)