FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — SNDK as of 2026-08-31

> **價格聲明**：PRICE_DATA_UNAVAILABLE。以下每一價位均由分析師共識均值目標 **$2,126（UNVERIFIED）** 以百分比推算，全部標注 UNVERIFIED，不構成已驗證市場數據。
> **執行閘門**：下單前必須以券商即時報價確認 SNDK 市價落在核准入場區間內。若即時市價偏離推算錨點超過 ±5%，本決策自動失效，需重新校準後才可執行。

## 1. FINAL VERDICT

**BUY — Conviction 6/10**（新倉，SNDK 不在 held_tickers.txt）

Verdict: **MODIFY**

修改重點：採納 Neutral 的均衡方案。維持原提案的入場區間與寬止損，但把滿倉上限自 1.5% 下修至 1.25% NAV，並駁回 Aggressive 的 2.5% NAV 與 Call spread 疊加。信心自 7/10 下調至 6/10，理由是 ATR UNAVAILABLE 加上 PRICE_DATA_UNAVAILABLE 兩層資料缺口，倉位無法做波動率校準。

## 2. 核准交易

| 欄位 | 內容 |
|---|---|
| Direction | LONG（正股，不用選擇權） |
| Entry zone | ~$1,488 – ~$1,552（錨點 -30% 至 -27%，UNVERIFIED） |
| Stop | ~$1,212（錨點 -43%，入場中值下方約 -20%，UNVERIFIED） |
| Target 1 | ~$2,126（錨點本身，UNVERIFIED） |
| Target 2 | ~$2,445（錨點 +15%，UNVERIFIED） |
| Size | 初倉 0.75% NAV；財報確認後上限 1.25% NAV |
| Horizon | 3m+（核心 2–4 個季度） |
| R:R to T1 | 2.0 |

加碼門檻（唯一）：Q1 FY2027 財報 EPS 超越指引上緣 $46，或管理層上調全年展望。未達成則永久維持 0.75% NAV。
對沖：核准買入 SMH 近月 Put 作板塊層級尾部保護，成本上限 0.15% NAV。

## 3. Risk debate 裁決

- **Aggressive 最強論點**：-10% 止損對年化波動 60–80% 的 NAND 週期股是雜訊等級，強制等財報後進場等於用更高成本買「確定性」。此點成立，故止損維持 -20%、入場不延後。
- **Conservative 最強論點**：ATR UNAVAILABLE 下，1.5%+ NAV 缺乏波動率校準依據；指引低於共識 5.5% 是已公告硬數據，管理層淨賣出 $8.4M 且零買入。此點成立，故滿倉上限下修。
- **Net**：我採 **neutral** 較重。Aggressive 在 stop 與時點上對、在 sizing 上錯（把 7/10 信心直接推導成 Large 倉位）；Conservative 在 sizing 上對、在 stop 與時點上錯。兩者各取其正確半邊，即為 Neutral 方案。Call spread 明確駁回：流動性 UNVERIFIED 時疊加槓桿是拿執行風險換帳面 R:R。

## 4. 論點支柱

| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| NAND 供需缺口 | 需求 +20–22% vs 供給 +15–17% 延續至 2027–28 | 雙方均未質疑此結構 | 成立 |
| 毛利率與盈餘動能 | 高檔維持 | Q4 FY2026 毛利率 84.6% 歷史高、非 GAAP EPS $39.25 超預期 11.7% | 成立 |
| 近期指引 | 順勢向上 | Q1 FY2027 營收指引中值低於共識 5.5% | 觀察中 |
| 內部人與大股東籌碼 | 中性偏正 | 管理層淨賣出 $8.4M、零買入；WDC 持股未知 | 觀察中 |

## 5. 論點失效條件（論點紀律，與 Stop 分開）

- 若 Q1 FY2027 毛利率跌破 75%，或連續兩季非 GAAP 毛利率環比下滑 → 支柱二失效 → **出場**。
- 若 TrendForce NAND 合約 ASP 連續兩個月環比為負 → 支柱一失效 → **減碼至 0.35% NAV**。
- 若 Q1 FY2027 為連續第二季指引低於共識 → 支柱三失效 → **減碼半倉**。
- 若美國鬆綁對中國 NAND 進口限制，或 Samsung/Micron 宣告提前釋放受限產能 → 支柱一失效 → **出場**。
- 若後續 13F 顯示 WDC 減碼超過持股三分之一 → 支柱四失效 → **減碼半倉**。

## Monitoring trigger

市價跌破錨點 -38%（~$1,318 UNVERIFIED）而 stop 尚未觸及時，立即重新評估：若同時伴隨 NAND ASP 月報轉負，不等 stop 直接減碼。

## Catalyst calendar

- 2026 年 10 月（預計）— Q1 FY2027 財報（EPS、NBM 合約量、毛利率指引）
- 每月 — TrendForce NAND 合約 ASP 月報
- H2 2026 — HBF 樣品交付通報（SK Hynix / Kioxia 聯盟）
- 持續 — WDC 13F 申報
- 2027 年初 — HBF 首批 AI 推理裝置上市

## Metrics summary

| Metric | Value |
|---|---|
| Verdict | BUY（MODIFY） |
| Conviction | 6/10 |
| Direction | LONG |
| Size (% NAV) | 0.75%（初倉）／1.25%（上限） |
| Entry | ~$1,488 – ~$1,552（UNVERIFIED） |
| Stop | ~$1,212（UNVERIFIED） |
| T1 | ~$2,126（UNVERIFIED） |
| T2 | ~$2,445（UNVERIFIED） |
| R:R T1 | 2.0 |
| R:R T2 | 3.0 |
| Time horizon | 3m+（2–4 個季度） |

FINAL DECISION COMPLETE
