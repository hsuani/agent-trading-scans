# Sentiment — 5455.TWO as of 2026-11-15

**DATA INTEGRITY WARNING — 代號對應錯誤，本報告未產出情緒分析**

本 session 的 sentiment-analyst 與 news-analyst 兩位獨立分析師均發現：`5455.TWO` 在 yfinance 回傳的公司為 **昇益開發股份有限公司 (Sheng Yi Development Co., Ltd.)**，一家新竹的住宅/建材開發商，與 `pipeline/tools/universe.py` 的 `tw_photonics` 清單中標示的「英特磊 (IntelliEPI)」完全不是同一家公司。

- 英特磊 (IntelliEPI / IET-KY) 的正確代號為 **4971.TWO**，已由多個獨立來源 (nStock、technews、cnyes、TradingView) 確認。
- 既有歷史報告 `daily/2026-07-27/5455.TWO/sentiment.md` 也記錄過同樣的錯誤對應，顯示這是上游 `universe.py` 第 50 行附近的長期性代號錯置，不是本次資料擷取的偶發錯誤。
- 本次 `fundamentals.md` 與 `market.md` 兩份 Phase 1 報告使用的是「5455.TWO 這個代號在 yfinance 真實回傳的資料」（即昇益開發的財務數字、真實的股價走勢），技術面與基本面數字本身是真實有效的市場資料，只是公司身份與 universe.py 的標籤不符。
- `news.md` 則相反：該分析師以為標的是英特磊，用 WebSearch 找到的是 4971.TWO (英特磊) 的新聞內容，貼在 5455.TWO 的新聞報告中——這部分內容描述的公司與本檔真正的股票代號不符，不可採信。

**本報告不對任一公司給出情緒判斷**，理由：
1. 若視為「昇益開發」（真正的 5455.TWO）：sentiment-analyst 已嘗試但因資料稀疏（分析師/機構/內部人欄位皆缺漏）而無法形成有意義的情緒判斷。
2. 若視為「英特磊」（universe.py 原意圖的公司）：沒有針對正確代號 4971.TWO 重跑的 Phase 1 資料，無法代用。

**建議**：
- 上游修正 `pipeline/tools/universe.py` 的 `tw_photonics` 清單，將「英特磊」改列為 `4971.TWO`，或確認 `5455.TWO` 的正確身份後更新清單註解。
- 本次 Sector 5 (sector-comparator / Phase 6) 應將 5455.TWO 標記為 **資料完整性存疑 (DATA_INTEGRITY_COMPROMISED)**，排除在跨券商排名與 Top 20 之外，直到代號對應修正並重新完整跑過 Phase 1。

SENTIMENT REPORT COMPLETE (flagged, no scoring)
