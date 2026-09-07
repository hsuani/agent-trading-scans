FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — VST as of 2026-09-08

## 決策結果
**BUY**（新倉；VST 不在 held_tickers.txt）

## Verdict
MODIFY

## 信心度
**55% conviction（MEDIUM）**

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $148.00 – $154.00（限價，不追市價） |
| Stop | $135.00（收盤價確認跌破） |
| Target 1 | $185.00 |
| Target 2 | $220.00 |
| Size | Medium — 1.5% NAV（第一批 0.7%，第二批 0.8% 條件式） |
| Horizon | 3–6 個月 |
| Conviction | M（55%） |
| R:R to T1 | 2.1（進場中位 $151） |

補充：R:R to T2 = 4.3。止損觸發損失 ≈ 0.16% NAV；FERC 跳空至 $120 情境約 0.31% NAV。可選配 VST $135 put（3 個月），成本上限 0.1% NAV，僅對沖 FERC 裁決跳空，不做 Call Spread。

## R:R ratio
- T1：(185 − 151) / (151 − 135) = **2.1x**
- T2：(220 − 151) / (151 − 135) = **4.3x**

## Risk debate adjudication
- Aggressive 最強論點：以最大可量化損失衡量，本部位下行僅 0.2–0.4% NAV，而 T2 上行 +0.66% NAV，倉位過小確實在浪費不對稱優勢；催化劑在 60 天內三箭齊發。
- Conservative 最強論點：進場區間上緣 $158 會使 R:R to T1 掉到 1.17x，低於 1.5x 門檻——這是算術問題，不是風格問題，必須修正。
- Net：我採 **neutral** 為主。理由是尾部風險（FERC 跳空至 $110–120）不由止損寬度決定，而由倉位大小決定，故 Aggressive 的 2.5% NAV + $128 止損是錯配；但 Conservative 的 $140 止損在 45–55% 年化波動率下僅約 1.2 個週標準差，等同保證被雜訊掃出。維持 1.5% NAV / $135 止損，並把提案的進場上緣由 $158 壓到 $154——這是我對原提案唯一的實質修改，也是 MODIFY 的原因。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| AI 電力需求與長約鎖定 | AWS 20 年核能 PPA + 新簽 AI 合約持續放量 | 合約在手，Q3 新簽量待驗證 | 成立 |
| FCF 與 EBITDA 動能 | 2026E FCF $4.3B、EBITDA YoY >25% | Q2 2026 EBITDA YoY 30%+ | 成立 |
| 估值未達極端 | EV/EBITDA <11x | 當前約 9.7x（vs CEG 約 11.5x） | 成立 |
| 內部人與情緒信號 | 管理層淨買進 | CEO 於 ~$152 拋售 $133.8M，無買進抵消；95% 買進評級擁擠 | 已失效 |

第四根已失效，故不給 Large size、不追高、不以市價執行——這正是倉位封頂在 1.5% 的直接原因。

## 論點失效條件
與 Stop 分開；論點先壞則不等價格打到 $135。
- 若 FERC 裁定成本轉嫁違規、要求退款或限制 AI 合約溢價，年化現金流影響 >$200M → **出場**
- 若 Q3 2026 調整後 EBITDA YoY <15%，或全年 FCF 指引下修至 <$3.8B → **減碼至 0.7% NAV**
- 若 Cogentrix 交割延至 2027 年，或整合費用超支 >$300M → **減碼一半**
- 若任一大型科技客戶公開取消或縮減既有 PPA → **出場**
- 若 ERCOT 現貨月均價連續兩個月 <$70/MWh（基準 $87） → **減碼**

## 關鍵催化劑
- 2026-10 前 — Cogentrix 5,500 MW 天然氣資產交割
- 2026-10/11 — Q3 2026 財報：EBITDA、AI 合約新簽量、全年指引
- 2026-09 底 — FERC PJM 互聯規則改革修訂案提交
- 2026-09 中下旬 — Helix Digital Infrastructure JV 首批投資進展
- 待定 — FERC 成本轉嫁調查裁決（雙向、最高權重）

## 風險因子
- FERC 不利裁決跳空（~20% 機率，$200–400M，止損無法保護）
- CEO $133.8M 高位拋售，內部人信號偏空
- ERCOT 電價由 $87 跌至 $65/MWh，EBITDA 損失 $500–700M
- Cogentrix + Helix 推升 2026–27 CapEx，壓縮 FCF
- PRICE_DATA_UNAVAILABLE：止損位缺乏 ATR／支撐驗證
- 淨債 $29.6B，利率上行放大股權跌幅

## Phase 1 評分表（3 / 5）
| Signal | 判定 |
|---|---|
| 結構性需求動能（AI 電力缺口） | ✅ |
| 估值（EV/EBITDA 9.7x vs EBITDA +30%） | ✅ |
| 現金流品質（FCF $4.3B、FCF/NI 135%） | ✅ |
| 內部人／情緒（CEO 拋售、95% 買進擁擠） | ❌ |
| 技術面確認（RSI/MACD/ATR 不可得） | ❌ |

## 執行建議
1. 開盤前先核對即時報價與日線圖；若實際價已 >$154，**不追**，改掛 $148–$154 GTC 限價等回落。
2. 第一批 **0.7% NAV**，於 $148–$154 分兩張限價單掛出（$153 與 $149），成交即設 $135 停損（收盤確認制，非盤中觸價）。
3. 第二批 **0.8% NAV** 僅在下列任一成就後投入：Cogentrix 正式交割無超支公告、或 Q3 EBITDA YoY >25% 且 AI 新簽 >150 MW。不因價格上漲而提前補倉。
4. 取得即時技術數據後 24 小時內複核 $135 是否仍為結構性水位；若 ATR 顯示該位僅 1 個週標準差，改以 $132 並同步縮減第一批至 0.5% NAV。
5. 若 FERC 裁決日程公布落在持倉窗口內，於裁決前一週買入 $135 put 對沖（成本上限 0.1% NAV）。

## Monitoring trigger
若股價收盤跌破 $140，或 FERC 排定聽證／裁決日期公告，於止損被觸及前先行重評並暫停第二批。

FINAL DECISION COMPLETE

FINAL TRANSACTION PROPOSAL COMPLETE
