from src.llm import get_llm

MAX_QUERY_LEN = 500


def _text(resp) -> str:
    c = resp.content
    if isinstance(c, str):
        return c
    return "".join(p.get("text", "") if isinstance(p, dict) else str(p) for p in c)


def validate_query(query: str) -> str:
    q = query.strip()
    if not q:
        raise ValueError("Query cannot be empty")
    if len(q) > MAX_QUERY_LEN:
        raise ValueError(f"Query too long (max {MAX_QUERY_LEN} chars)")
    return q


def is_in_scope(query: str) -> bool:
    llm = get_llm()
    resp = llm.invoke(
        f"Is this question about a software/infrastructure incident, outage, or "
        f"postmortem? Answer only yes or no.\n\nQuestion: {query}"
    )
    return "yes" in _text(resp).strip().lower()