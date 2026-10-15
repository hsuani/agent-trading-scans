FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — TLN as of 2026-10-15

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

## 判定框架
TLN 不在 `held_tickers.txt`,屬**新倉**。問題是「該不該進」,答案是:財報前不進。交易員的 AVOID／0% 核心結論核准;MODIFY 的部分是提案內嵌的財報後轉多觸發條件——三方風控一致指出「固定停損 MA200 $351.56」有缺陷(現價僅 2%、追到 $390 卻變 10%),故改為錨定進場價的 ATR 停損,並把首倉由 1/4 常規倉降為 Small。

## Final trade card (條件式,僅在 11-03 財報後觸發條件全部成立時啟用;今日執行倉位 0%)
| Field | Value |
|---|---|
| Direction | LONG(條件式) |
| Entry zone | $374.00 – $380.00(收盤站穩 $373.97 且量能 ≥ 均量,分批) |
| Stop | 進場價 − 1.5×ATR14(以 $377 進場約 $350) |
| Target 1 | $394.63 |
| Target 2 | $414.79 |
| Size | Small(風險預算 0.5% NAV,約正常倉 1/8);10-Q 確認淨負債下降後再升至 Medium |
| Horizon | 觸發評估 2–3 週;論點驗證 2–3 季(至 2027Q1 ASR 完成) |
| Conviction | L |
| R:R to T1 | 0.7(T2 約 1.5) |

說明:T1 的 R:R 僅 0.7,低於門檻,因此即使財報兌現,首倉也只是 Small 試探倉,實際獲利目標以 T2 為準;若財報後跳空直接越過 $390,不追價。

## Risk debate adjudication
- Aggressive's strongest point:10-14 長黑量縮(0.78 倍均量),賣壓不重;分析師目標中位數 $449、PJM 容量缺口 6,623MW 的稀缺敘事未變,完全歸零確實放棄了凸性。若要保留財報前曝險,call spread(定義風險)比裸股合理。
- Conservative's strongest point:Current ratio 0.78、利息覆蓋 0.75x、Q2 FCF −612M 仍回購 198M 是**既成事實**而非待驗證假設;股價反彈 +28% 反映的是「若兌現」的預期,不等於資產負債表已修復。Beta 1.62、D/E 584% 在 FOMC+財報雙事件下提前曝險,是為未驗證假設買單。
- Net:我偏向 **conservative**,理由是這檔的下行不是「估值倍數縮一點」,而是槓桿標的在 10-Q 揭露 ASR 由新債支應時的結構性重估;前一季 EPS 已 miss 30%,再押一次財報前卡位的勝率不足。但採納 neutral 對 conservative 的修正:財報後不應因停損過緊而在正常波動被洗出,故停損用 1.5×ATR 錨定進場價、進場壓在突破區間低端。選擇權方案不採用——權利金 0.3–0.5% NAV 換取的凸性,其結果仍完全取決於同一個未驗證變數,等於換個包裝的方向賭注。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| Adjusted EBITDA 指引兌現 | Q3 年化落在 $2.025B–$2.225B | Cornerstone 首個完整併表季,11-03 才有數據;Q2 調整後 EPS miss −30% | 觀察中 |
| 資產負債表與流動性 | ASR $1.5B 由 PJM 容量收入支應,淨負債不升 | 現金 231M、Current ratio 0.78、利息覆蓋 0.75x;ASR 資金來源待 10-Q | 觀察中(紅旗) |
| PJM 容量稀缺／核能基載 | 2027/28 缺口 6,623MW 支撐定價 | 拍賣結果已公布,結構未變;電價上限提案與 FERC co-location 未定案 | 成立 |
| 技術結構 | 守住 MA200 $351.56,挑戰 $373.97 | 10-14 收 $358.42 守住 MA200,但 MACD histogram 連三日收縮 | 觀察中 |

## 論點失效條件
必須可證偽,且與 Stop 分開(Stop 是價格紀律,這裡是論點紀律)。
- 若 11-03 財報 Q3 Adjusted EBITDA 年化 < $2.025B,或下修 2026 全年指引 → 支柱一失效 → 取消轉多觸發,改列 SHORT 候選。
- 若 Q3 10-Q 顯示淨負債 > $9.34B(即 ASR 由新增舉債支應),或現金 < $231M,或 Q3 FCF 仍為負 → 支柱二失效 → 不建倉;已建倉者出場,不等停損。
- 若 PJM 電價上限提案進入 FERC 正式程序,或 FERC co-location 裁決將核電廠直供資料中心歸為須付全額輸電費的 Non-Firm → 支柱三失效 → 中期論點作廢,出場。
- 若收盤跌破 $351.56 且成交量 > 1.2 倍 20 日均量 → 支柱四失效 → 取消觸發,等待新結構。

## Monitoring trigger
- 10-28 FOMC 若偏鷹(點陣圖上修或聲明刪除降息措辭),財報後首倉規模再折半。
- 財報後 2 個交易日內收盤未站上 $373.97,視為市場不買單指引,觸發作廢。
- 財報當日若跳空 > ±8%,不在當日動作,等第二日量能確認。

## Catalyst calendar
- 2026-10-28 — FOMC 利率決議
- 2026-11-03 — TLN Q3 財報／10-Q(Adjusted EBITDA、淨負債、現金、利息支出、Adjusted 與 GAAP 調節項)
- 持續追蹤 — PJM 電價上限提案、FERC co-location(Firm／Non-Firm)裁決
- 2027Q1 — ASR 完成,股數減少效果入帳

FINAL DECISION COMPLETE
