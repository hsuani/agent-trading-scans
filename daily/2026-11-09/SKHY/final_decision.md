# Final Decision — SKHY Sky Harbour Group (2026-11-09)

**狀態**：Phase-1-only stub（未達 positive-pick 門檻，未進入 Phase 2-4）

## Positive-pick 評分（需 ≥3/5）

| Signal | 結果 | 說明 |
|---|---|---|
| Fundamentals | FAIL | `pipeline/tools/yf SKHY` 回傳的 info 資料為 SK hynix（韓國 DRAM/NAND 廠），非 Sky Harbour Group；`yf SKYH` 則連線失敗無資料。無法確認營收成長或 FCF/NI，資料判定為 DATA_UNAVAILABLE |
| Market (technical) | FAIL | 11/6 收盤 $127.34，低於 MA50 $166.79（-23.7%）與 MA200 $162.10（-21.4%），RSI14 36.38 中性偏弱 |
| News | FAIL | 近 14 天無已確認公司公告；唯一可用基本面（Q2 2026，窗口外）偏多但來自二手聚合站。淨讀數為「mixed，slightly bullish」，非明確偏多 |
| Sentiment | PASS | yf rec_summary：14 buy（含 5 strong buy）/1 hold/0 sell，買方占比約 93%，≥60% 門檻 |
| Valuation | FAIL | 因基本面資料無法確認（ticker 解析失敗），forward P/E 與 EPS catalyst 均無法驗證 |

**總分：1/5** — 未達 positive-pick 標準（≥3/5），停留 Phase-1，不進入 Phase 2-4 辯論與交易建議。

## 摘要

Sky Harbour Group（SKHY）本次掃描的基本面資料取數失敗：`pipeline/tools/yf` 工具對 SKHY 代碼回傳的是 SK hynix（南韓記憶體廠）資料，顯示本沙箱 ticker 解析存在已知的交叉污染問題（本次掃描中 NVDA/AMD、IREN/GOOGL 亦出現類似現象），而嘗試改用 SKYH 代碼則因連線失敗（403）同樣未取得任何資料。技術面（市場與情緒分析師取得的報價似為有效快取資料，價格 $127.34）顯示股價明顯弱於均線，11/5 單日重挫並創 52 週新低後小幅反彈，尚未止穩。分析師覆蓋偏多（14 買/1 持有），但散戶與內部人資料（yf insider 回傳空陣列）同樣無法確認，近 14 天亦無可驗證的公司公告。綜合評分僅 1/5（Sentiment 單項通過），基本面與估值因資料缺口判定為 FAIL，未達 positive-pick 標準。

FINAL TRANSACTION PROPOSAL: **HOLD**（暫不給進出場價位，Phase-1 stub；基本面資料缺口建議下次掃描前先確認正確 ticker 代碼）
