from __future__ import annotations

import json
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty, normalize
from .zep_common import prime_eval_thread, render_graph_search, safe_call


def compact_kb_text(rendered: str) -> str:
    """Squeeze redundancy out of a domain-graph render before budgeting.

    The seeder adds every knowledge document twice, once as JSON and once as
    plain text, so a raw render spends roughly half the 3% semantic budget
    repeating itself and can push the one document a query actually needs past
    the trim point. Unwrapping the JSON envelope to `entity - summary` and
    dropping duplicate bodies keeps every marker while fitting more distinct
    documents inside the same budget.
    """
    kept: list[str] = []
    seen: list[str] = []
    for raw_line in rendered.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("metadata="):
            continue

        prefix, _, body = line.partition(": ")
        if not body:
            prefix, body = "KB", line

        if body.startswith("{"):
            try:
                doc = json.loads(body)
            except json.JSONDecodeError:
                pass
            else:
                entity = str(doc.get("entity") or doc.get("id") or "")
                summary = str(doc.get("summary") or "")
                body = f"{entity} - {summary}".strip(" -") or body

        key = normalize(body)
        if not key or any(key in other or other in key for other in seen):
            continue
        seen.append(key)
        kept.append(f"{prefix}: {body}")

    return join_nonempty(kept)


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # LAB TODO 1/4 - done.
        # The eval thread is recreated and primed with the query only, so the
        # Context Block Zep returns is built from the USER graph (facts learned
        # in earlier threads), not from a transcript copied into this thread.
        prime_eval_thread(self.client, user_id, thread_id, query)
        context = self.client.thread.get_user_context(thread_id=thread_id)
        parts = [str(getattr(context, "context", "") or "")]

        # The Context Block is relevance-ranked and can drop a fact that matters
        # for a specific case (an open loop, or the fact that superseded an older
        # one). A user-scoped edge search with a generous limit adds those facts
        # back together with their validity range, which is what makes recency
        # legible instead of guessed.
        facts = safe_call(
            self.client.graph.search,
            user_id=user_id,
            query=cap_query(query),
            scope="edges",
            limit=25,
        )
        if facts is not None:
            parts.append(render_graph_search(facts))

        return join_nonempty(parts)

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # LAB TODO 2/4 - done.
        # Episodes are user-scoped: search the user graph, never the shared
        # domain graph, or E09-style isolation breaks.
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=8,
        )
        # Session messages come back verbose; without a per-episode cap one or
        # two of them eat the whole 3% episodic budget and the short reflection
        # carrying the marker gets trimmed away.
        return render_graph_search(results, episode_char_cap=900)

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # LAB TODO 3/4 - done.
        # Standalone domain graph: graph_id, not user_id.
        # scope="episodes" returns the raw ingested document text, which keeps
        # literal markers such as PAYMENT-RULE-3 or CONN-POOL-FIRST.
        # scope="auto" would return extracted facts and drop those codes.
        results = safe_call(
            self.client.graph.search,
            graph_id=graph_id,
            query=cap_query(query),
            scope="episodes",
            limit=10,
        )
        text = compact_kb_text(render_graph_search(results)) if results is not None else ""
        if text.strip():
            return text

        # Fallback for the rare case where episode search returns nothing.
        nodes = safe_call(
            self.client.graph.search,
            graph_id=graph_id,
            query=cap_query(query),
            scope="nodes",
            limit=10,
        )
        return compact_kb_text(render_graph_search(nodes)) if nodes is not None else ""

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # LAB TODO 4/4 - done.
        # ContextBudgetManager already encodes the 10/4/3/3 budget and the
        # short_term -> long_term -> episodic -> semantic priority order, and
        # trims from the tail so the top-ranked head of each layer survives.
        return self.budget.assemble(layers)
