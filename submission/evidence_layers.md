# Bang chung retrieval theo tung layer

Trich tu `reports/benchmark.json` (--impl student, practice 11/11) va `reports/golden_benchmark.json` (golden 20/20).

## long_term

### E02 — PASS · 1368.7 ms · 1531 tokens

Query: Voi demo ca nhan cua Minh, ngon ngu uu tien la gi?

```text
<USER_SUMMARY>
The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.

Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. When discussing async/await, coroutines, and Tasks, explain them using a timeline, and the AI will prioritize timelines for these topics. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python is not to be used for this project, but Python is still preferred for the personal project ORCHID-27.
</USER_SUMMARY>

<EPISODES>
Episodes are source message or document excerpts shown in selection order.
  - Created At: 2026-08-17 10:01:39
    Source: message
    Content: [user] {
  "u
```

### E03 — PASS · 1404.8 ms · 1545 tokens

Query: Minh con open loop hay deadline nao chua hoan thanh?

```text
<USER_SUMMARY>
The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.

Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. When discussing async/await, coroutines, and Tasks, explain them using a timeline, and the AI will prioritize timelines for these topics. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python is not to be used for this project, but Python is still preferred for the personal project ORCHID-27.
</USER_SUMMARY>

<EPISODES>
Episodes are source message or document excerpts shown in selection order.
  - Created At: 2026-08-17 10:01:35
    Source: message
    Content: [user] {
  "u
```

### E08 — PASS · 1304.4 ms · 1570 tokens

Query: Backend cua BLUEBIRD-42 bat buoc dung stack gi?

```text
<USER_SUMMARY>
The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.

Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. When discussing async/await, coroutines, and Tasks, explain them using a timeline, and the AI will prioritize timelines for these topics. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python is not to be used for this project, but Python is still preferred for the personal project ORCHID-27.
</USER_SUMMARY>

<EPISODES>
Episodes are source message or document excerpts shown in selection order.
  - Created At: 2026-08-17 10:01:42
    Source: message
    Content: [user] {
  "u
```

### E09 — PASS · 1307.1 ms · 803 tokens

Query: Lan uu tien stack backend nao cho LOTUS-88?

```text
<USER_SUMMARY>
Lan's project is LOTUS-88, prioritizing Java and Spring Boot for backend examples.

Lan prefers Java and Spring Boot, and does not use Python for backend development.
</USER_SUMMARY>

<EPISODES>
Episodes are source message or document excerpts shown in selection order.
  - Created At: 2026-08-01 11:00:20
    Source: message
    Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.
  - Created At: 2026-08-01 11:00:00
    Source: message
    Content: [user] {
  "user_id": "lan-lab17",
  "first_name": "Lan",
  "last_name": "Tran",
  "user_alias": "Lan Tran"
}: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.
</EPISODES>

<FACTS>
The timestamp shown for each fact is the reference time of the source message that introduced it — i.e. when the fact was first mentioned. `date unknown` means no reference time is recorded for the source message.
  - Lan Tran's project is LOTUS-88. (2026-08-01 11:00:00)
  - Da hieu is LOTUS-88. (2026-08-01 11:00:20)
  - Lan Tran prioritizes Java. (2026-08-01 11:00:00)
  - Lan Tran prioritizes Spring Boot. (2026-08-01 11:00:00)
  - Lan Tran
```

## episodic

### E04 — PASS · 294.6 ms · 372 tokens

Query: Lan truoc Minh fix async HTTP timeout bang cach nao?

```text
EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline.
EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.
EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.
EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi? Chi preference cua Minh, dung tron so thich dong nghiep.
EPISODE: Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam mot minh, ma su co async lan truoc, va buoc playbook truoc khi tang timeout. Scope Minh, dung tron Lan.
EPISODE: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh thuc trong lab.
EPISODE: Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? 
```

### E05 — PASS · 280.3 ms · 356 tokens

Query: Reflection cua su co async la gi, tang timeout co phai root fix khong?

```text
EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan.
EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail.
EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20.
EPISODE: Voi demo ca nhan cua Minh, ngon ngu uu tien la gi?
EPISODE: Cuoi tuan minh ngoi mot minh lam demo rieng, khong hop team. Truoc khi chon template, nhac lai: khi lam viec ca nhan minh uu tien ngon ngu nao, va ma du an demo ca nhan la gi? Chi preference cua Minh, dung tron so thich dong nghiep.
EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. Ghep hai manh: stack ca nhan cua Minh, va buoc bat buoc trong playbook truoc khi noi timeout. Dung lay stack cua ai khac.
EPISODE: Toi nay minh viet tool ca nhan de tai hien su co HTTP roi sua dung playbook. Can ba manh: ngon ngu minh thich khi lam mot minh, ma su co async lan truoc, va buoc playbook truoc khi tang time
```

## semantic

### E06 — PASS · 413.7 ms · 60 tokens

Query: Quy tac retry POST payment la gi?

```text
EPISODE: Payment API Retry Policy - For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.
```

### E11 — PASS · 229.9 ms · 60 tokens

Query: Theo incident playbook, truoc khi tang timeout can kiem tra gi?

```text
EPISODE: Async HTTP Incident Playbook - When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.
```

## mixed

### E07 — PASS · 1859.7 ms · 397 tokens

Query: Hay chon huong dan code retry payment phu hop voi preference ca nhan cua Minh.

```text
<LONG_TERM>
<USER_SUMMARY>
The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.

Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. When discussing async/await, coroutines, and Tasks, explain them using a timeline, and the AI will prioritize timelines for these topics. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS; Python is not to be used for this project, but Python is still preferred for the personal project ORCHID-27.
</USER_SUMMARY>

<EPISODES>
Episodes are source message or document excerpts shown in selection order.
  - Created At: 2026-08-17 10:01:27
    Source: message
    Content: [
```

## Golden 20/20

| Case | Layer | Pass | Latency ms |
| --- | --- | --- | ---: |
| G01 | short_term | PASS | 1.3 |
| G02 | short_term | PASS | 0.0 |
| G06 | long_term | PASS | 1904.5 |
| G09 | semantic | PASS | 259.0 |
| G10 | semantic | PASS | 255.3 |
| G14 | mixed | PASS | 1639.6 |
| G03 | long_term | PASS | 1354.1 |
| G04 | long_term | PASS | 1631.6 |
| G07 | episodic | PASS | 390.0 |
| G08 | episodic | PASS | 246.9 |
| G11 | mixed | PASS | 1679.7 |
| G13 | mixed | PASS | 504.1 |
| G15 | mixed | PASS | 1976.3 |
| G16 | mixed | PASS | 1700.3 |
| G17 | mixed | PASS | 1617.6 |
| G18 | mixed | PASS | 495.2 |
| G19 | mixed | PASS | 1794.9 |
| G05 | long_term | PASS | 1425.8 |
| G12 | mixed | PASS | 1621.2 |
| G20 | mixed | PASS | 1670.3 |
