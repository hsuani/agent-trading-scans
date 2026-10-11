# 5455.TWO — Phase-1-Only 最終決策 — 2026-10-11

## 評級：HOLD (Phase-1-only stub) — DATA_INTEGRITY_ERROR

**未進入 Phase 2-4 全流程原因**：代號資料完整性錯誤，非 Phase 1 評分不足。

## 關鍵發現

四份 Phase-1 報告（fundamentals、market、news、sentiment）**獨立一致**確認：yfinance 對代號 **5455.TWO** 的 cache 資料實際對應「昇益開發股份有限公司」（Sheng Yi Development Co., Ltd，新竹房地產開發商，統編 86233176），**並非**本次任務意圖分析的「英特磊」（IntelliEPI / IET-KY，InP/GaAs 磊晶廠）。

- 英特磊的正確上櫃代號為 **4971.TWO**（IET-KY），本地快取目前無此代號資料。
- 本次 fundamentals.md / market.md / sentiment.md 中的財務與技術數據皆為「昇益開發」（房地產業，非光通訊）的真實資料，不可用於評估英特磊的投資價值。
- news.md 另行以 WebSearch 取得英特磊（4971）本身的新聞背景，但未搭配同代號之正確財務與技術資料，不足以支撐完整投資判斷。

## 建議

1. **taxonomy 修正**：`pipeline/tools/universe.py` 中 `tw_photonics` 的 "英特磊 5455.TWO" 映射需更正為 **4971.TWO**，並重新抓取/快取其財務與價格資料後重跑完整 Phase 1-6。
2. 本次 5455.TWO（昇益開發）身為房地產開發商，不屬於光通訊/矽光子族群，不應繼續留在 `tw_photonics` 清單中計分或進入 Phase 2-4。

## 結論

因代號對應錯誤，本輪無法對英特磊做出任何有效的技術面、基本面或情緒面判斷，亦不對昇益開發（房地產業，與本板塊無關）做方向性建議。

**判決：HOLD（資料完整性錯誤，暫不給出交易判斷）** | **信心：N/A** | **階段：Phase-1-only / DATA_INTEGRITY_ERROR**
