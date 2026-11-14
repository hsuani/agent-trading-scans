FINAL TRANSACTION PROPOSAL: **HOLD**

# 最終決策 — 5455.TWO 截至 2026-11-15

## Verdict
**DATA_INTEGRITY_COMPROMISED — PHASE 1 ONLY, 排除於排名與 positive-pick 評分**

## 代號對應錯誤 (詳見 fundamentals.md / market.md / sentiment.md)

三位獨立的 Phase 1 分析師均發現：`5455.TWO` 在 yfinance 回傳的公司是 **昇益開發股份有限公司 (Sheng Yi Development)**，新竹的住宅/建材開發商，與 `pipeline/tools/universe.py` 的 `tw_photonics` 清單標示的「英特磊 (IntelliEPI)」完全不是同一家公司。

- 英特磊正確代號為 **4971.TWO**，已由多個獨立來源確認。
- 既有歷史報告 `daily/2026-07-27/5455.TWO/sentiment.md` 也記錄過同樣的錯誤對應，顯示這是上游 `universe.py` 長期性代號錯置，非本次資料擷取偶發錯誤。
- `fundamentals.md` 與 `market.md` 使用的是「5455.TWO 這個代號在 yfinance 真實回傳的資料」(昇益開發的真實財務與價格數據)；`news.md` 則誤用了 4971.TWO (英特磊) 的新聞內容，與本檔真正代號不符，不可採信。

## 本決策不評分、不進 Phase 2-4

由於無法確定分析對象究竟是昇益開發還是英特磊，本檔不納入 positive-pick 評分，不產生交易提案。

## 建議（供上游維護者參考）
- 修正 `pipeline/tools/universe.py` 的 `tw_photonics` 清單，將「英特磊」改列為 `4971.TWO`。
- 若 `5455.TWO` (昇益開發) 本身不屬於光通訊/矽光子族群，應自 `tw_photonics` 清單移除。
- 待代號修正後，對正確的英特磊代號 (4971.TWO) 重新執行完整 Phase 1。

## 同 sector tw_photonics 排序
tw_photonics 中 2455.TW、4979.TW、3711.TW、3587.TWO 達 positive-pick 門檻並進入 Phase 2-4；其餘 8 檔 (含本票以外) 為 Phase-1-only stragglers；本票因資料完整性問題單獨排除。
