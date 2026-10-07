from scripts.search import search
from scripts.hybrid_search import hybrid_search
from src.test.data.golden_realistic import GOLDEN_REALISTIC
from run_golden import run
K = 5



if __name__ == "__main__":
    run("vector-only", search,GOLDEN_REALISTIC)
    run("hybrid", hybrid_search,GOLDEN_REALISTIC)