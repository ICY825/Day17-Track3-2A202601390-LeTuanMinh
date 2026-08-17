# Lab 17 — Nộp bài

**Lê Tuấn Minh — 2A202601390.** Practice **11/11 (100%)**, golden **20/20 (`perfect: true`, +10)**, baseline no-memory 2/11 (18.2%).

## 3 câu bắt buộc

**1. Layer quan trọng nhất: long-term.** Nó quyết định 5/11 case (E02, E03, E08, E09 và một nửa E07), và là layer duy nhất chứng minh cross-session recall: `prime_eval_thread` tạo thread trống chỉ chứa câu query, nên mọi marker trả về đều đến từ user graph.

**2. Trade-off Context Block (Zep) vs Redis + Qdrant.** Zep lo extraction, conflict theo `valid_at`/`invalid_at` và lắp context theo relevance — gần như không phải viết code. Đổi lại: ingestion bất đồng bộ (phải poll, thấy rõ khi seed) và tôi không kiểm soát thứ hạng, nên E02/E08 tốn ~1.5k token và ~1.4s mà không cắt được. Redis + Qdrant thì latency ~0 và schema do tôi định, nhưng phải tự viết extraction, versioning fact và conflict resolution — đúng phần khó nhất.

**3. Guardrail chống memory poisoning.** (a) `data/consent.json` + `require_memory_consent` chặn ingest khi chưa opt-in; `minimize_pii` redact email/phone trước khi ghi durable. (b) Heartbeat chạy dry-run và **không** được tự thêm instruction/quyền mới vào durable memory. (c) Mọi call long-term/episodic đều mang `user_id`, nên E09 và G06 không lấy được fact của user khác.

## 4 câu phân tích benchmark

1. **Layer yếu nhất:** không layer nào fail (11/11). Xét chi phí, long-term yếu nhất: token reduction 0%, latency ~1.3–1.4s, so với semantic 86–89% và ~230ms.
2. **Case nhiều token nhất: E08 = 1570 token** (E03 1545, E02 1531) — Context Block gộp cả user summary lẫn facts nên luôn đắt nhất.
3. **E07 cần long-term + semantic**: bắt buộc có `Python` (preference) và `Idempotency-Key` (domain rule); thiếu một là FAIL.
4. **Reduction 18.7% (memory) vs 81.8% (no-memory)** nhưng hit rate 18.2%: baseline "tiết kiệm" bằng cách không retrieve gì. Reduction chỉ có nghĩa khi đọc kèm hit rate.

## E08 recency và E10 compaction

**E08:** fact cũ (Python) không bị xoá mà bị đánh dấu hết hiệu lực; Context Block trả TypeScript + NestJS cho BLUEBIRD-42, Python vẫn đúng cho ORCHID-27 — recency thắng **trong đúng scope**. Tôi thêm `graph.search(scope="edges", limit=25)` để lấy kèm `valid_at`/`invalid_at`.

**E10:** hạ `max_recent_messages` 6→4, raw turn của constraint bị evict hết (compactions 10→12) nhưng `REVIEW-DEADLINE-1600` vẫn sống trong `<DURABLE_NOTES>`. Buffer giữ tất cả nên token tăng tuyến tính.
