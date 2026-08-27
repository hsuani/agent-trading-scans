FINAL TRANSACTION PROPOSAL: **HOLD**

# Trade proposal — SH (ProShares Short S&P 500 ETF) as of 2026-07-25

## Direction
AVOID — 不建立 SH 常規倉位

---

## 不進場理由

S&P 500 空頭論點具備足夠歷史依據（Shiller CAPE 42.84 為 155 年第二高；Alphabet/Tesla 財報後分別重跌 7.5%/14%；NVDA 內部人淨賣出 4.106 億美元、零買入；HY OAS 269bp 遠低於 10 年均值 350bp；VIX 升至 18.70），然而 **SH 作為工具本身存在數學上不可避免的結構缺陷**，使其在非急跌情景下為負期望值工具：

- **每日 decay**：VIX≈19 環境下年化損耗 5–8%，加 0.89% 管理費；橫盤四週自動損耗 1–2%
- **損益平衡門檻**：需 S&P 500 在 5–10 個交易日內單向急跌 >6% 方能覆蓋成本
- **逆向風險不可忽視**：AAII 看漲僅 29.6%（歷史統計此後 12 個月 SPX 平均 +15%）；FOMC 升息 80% 已定價，存在「利空出盡」反彈風險；Put/Call 比率偏高顯示防守情緒已部分定價

**無即時價格，暫不給進出場價位。**（Yahoo Finance 遭 proxy 封鎖，PRICE_DATA_UNAVAILABLE）

---

## Setup
```
Entry:    PRICE_DATA_UNAVAILABLE
Stop:     PRICE_DATA_UNAVAILABLE
Target 1: PRICE_DATA_UNAVAILABLE
Target 2: PRICE_DATA_UNAVAILABLE
R:R:      無法計算（無即時價格數據）
```

---

## Sizing
AVOID 為主要建議，**不配置常規倉位**。

若因戰術對沖需求確需持有，上限為 NAV **0.5%（Small）**，且須設定**硬性時間停損**：不論盈虧，2026-08-08 前強制平倉，避免 decay 無聲侵蝕。  
Conviction：L；ATR：PRICE_DATA_UNAVAILABLE；vol：PRICE_DATA_UNAVAILABLE。

---

## Time horizon
若迫不得已持有：**5–10 個交易日**（僅覆蓋 2026-07-28 至 08-05 催化劑窗口）。  
**3 個月以上：絕對避免**——decay 成本完全吞噬非極端下跌情景的對沖效益。

---

## Trigger
**以下三項須同時成立，才考慮極小倉位入場，否則維持 AVOID：**

1. FOMC 7/29 升息 25bp **且** 聲明措辭明確鷹派（非一次性暗示）
2. MSFT 或 AMZN 任一財報盤後跌 5%+（類 Alphabet 式懲罰）
3. VIX 突破 22 **且** S&P 500 連跌三日

**現階段**：等待觀察，不先行建倉。

---

## 替代工具建議（成本效益優於 SH）

| 工具 | 優點 | 適合時間框架 |
|---|---|---|
| SPY Put options（OTM、1–2 個月到期） | 無每日 decay 拖累，最大損失為權利金 | 1–2 個月 |
| SPXS（3× 反向 S&P 500 ETF） | 短線急跌時槓桿放大收益，但 decay 速度更快 | 5–10 個交易日 |
| E-mini S&P 500 Futures（空頭） | 精確對沖、無 decay、成本效益最高 | 彈性 |

---

## Invalidation
下列任一條件出現，確認 AVOID 為正確決策，不再重新評估 SH：

- FOMC 無升息或偏鴿措辭
- MSFT / AMZN 財報優於預期且股價上漲
- VIX 回落至 16 以下
- S&P 500 收復週線高點並站上 50DMA

---

## Catalyst calendar
- **2026-07-28 至 07-29** — FOMC 會議暨利率決定（最高優先監控事件）
- **2026-07-29** — MSFT Q2 財報（盤後）；FOMC 聲明措辭逐字分析
- **2026-07-30** — AMZN、AAPL Q2 財報；PCE 物價指數公布
- **2026-08-05（前後）** — META 及其餘 Mag-7 財報
- **2026-08-26** — NVDA Q2 財報（AI 資本支出敘事最終確認點）

---

TRADE PROPOSAL COMPLETE
