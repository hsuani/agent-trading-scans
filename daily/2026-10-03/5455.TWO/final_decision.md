FINAL TRANSACTION PROPOSAL: **HOLD**

# 5455.TWO — Final Decision (Phase 1 Only)
**日期**: 2026-10-03 | **分析師**: TradingAgents Pipeline | **階段**: Phase 1 Stub（資料完整性排除）

---

## 決策摘要

| 項目 | 內容 |
|------|------|
| **Verdict** | HOLD（不建倉，排除於 tw_photonics 分析範圍） |
| **Conviction** | N/A |
| **Score** | 不適用 ×0.35 階段修正（身分錯誤,非單純配額排序問題） |
| **Phase** | Phase 1 Only（ticker–公司身分對照錯誤，依「價格與身分完整性」原則強制排除） |

---

## ⚠️ 排除理由：ticker–公司身分對照錯誤（非評分排序結果）

本檔之 Phase 1-only 分類**不是**因為正面選股評分未達門檻，而是因為**身分完整性問題**：
`universe.py` tw_photonics 清單中 5455.TWO 原意指向「英特磊科技（IntelliEPI Inc.）」，但 yfinance 查證其實際公司為**昇益開發（Sheng Yi Development Co., Ltd.）**，一家新竹房地產開發商,與矽光子產業無關。經 WebSearch 交叉驗證,英特磊正確 TPEx 代號應為 **4971.TWO**。

即使機械式套用正面選股評分準則,本檔亦僅獲 1-2/5 訊號（技術面與估值面邊緣通過,基本面、新聞面、情緒面皆未通過,詳見 fundamentals.md/sentiment.md）,故無論身分問題,本就不會進入 Phase 2-4。但此說明刻意置於「排除理由」而非單純評分結果,因為**身分錯誤本身已構成否決條件**,獨立於分數之上——不應用錯誤公司的資料去分析英特磊,亦不應用英特磊的名義去分析昇益開發。

## 正面選股評分（供完整性記錄）

| 訊號 | 條件 | 結果 | 狀態 |
|------|------|------|------|
| 基本面 | 營收成長 >15% YoY AND FCF/NI > -1 | 營收成長 yfinance 口徑 -100%（異常）;FCF/NI = -2.18 | ❌ 未通過 |
| 技術面 | RSI14<72 AND MACD hist 非深度負值 AND 價格>MA50 | RSI14 70.3（接近超買邊緣）；MACD hist +0.02；價格>MA50 | ✅ 技術面通過（但無產業意義） |
| 新聞 | 淨標題情緒為正向 | 無相關新聞（非光通訊業，不適用） | ❌ 未通過（無覆蓋） |
| 情緒 | 分析師共識≥60%買進或機構流向淨正向 | 零分析師覆蓋、零機構持股 | ❌ 未通過 |
| 估值 | forward P/E<35x 或顯著EPS成長催化劑確認 | forward P/E 無法計算 | ❌ 未通過 |

**結論**：1/5 訊號通過（技術面，但無產業意義），遠低於 3/5 門檻；且無論評分結果，身分錯誤本身已是獨立的排除條件。

## 建議後續行動

1. 建議 `pipeline/tools/universe.py` 將 tw_photonics 清單中的 5455.TWO 修正為 **4971.TWO**（英特磊科技正確代號）。
2. 下次 tw_photonics 排程時,以 4971.TWO 重新執行完整 Phase 1 分析。
3. 5455.TWO（昇益開發）本身若有分析需求,應歸類至適當的房地產/營建產業掃描,而非 tw_photonics。

FINAL DECISION COMPLETE
