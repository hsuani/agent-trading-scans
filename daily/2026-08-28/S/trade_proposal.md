# Trade proposal — S (SentinelOne) as of 2026-08-28

FINAL TRANSACTION PROPOSAL: **HOLD**

## Direction
AVOID（尚未持倉者，建議觀望；已持倉者，維持半倉以下，不加碼）

---

## 無即時價格，暫不給進出場價位

技術面報告（market.md）顯示所有即時價格、支撐/阻力位、ATR、RSI14、MACD 均標記為 PRICE_DATA_UNAVAILABLE（yfinance HTTP 403 封鎖）。Entry / Stop / Target 1 / Target 2 均無法基於真實數據給出，故本提案不列具體價位。

```
Entry:    PRICE_DATA_UNAVAILABLE
Stop:     PRICE_DATA_UNAVAILABLE
Target 1: PRICE_DATA_UNAVAILABLE
Target 2: PRICE_DATA_UNAVAILABLE
R:R:      PRICE_DATA_UNAVAILABLE
```

---

## Setup（基本面背景，供條件觸發參考）

研究報告中提及財報日股價約 $23.11，分析師共識目標價區間 $19.68–$20.98，低端目標 $17.00。若以此為參考框架，股價已高於共識目標 10–17%，下行空間達 26%（低端），R:R 不利於建立新多頭部位。由於無法從市場數據工具取得即時價格與關鍵技術位，無法建構技術面 Entry / Stop 方案，亦無法計算實際 R:R 是否達標（Long ≥ 1.5、Short ≥ 2.0）。

---

## Sizing
不建倉。

**理由：**
- 研究管理人判斷為 NEUTRAL，conviction MEDIUM。
- 股價（約 $23.11，源自投資計畫敘述）已超越德銀、Citi、Piper Sandler 共識目標，上行空間受限。
- 技術面數據全部 PRICE_DATA_UNAVAILABLE，無法依 ATR 計算合理倉位大小。
- 依規則：NEUTRAL + 無技術位 → 不開新倉。

---

## Time horizon
3–6 個月（以 2026年9月 Q3 FY2026 財報作為關鍵驗證節點）。

---

## Trigger（何時重新評估）

**轉 LONG 條件（需同時滿足）：**
1. Q3 FY2026 實際營收明顯超越指引 $2.56億美元，且管理層上修全年展望。
2. 財報首次披露 Purple AI / Singularity Credits 可量化 ARPU 貢獻（如每客戶 AI Credits 消費數據）。
3. 股價回落至分析師共識目標區間（$19.68–$20.98）以內，且技術面形成支撐確認（需屆時市場數據恢復可用）。
4. 淨新增 ARR 再度加速，NRR 維持 120%+。

**轉 SHORT / 加深 AVOID 條件：**
1. Q3 實際營收低於或接近 $2.56億美元指引（未超越）。
2. NRR 下修至 115% 以下。
3. Purple AI 貨幣化數據缺席或令市場失望。
4. 更多機構跟進降評，目標價向 $17 集中。

---

## Invalidation（論點失效條件）

- **多頭論點失效**：Q3 FY2026 季度環比萎縮被確認為需求真實轉弱（非保守指引），NRR 出現明顯下修，AI 差異化優勢被 CrowdStrike / Microsoft / Palo Alto 技術追平。
- **空頭論點失效**：Q3 大幅超越指引同時披露 AI 量化指標，帶動機構共識目標價集體上修至 $25+ 且股價獲成交量確認突破。

---

## Catalyst calendar

| 日期 | 事件 |
|------|------|
| 2026年9月（預計） | Q3 FY2026 財報：核心指標——實際營收 vs $2.56億美元指引、淨新增 ARR 趨勢、Purple AI / Singularity Credits 首次量化披露 |
| 2026年12月（預計） | Q4 FY2026 財報：驗證全年 Non-GAAP 營運利率 +3% 指引與盈利路徑能見度 |
| 持續監測 | CrowdStrike / Microsoft / Palo Alto Agentic SOC 功能發布進度，影響 Purple AI 差異化窗口評估 |

---

**總結**：SentinelOne 長期結構故事（ARR $10億美元突破、NRR 120-130%、政府管道）具真實基礎，但當前股價已超越共識目標、Q3 季度環比萎縮指引提供量化逆風、技術面數據完全不可用，三重因素共同指向「觀望」為最佳策略。待 2026年9月 Q3 財報釐清方向後，再依實際數據重新評估進場條件。

TRADE PROPOSAL COMPLETE
