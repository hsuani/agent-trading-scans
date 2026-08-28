# GLD Final Decision — 2026-08-29

FINAL TRANSACTION PROPOSAL: **BUY**

## 決策
**VERDICT: BUY** | **Conviction: 55%** | **Phase: Phase 2-4 Complete**

**Verdict (新倉框架): MODIFY**

GLD 不在 `pipeline/tools/held_tickers.txt` 內，屬新倉判斷：問的是「該不該進」。
答案是進，但不照原案進 — 修改倉位節奏與止損執行機制。

## 綜合評估

原提案的核心缺陷是**雙重等待條件**：既等 Jackson Hole 結果、又等金現貨回測
$4,400–$4,500/oz。Aggressive 正確指出這兩個條件在鴿派情境下互斥 — 若 Warsh 偏鴿，
金價跳空至 $4,800，回測永不出現，結果是零部位錯過整段行情。同時 Conservative 的
0.5% NAV 探針又矯枉過正：結構性支柱（央行 Q2 淨購金 289 噸、DXY 跌破 100）是**已發生
的事實**，不是 Jackson Hole 的函數，用事件不確定性把倉位壓到 0.5% 是把結構性驅動力
錯誤折價。

採 Neutral 的平衡方案：**今日建 1.0% NAV 核心，JH 鴿派確認後加至 1.5% 封頂**。
不追至 Aggressive 主張的 2.5% — MEDIUM 信念（55%）與 T1 R:R 僅 0.7–1.0 不支持該規模。

**Risk debate 裁定**：Aggressive 最強的一點是「等待的機會成本大於追價成本」；
Conservative 最強的一點是「T1 R:R 低於門檻 1.5 是提案自己承認的，以 T2 為唯一入場
理由等於押注完美情境」。**我採 Neutral 權重最重** — 它同時吸收了 Aggressive 的
收盤價確認止損（拒絕在事件日被盤中 noise 洗出）與 Conservative 的 Put 尾端對沖，
兩項調整互補而非互斥。

## 核心論點

### 論點支柱

| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 央行結構性買盤 | 季度淨購金 200+ 噸 | Q2 289 噸創紀錄，但俄、土已轉淨賣出 | 成立（觀察中） |
| 實質利率下行 | Fed 政策轉向、降息折現 | 9 月升息機率 50%→31% | 成立 |
| 美元週期反轉 | DXY 跌破 100 | 已確認技術破位 | 成立 |
| 倉位健康度 | 需消化超買方可續攻 | Call 82.5%、COMEX 淨多 +222K 口、3 週漲 15% | 已失效（反向指標） |

第四根支柱已失效，這正是倉位從 1.5% 降為 1.0% 起步的原因 —
不是不進，是**用規模承認這根柱子倒了**。

## 風險管理

### 論點失效條件（與 Stop 分開；Stop 是價格紀律，此處為論點紀律）

- 若 Warsh 於 8/29–30 演講中**明確排除 9 月降息**，實質利率支柱失效 → **立即出場**，不等 $4,200 技術位
- 若 WGC Q3 數據顯示全球央行**季度淨購金低於 150 噸**，結構性支柱失效 → **減碼至 0.5%**
- 若 8 月 PCE **連續兩個月維持 3.7% 以上**且 9 月 CPI 高於預期，降息折現支柱失效 → **減碼一半**
- 若 **DXY 連續三個交易日收於 102 以上**，美元支柱失效 → **減碼一半**
- 若金現貨**收盤跌破 $4,000/oz**，多頭敘事全面瓦解 → **出場**

### 執行機制

Stop 錨定金現貨 $4,200/oz，**以收盤價確認破位**，拒絕盤中 spike 觸發。
搭配少量 GLD near-month Put（Delta ~−0.20）覆蓋 JH 鷹派跳空尾端，不佔主倉額度。
止損觸發淨損估計：1.0% NAV 時約 0.09% NAV，滿倉 1.5% 時約 0.13% NAV。

## 最終交易記錄
| 項目 | 數值 |
|---|---|
| Ticker | GLD |
| Direction | LONG |
| Entry | PRICE_DATA_UNAVAILABLE — 無即時 GLD ETF 價格，暫不給進出場價位 |
| Stop | PRICE_DATA_UNAVAILABLE — 無即時 GLD ETF 價格，暫不給進出場價位 |
| T1 | PRICE_DATA_UNAVAILABLE — 無即時 GLD ETF 價格，暫不給進出場價位 |
| T2 | PRICE_DATA_UNAVAILABLE — 無即時 GLD ETF 價格，暫不給進出場價位 |
| 倉位規模 | 1.0% NAV（JH 鴿派確認後加至 1.5% 封頂）|
| Conviction | 55% |
| 持倉週期 | 1-3 months |
| Phase | Phase 2-4 Complete |

> **價格免責**：Yahoo Finance 遭封鎖，本系統無法驗證即時 GLD ETF 價格。
> 上述所有 $/oz 水位（$4,200 / $4,800 / $5,000）均為**新聞脈絡中的金現貨參考值**
> （現貨約 $4,600/oz），非 GLD ETF 股價，亦非可直接下單的價位。
> 交易員執行前必須以獨立即時報價系統確認 GLD 股價並自行換算。

## 監控清單

- **2026-08-29/30** — Jackson Hole（Warsh 演講）：本案最大二元風險，鷹派即論點失效
- **2026-09-初** — World Gold Council Q3 央行購金數據：門檻 200 噸／警戒 150 噸
- **2026-09-11** — 8 月 CPI
- **2026-09-16/17** — FOMC 決議
- **持續** — 10 年 TIPS 實質殖利率方向、DXY 每日收盤、GLD 每日資金流、COMEX COT 商業空頭擴張速度

**Monitoring trigger**：若 COMEX 大型投機客淨多倉單週縮減超過 50K 口，或 GLD 出現
連續三日淨流出，在 Stop 觸發前重新評估倉位。

**PORTFOLIO MANAGER COMPLETE**

FINAL DECISION COMPLETE
