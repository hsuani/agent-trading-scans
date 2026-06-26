# Final decision — AMT as of 2026-06-27

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY（採 neutral 綜合方案；新資金不建股票倉，僅以選擇權結構參與）

## Final trade card (if not REJECT)
| Field | Value |
|---|---|
| Direction | LONG（透過 bull call spread，定義性風險）|
| Entry zone | 條件式：選擇權今日可建；股票倉等 $162–$165 回落或 2026-07-28 確認後 |
| Stop | $155（股票倉論題失效位；選擇權倉以期權費為最大損失）|
| Target 1 | $195 |
| Target 2 | $227 |
| Size | Small — 選擇權 0.25% NAV（現在）；確認後股票倉擴至 0.5% NAV（核心），上限 1.0% |
| Horizon | 3 個月+（季度級別），2026-07-28 為第一決策節點 |
| Conviction | 55% |
| R:R to T1 | 3.0（股票倉以中點 $165、止損 $155 計）|

具體結構：bull call spread $170/$195，到期 2026-09-18（涵蓋 Q2 業績與 FOMC），最大損失鎖定於期權費（估 $4–$6/spread）。現有持倉者維持半倉，並以 VNQ put spread（到期 2026-08-15）對沖事件窗口利率上行。

## Risk debate adjudication
- Aggressive 最強論點：現價 $168.72 已在進場區間上緣，T2 R:R 達 4.5x 的非對稱結構配 0.5% NAV 過於吝嗇；等待有真實機會成本。
- Conservative 最強論點：技術面數據缺失使止損可靠性近零，CFO 淨賣出 $5.0M 為內部資訊不對稱，跳空情境下 $155 止損形同虛設（情境 B/C 指向 $132–$150）。
- Net：我較傾向 neutral。Aggressive 正確指出非對稱性，但混淆「接近進場區間」與「條件成立」，且裸股票倉無法迴避跳空尾部風險；Conservative 正確點出尾部風險，但「完全 AVOID」放棄了 bull call spread 這個能同時捕捉上行又封頂下行的工具。選擇權結構正是兩派的最大公約數：以定義性期權費參與 AFFO 復甦與 Fed 轉鴿的 optionality，徹底規避 gap-down 風險。

## Monitoring trigger
若 2026-07-28 FOMC 點陣圖 2026 年支持升息委員增至 12 位以上，或同日 Q2 AFFO/股年增低於 3% 且 CoreSite 成長回落至 10% 以下，立即放棄股票倉建倉計劃並讓選擇權倉自然到期，不等 $155 止損。反向若 AFFO/股加速至 4%+ 且 FOMC 刪除升息措辭，將股票倉擴至 1.0% NAV。

## Catalyst calendar
- 2026-07-28 — AMT Q2 2026 業績（AFFO/股成長率、CoreSite 利用率、美國 TTB 有機增長）
- 2026-07-28/29 — FOMC 決議（升息/維持/鴿派訊號為分水嶺）
- 2026-08-15 — VNQ put spread 對沖到期
- 2026-09-18 — bull call spread $170/$195 到期
- 持續監測 — AT&T/Verizon/T-Mobile 資本支出、US 10Y 殖利率

FINAL DECISION COMPLETE
