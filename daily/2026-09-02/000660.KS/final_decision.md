FINAL TRANSACTION PROPOSAL: **BUY**

# FINAL DECISION — 000660.KS (SK하이닉스) 2026-09-02

> PRICE_DATA_UNAVAILABLE — 無可靠即時報價，本決策不設價格型 entry/stop/target，一律以 % NAV 與事件觸發條件表達。

## 裁決

**VERDICT:** BUY
**CONVICTION:** 45%
**POSITION SIZE:** 0.35% NAV（第 1 批 0.20% 立即；第 2 批 0.15% 條件式）
**PHASE:** Phase 4 Complete
**新倉判定（不在 held_tickers.txt）：** MODIFY — 批准做多，但下修規模並為第 2 批加上資料閘門

| 欄位 | 內容 |
|---|---|
| Direction | LONG（現貨正股，KRX） |
| Entry | 事件式：第 1 批立即 0.20% NAV；第 2 批 2026-09-16 前，須 TrendForce 9 月 DRAM/HBM 合約均價環比持平或上升 |
| Stop | 事件觸發（見下），無價格 stop |
| Size | Small — 0.35% NAV 上限（財報前不得超過） |
| Horizon | 1–2 個月，錨定 2026-10-27 Q3 財報 |
| Hedge | KRW/USD 遠期對沖約 30% 倉位敞口；不做 SOXX put（倉位過小，對沖成本不對稱） |

## 風險辯論摘要

- **Aggressive 最強論點：** UBS/TrendForce 2026-08 報告確認的 Vera Rubin HBM4 訂單 60–70% 集中度屬有日期、有機構背書的硬數據，而非預測；Samsung 從「良率 80%」到「系統整合量產」仍有 12–18 個月工程落差，這段護城河視窗是真的。
- **Conservative 最強論點：** 創歷史紀錄的 Q2 財報後單日 -9.6%，配上 37 買 / 1 持 / 0 賣的賣方共識，代表邊際買盤已耗竭；此結構下任何利空都會遇到流動性真空式的非線性跌幅。FX 風險亦被原提案完全忽略。
- **Net：** 我採 **neutral** 權重。Aggressive 把 0.85% NAV 建立在「訂單能見度」上，但訂單能見度解決的是 thesis 品質，解決不了時機問題——而三項 crux 全部是時機問題。Conservative 的 0.2% 凍結則低估了硬數據品質，且「Samsung 良率 85% 即減半倉」對一個已被市場折現的指標反應過度。0.35% NAV 分兩批、第 2 批掛 ASP 閘門，是唯一同時尊重兩邊有效論證的結構。

## 論點支柱

| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| HBM4 訂單集中度 | Vera Rubin 平台 SK Hynix 佔 60–70% | UBS/TrendForce 2026-08 確認 | 成立 |
| DRAM/HBM 供給短缺延續 | 供給僅覆蓋需求約 2/3，延伸至 2027 | 韓國出口均價數據支持，ASP 尚未拐頭 | 成立 |
| 估值安全墊 | 6× FY2026 Forward P/E（EPS 共識 KRW 281,074） | 仍成立，但盈利本身處周期高位，P/E 分母有下修風險 | 觀察中 |
| 資本配置一致性 | KRW 40兆 capex + KRW 40兆 buyback 並行可兌現 | 多頭方未提出令人信服的數學解釋 | 觀察中 |

## 進出場條件（event-based）與論點失效條件

論點紀律，與價格無關；任一成立即依指定動作執行，不等價格。

- 若 TrendForce 月報顯示 DRAM 或 HBM4 合約均價出現環比下滑 → 供給短缺支柱失效，**出場（清零）**
- 若 Samsung 於 Vera Rubin Ultra 確認取得逾 35% HBM4 訂單配比 → 訂單集中度支柱失效，**出場**
- 若 NVIDIA 公告 2027 年 AI 加速器採購縮減或延後 → 需求支柱失效，**出場**
- 若 KRW 40兆回購宣布縮水、暫停或至 11-19 明顯落後進度 → 資本配置支柱失效，**減碼至 0.15% NAV**
- 若 Q3 財報（10-27）HBM4 比特出貨 QoQ 停滯或 ASP 下滑 → 核心驗證失敗，**出場**
- 若工會罷工導致生產中斷逾 2 週 → **減碼一半**

**加碼條件：** 僅 2026-10-27 Q3 財報確認 HBM4 出貨 QoQ 加速且全年指引上調至 Nomura KRW 99兆營業利潤之上，方可加至 0.75–1.0% NAV。

## Monitoring trigger

Samsung HBM4 良率突破 85% → 不觸發減倉，但**立即凍結第 2 批**並重新評估護城河視窗年限。

## 關鍵催化劑

- 2026-09（月內）— TrendForce 9 月 DRAM/HBM 合約均價月報（第 2 批閘門）
- 2026-09（月內）— Micron 台灣廠工會罷工投票結果
- 2026-10-27 — **SK Hynix Q3 2026 財報**（本論點唯一可信加碼觸發點）
- 2026-11-19 — KRW 40兆回購截止日，執行進度驗證
- 2026-H2 — ADR 上市時程公告
- 2027-H1 — Rubin Ultra 訂單最終配比官方確認

## 風險因子

周期頂部時機不明（2026 Q4–2027 H1）；97% BUY 共識為反向指標；KRW/USD 貶值疊加股價下跌的雙重損失（已用 30% 遠期部分覆蓋）；美國 HBM 對中出口管制擴大的非線性尾部。最壞情況損失約 0.35% NAV。

FINAL DECISION COMPLETE
