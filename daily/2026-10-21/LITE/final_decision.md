FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — LITE as of 2026-10-21

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
REJECT

## 持倉判定
LITE 不在 `pipeline/tools/held_tickers.txt`，屬新倉評估，採 A 框架：問題是「該不該進」。結論是現在不進。交易員的 AVOID 方向正確，但 REJECT 的對象是「在 11-05 財報前建立任何方向性現股部位」，包括 aggressive 建議的半倉與 investment_plan 留的「回測止跌升至半倉」後門。

## Final trade card
不適用（REJECT，0% NAV）。

## Dealbreaker
不是基本面，而是時點與結構。中長期論點（營收連 4 季 QoQ >11%、營業利益率 28.0%、淨現金 $10.67 億）我接受，但：
1. 獲利基準未定：forward EPS 36.02 與 21.79 差距 65%，對應 P/E 23.2x 與 38.3x。多方最強的估值論據（PEG 0.63）建立在尚未驗證的數字上，兩週後財報才會揭曉。
2. 價格結構仍在下行：反彈高點連續下移、MACD 柱狀體擴大至 -30.63、跌日放量反彈縮量。現價 $834.51 距支撐 $776 僅 7%，距壓力 $897 也僅 7.5%，進場無邊際。
3. 波動使停損失效：ATR14 占股價 8.3%，財報跳空可直接穿透 $776；aggressive 計算的 2.38:1 R:R 假設停損能在 $776 成交，這個假設在二元事件下不成立。Conservative 算出的 Scenario A 損失（跳空至 $594.84）是 $776 停損損失的 4 倍，這才是真實的尾部曝險。

## Risk debate adjudication
- Aggressive's strongest point: 23/24 季 EPS 超預期是可量化的統計優勢，財報前完全空手等於放棄它；若要卡位，call spread（$850/$950，2026-11-20 到期）把下方鎖在權利金內是合理結構。
- Conservative's strongest point: 現有技術停損在財報跳空情境下不可靠，位置風險應以 $594.84 情境而非 $776 情境計算。
- Net: I weight **neutral** more here because 它正確指出雙方各自的過度之處——aggressive 把機率優勢當成確定性，與 research manager 的 NEUTRAL/MEDIUM 定調矛盾；conservative 上移停損至 $784.47 反而更易被雜訊洗出，且 COHR 同因子疊加缺乏證據（但提醒合理：本組合確實持有 COHR，AI 光通訊因子已有曝險，這是不加 LITE 的額外理由）。Neutral 的折衷（不開現股倉、若要上行曝險只用小額 call spread）與我的結論一致，但 call spread 屬選擇權策略，不在本決策的現股交易卡範圍，留給交易員自行裁量。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 營收動能 | 連續 QoQ 雙位數成長 | 連 4 季 QoQ >11%，YoY +109.3% | 成立 |
| 毛利率為結構性定價權 | non-GAAP 毛利率守 50% 以上 | 33.3% → 47.4%，但 COHR CW 雷射擴產威脅 2027 後供給 | 觀察中 |
| FY2027 獲利基準 | forward EPS 向 36.02 靠攏 | Q1 指引年化約 $17，與 36 差距大 | 觀察中 |
| $776–784 支撐帶 | 守住並收復 MA50 | 現價距支撐 7%，MACD 空方動能仍擴大 | 觀察中 |

四根支柱只有一根成立，三根待驗，不足以支撐新倉。

## 論點失效條件
- 若 11-05 財報 non-GAAP 毛利率環比下滑（低於 47.4%），毛利率支柱失效 → 轉為 SHORT_OR_AVOID 追蹤，下方目標 $594.84。
- 若 Q2 營收指引中值低於 $12.75 億或低於共識，獲利基準支柱失效 → 不再考慮多頭建倉，直到連兩季指引回升。
- 若收盤跌破 $776.01 且成交量高於 20 日均量，支撐支柱失效 → 多頭論點暫停，重新等待 $594.84 附近的結構。

## 重啟評估條件（future revisit）
任一出現即重新走流程評估 LONG：
- 11-05 財報營收 ≥ $12.75 億、non-GAAP 毛利率 ≥ 50%、Q2 指引上修且無新 GAAP 特殊項目；或
- 價格守住 $776–784 後收盤站回 $897 並收復 MA50 $930.54。
屆時建倉以 Small（常規成長股部位的一半以下）起步，停損採結構停損而非 2 ATR。

## Monitoring trigger
If 財報前股價收盤跌破 $784.47 且放量，或盤前跌破 $800 時，重新檢視是否轉為空方追蹤，不等財報。

## Catalyst calendar
- 2026-11-05 — LITE FY2027 Q1 財報（毛利率、Q2 指引、GAAP 特殊項目）
- 2026-11-20 — aggressive 提議之 call spread 到期日（若交易員採用）
- 待觀察 — OCS 積壓訂單更新（上次數字 2026-02，已過時）
- 待觀察 — COHR 德州 CW 雷射產能爬坡進度

FINAL DECISION COMPLETE
