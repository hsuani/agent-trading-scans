# Final decision — 5455.TWO as of 2026-11-08

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
**DATA_INTEGRITY_ISSUE — Phase-1-only stub, 未進入 Phase 2-4。本股不計入 tw_photonics 正常排名。**

## 核心問題
universe.py taxonomy 將 5455.TWO 定義為「英特磊」（矽光子磊晶供應鏈上游，tw_photonics 族群成員）。本次 Phase 1 報告（market、news、sentiment）皆獨立觀察到 yfinance 針對 5455.TWO 回傳的實際公司身分為 **聖億開發股份有限公司（Sheng Yi Development, 新竹市房地產開發商）**，與預期的光通訊業務完全不相關：
- 業務描述為住宅/房地產開發，與矽光子磊晶毫無關聯（industry=Real Estate）。
- yfinance totalRevenue 僅約 0.27 億 TWD，與英特磊（IET-KY）應有規模明顯不符；news agent 查得第三方聚合站的英特磊實際正確 ticker 為 **4971.TWO**，2026 上半年營收 5.88 億 TWD（YoY +15.57%），毛利率 41.81%，與本次 5455.TWO 的 yfinance 數字量級不符。
- 此問題已於 daily/2026-10-03、daily/2026-10-11、daily/2026-11-01 等多次先前掃描中重複出現並記錄於 _catalysts.json（event_key 含「若本次 yfinance 回傳的公司身分 聖億建設」），universe.py 的 ticker 對照表尚未修正。

## 為何不進行 positive-pick 評分
由於公司身分本身未經核實，對本股套用 positive-pick 的五項訊號評分在方法論上無意義——無論評分結果為何，都無法確定評分對象究竟是「英特磊」還是「聖億建設」。因此本報告不進行正式評分，直接標記為 HOLD / 不交易，並建議排除於 tw_photonics 族群排名之外。

## 建議後續行動（已連續 4 次掃描重複提出）
1. 人工核對 5455.TWO 在 TWSE/TPEx 的正確對應標的；英特磊 (IET-KY) 的正確 ticker 應為 **4971.TWO**，建議修正 pipeline/tools/universe.py 的 tw_photonics 清單。
2. 修正後應將 4971.TWO 排入下一輪 tw_photonics 掃描，取代目前錯誤的 5455.TWO 標籤。
3. 本報告不建議本次 session 直接修改 universe.py（屬 pipeline 原始碼變更，超出單次掃描範圍），僅記錄問題供下次維護處理。

## 資料限制聲明
本報告僅使用 2026-11-08 當日工具輸出與同日 WebSearch 結果。所有引用數字均基於 yfinance 實際回傳的 5455.TWO（聖億開發）資料，而非「英特磊」的真實基本面。

FINAL DECISION COMPLETE
