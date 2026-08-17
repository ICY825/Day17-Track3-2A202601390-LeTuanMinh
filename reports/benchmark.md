# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1045.4 ms**
- Average token reduction vs full source context: **18.7%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| E06 | semantic | PASS | 515.8 | 60 | 86.9% |  |
| E09 | long_term | PASS | 1681.1 | 803 | 0.0% |  |
| E10 | short_term | PASS | 0.5 | 195 | 0.0% |  |
| E02 | long_term | PASS | 2210.5 | 1543 | 0.0% |  |
| E03 | long_term | PASS | 1581.5 | 1547 | 0.0% |  |
| E04 | episodic | PASS | 256.8 | 372 | 0.0% |  |
| E05 | episodic | PASS | 258.6 | 356 | 0.0% |  |
| E07 | mixed | PASS | 2689.7 | 397 | 29.7% |  |
| E11 | semantic | PASS | 241.6 | 60 | 89.4% |  |
| E08 | long_term | PASS | 2063.5 | 1563 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: Payment API Retry Policy - For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.`

### E09 - long_term

`<USER_SUMMARY> Lan's project is LOTUS-88, prioritizing Java and Spring Boot for backend examples.  Lan prefers Java and Spring Boot, and does not use Python for backend development. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khon`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.  Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. When discussin`

### E03 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.  Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. When discussin`

### E04 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Minh con mot open-loop phai nop truoc deadline, dong thoi muon ghi chu retry payment dung so lan toi da theo policy. Nac lai ma task/deadline con dang do, va gioi han retry chinh thuc trong lab. EPISODE: Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Cuoi tuan minh ngoi mot minh lam dem`

### E05 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. Ghep hai manh: stack ca nhan cua Minh, va buoc bat buoc trong playbook truoc khi noi timeout. Dung lay stack cua ai khac. EPISODE: Chuan bi demo ca nhan: ten/ma project rieng cua Minh la gi, va lan async HTTP truoc minh reuse client nhu the nao (kem ma su co)? Khong can policy domain chung, chi memory cua Minh. EPISODE: Voi demo ca nhan `

### E07 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.  Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. Wh`

### E11 - semantic

`EPISODE: Async HTTP Incident Playbook - When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.`

### E08 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.  Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. When discussin`
