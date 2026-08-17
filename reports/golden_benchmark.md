# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1414.7 ms**
- Average token reduction vs full source context: **13.1%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G06 | long_term | PASS | 3448.0 | 794 | 0.0% |  |
| G09 | semantic | PASS | 263.5 | 168 | 63.4% |  |
| G10 | semantic | PASS | 306.7 | 108 | 76.5% |  |
| G14 | mixed | PASS | 2262.2 | 444 | 0.0% |  |
| G03 | long_term | PASS | 1444.4 | 1550 | 0.0% |  |
| G04 | long_term | PASS | 1587.6 | 1567 | 0.0% |  |
| G07 | episodic | PASS | 296.7 | 334 | 0.0% |  |
| G08 | episodic | PASS | 274.3 | 301 | 0.0% |  |
| G11 | mixed | PASS | 1952.5 | 453 | 19.8% |  |
| G13 | mixed | PASS | 586.3 | 427 | 24.4% |  |
| G15 | mixed | PASS | 2441.2 | 758 | 0.0% |  |
| G16 | mixed | PASS | 2577.4 | 504 | 10.8% |  |
| G17 | mixed | PASS | 2392.9 | 504 | 10.8% |  |
| G18 | mixed | PASS | 705.3 | 424 | 25.0% |  |
| G19 | mixed | PASS | 2300.3 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1858.4 | 1567 | 0.0% |  |
| G12 | mixed | PASS | 1759.4 | 444 | 29.8% |  |
| G20 | mixed | PASS | 1835.9 | 623 | 1.4% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`<USER_SUMMARY> Lan's project is LOTUS-88, prioritizing Java and Spring Boot for backend examples.  Lan prefers Java and Spring Boot, and does not use Python for backend development. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java +`

### G09 - semantic

`EPISODE: Payment API Retry Policy - For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. EPISODE: Agent Memory Privacy Rule - Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Memory Context Budget - Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.`

### G10 - semantic

`EPISODE: Agent Memory Privacy Rule - Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Memory Context Budget - Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.`

### G14 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan's project is LOTUS-88, prioritizing Java and Spring Boot for backend examples.  Lan prefers Java and Spring Boot, and does not use Python for backend development. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTU`

### G03 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.  Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. When discussin`

### G04 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.  Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. When discussin`

### G07 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORCHID-27. EPISODE: Trong thread nay minh vua nhac constraint gio standup. Lat nua minh se them retry payment vao dung backend du an cong ty. Ghep ba manh: constraint standup con hieu luc trong thread, stack bat buoc `

### G08 - episodic

`EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Trong thread nay minh vua nhac constraint gio standup. Lat nua minh se them retry payment vao dung backend du an cong ty. Ghep ba manh: constraint standup con hieu luc trong thread, stack bat buoc cua backend cong ty, va cach danh dau request payment de khong trung don. EPISODE: Hay chon huong dan code retry payment phu hop voi preference ca nhan cua`

### G11 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.  Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. Wh`

### G13 - mixed

`<EPISODIC> EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. EPISODE: Trong thread nay minh vua nhac constraint gio standup. Lat nua minh se them retry payment vao dung backend du an cong ty. Ghep ba manh: constraint standup con hieu luc trong thread, stack bat buoc cua backend cong ty, va cach danh dau request payment de khong trung don. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay chon huong dan code retry payment phu hop voi `

### G15 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.  Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. Wh`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.  Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. Wh`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.  Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. Wh`

### G18 - mixed

`<EPISODIC> EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Trong thread nay minh vua nhac constraint gio standup. Lat nua minh se them retry payment vao dung backend du an cong ty. Ghep ba manh: constraint standup con hieu luc trong thread, stack bat buoc cua backend cong ty, va cach danh dau request payment de khong trung don. EPISODE: Minh sap viet script ca nhan de tai hien su co latency, muon code dung ngon ngu minh thich khi lam mot minh, dong thoi bam sat playbook incident cua lab chu dung vo tang timeout. Ghep hai manh: stack ca nhan cua Minh, va buoc b`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.  Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. Wh`

### G05 - long_term

`<USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.  Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. When discussin`

### G12 - mixed

`<LONG_TERM> <USER_SUMMARY> The user's personal project is named ORCHID-27, for which they prefer Python. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS, and Python is not to be used for this project. The user is studying async/await and coroutines vs Tasks. They have a deadline to complete a benchmark report before Thursday at 16:00, related to open loop LAB-REPORT-1600. The user is currently debugging async HTTP, investigating connection pool, client lifecycle, and concurrency, specifically identifying connection churn as the root cause for the ASYNC-FIX-20 incident.  Minh Nguyen prefers Python and dislikes Java. When explaining code, use short examples. Wh`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`
