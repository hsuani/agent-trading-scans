FINAL TRANSACTION PROPOSAL: **HOLD**

# IONQ — 最終決策 2026-09-08

## 決策結果

**HOLD**（新倉判定 → REJECT 進場，不建立部位；IONQ 不在 held_tickers.txt，此為「今日不進場、留待觀察」而非賣出）

理由簡述：三項前置條件同時缺席——(1) PRICE_DATA_UNAVAILABLE 使停損無法定義，(2) fundamentals.md 與 news/sentiment 資料互相矛盾至無法採信，(3) 交易提案自身的條件性觸發（投資者日具體財務揭露）尚未被任何輸入證實。在 Beta 1.8–2.2、P/S 46.51x、年化 EBITDA 虧損逾 $480M 的標的上，無停損等同開放式下行暴露。

## 信心度

**30% conviction**（多方論述本身）／對「今日不進場」此一決策的信心度 **75%**

## 進出場價位

PRICE_DATA_UNAVAILABLE

| Field | Value |
|---|---|
| Direction | LONG（暫緩） |
| Entry zone | PRICE_DATA_UNAVAILABLE |
| Stop | PRICE_DATA_UNAVAILABLE |
| Target 1 | PRICE_DATA_UNAVAILABLE |
| Target 2 | PRICE_DATA_UNAVAILABLE |
| Size | 0%（不建倉）；條件全數滿足後上限 0.5% NAV |
| Horizon | 3–12 個月 |
| Conviction | L |
| R:R | PRICE_DATA_UNAVAILABLE |

## 理由摘要

我採納保守方的核心主張。積極方要求在投資者日前先建 50% 倉並疊加 call spread，等於在自己承認無法計算停損的環境下加槓桿——這不是承擔風險，是放棄風險量化。中性方維持 0.5% NAV 的判斷本身合理，但它預設觸發條件已可驗證；今日輸入中沒有任何一份文件證實投資者日已公佈量化 2027–2028 收入目標或單獨揭露有機量子服務收入，觸發條件仍是空的。

另有一項風險委員會未指出的問題：fundamentals.md 記載市值 $250–280M、P/S 1.5–1.8x、LTM 收入 $145–155M，而 news.md 記載單季 Q2 收入即 $80.1M、SkyWater 對價 $18 億、sentiment.md 記載 P/S 46.51x。兩者相差一個數量級。當估值錨點本身不可信，任何倉位規模的推導都是虛假精確。這是本次不進場的首要理由，優先於價格資料缺失。

## 論點支柱

| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 收入動能與合約能見度 | RPO $4.7B、FY 指引 $280–290M | Q2 +287% YoY 但有機 vs SkyWater 合併貢獻未拆分 | 觀察中 |
| 垂直整合護城河 | SkyWater 整合建立全鏈控制 | 7/31 完成，$741.3M 現金流出 + 24.1M 股稀釋，整合成效未驗證 | 觀察中 |
| 技術領先 | 雙量子位閘忠實度 99.99%、NVIDIA 邏輯錯誤率 -54% | 有外部佐證，成立 | 成立 |
| 估值可辯護性 | 成長支撐高倍數 | P/S 46.51x 與內部資料 1.5x 相互矛盾，錨點失效 | 已失效 |

## 論點失效條件

- 若投資者日結束後未公佈可量化的 2027–2028 收入目標與毛利率路線圖，「收入能見度」支柱失效 → 維持不進場至 Q3 財報。
- 若 Q3 財報（2026-11）未單獨揭露排除 SkyWater 的有機量子服務收入，或該數字環比零成長／下滑，「收入動能」支柱失效 → 永久放棄本論述。
- 若 2027 上半年前出現價格低於前輪的稀釋性融資（暗示 SkyWater Capex 超支），「垂直整合」支柱失效 → 出場。
- 若 Quantinuum 或 Google 宣佈可驗證的商用容錯量子計算，「技術領先」支柱失效 → 出場。

## 風險因素

散戶情緒 Stocktwits 88/100 已極度擁擠，Short Interest 自 22.4% 腰斬至 10.7%，逼空燃料與買盤緩衝雙雙耗盡；投資者日若不及預期，跌幅會超比例。內部人於 $34–35 賣出、股價低至 $32 時無人買入。日均成交 $0.5M–$2M，滑點風險實質。

## Monitoring trigger

取得實時報價後立即重跑技術面並重建 fundamentals.md（以 8-K 原始數據為準）；同時確認投資者日揭露內容。三者齊備且觸發條件成立，才以 0.3% NAV 初始建倉、-20% 硬停損、上限 0.5% NAV。

## Catalyst calendar

- 2026-09-08 — 投資者日（NYSE）
- 2026-09-23~25 — Quantum World Congress 2026
- 2026-09-29 — IONQ WS 認股權證停止交易
- 2026-11 — Q3 2026 財報
- 2027-Q1 — 256 量子位系統交付目標

FINAL DECISION COMPLETE
