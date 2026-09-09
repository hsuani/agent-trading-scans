# Trade proposal — MRVL as of 2026-09-07

FINAL TRANSACTION PROPOSAL: **HOLD**

> **框架**：Framework B（既有持倉審查）。當前為已持有多頭部位，本提案評估「維持現倉 / 條件性加碼 / 減碼」。

---

## Direction

**HOLD（維持現有多頭，條件性加碼）**

研究管理員結論：LONG、conviction MEDIUM。財報後股價單日跌逾 10% 為「利多出盡」警示，但 Google 認股權憑證合約（行使價 $206.58，[PRICE_DATA_UNAVAILABLE — 基本面錨定]）提供有效下檔結構支撐。在 Q3 FY27 資料中心年增率 ≥60% 獲財報確認之前，**不主動加碼至滿倉**。

---

## Setup

> 所有價格標記 **[PRICE_DATA_UNAVAILABLE — 基本面估算]**，Yahoo Finance 被代理阻擋（HTTP 403），無即時市場報價。

**現有持倉**：維持原倉位，無需調整。

**條件性加碼區間（Add Tranche）**：
```
Entry（加碼區）: $204 – $210  [PRICE_DATA_UNAVAILABLE — 估算]
  依據：Google 認股權行使價 $206.58 為已驗證合約錨點；
        Non-GAAP EPS FY27 ~$3.80 × P/E 55x = $209 為估值下緣
```

```
Stop: $198  [PRICE_DATA_UNAVAILABLE — 估算]
  依據：$206.58 有效跌破後 ~4% 緩衝確認跌破，非噪音；
        跌破此位代表 Google 認股權水下，合約信號轉為負面，
        多頭核心論點（合約支撐 + 估值地板）同步失效
```

```
Target 1: $247  [PRICE_DATA_UNAVAILABLE — 估算]
  依據：Non-GAAP EPS FY27 ~$3.80 × P/E 65x（成長溢價上緣）
        = $247；對應 Q3 財報確認後估值重評區間頂端
```

```
Target 2: $285  [PRICE_DATA_UNAVAILABLE — 估算]
  依據：44 名分析師共識目標均價 $284.8（有具名研究支撐）；
        亦對應 FY28 $18B 指引可達成情境的中性估值折現
```

**R:R（以加碼中位點 $207 計算）**：
- R:R to T1：(247 − 207) ÷ (207 − 198) = **4.4x** ✓（門檻 ≥1.5 for LONG）
- R:R to T2：(285 − 207) ÷ (207 − 198) = **8.7x** ✓

---

## Sizing

**現有持倉**：維持不動，不削減，不加倉（MEDIUM conviction，估值 P/E 73x 無容錯空間）。

**條件性加碼批次**：**Small — 0.5% of portfolio NAV**

| 項目 | 說明 |
|---|---|
| Conviction | MEDIUM |
| ATR 估算 | ~$5–8（[PRICE_DATA_UNAVAILABLE]，財報日單日振幅 ~10% 反推） |
| 年化波動率 | 估算 ~45–55%（高於半導體中位數，反映集中度風險） |
| 加碼上限 | 現有倉 + 加碼批次合計不超過 Medium（1.5% NAV）；ATR 過大不宜超配 |

---

## Time horizon

**3m+**（核心多頭持倉）

Google ASIC 大量收益入帳點為 FY29（約 2028 年底）；下一個關鍵驗證節點為 **Q3 FY27 財報**（預估 2026 年 11–12 月），構成 1–3 個月的短期觀察窗口。

---

## Trigger

**現有持倉**：立即維持（Enter now — hold）。

**加碼批次**：等待以下條件同時成立方可執行：
1. **Q3 FY27 資料中心年增率 ≥60%** 由財報數字確認，且
2. 管理層確認 Google 首批量產訂單已開始入帳（或 FY28 $18B 指引未下修），且
3. 股價在 **$204–$210 支撐區** 獲得技術確認（非加速跌破）

三者缺一不可；若股價跌至該區但財報尚未公告，應**等候財報結果後再行動**，避免在不確定性最高點倉促加碼。

---

## Invalidation

以下任一事件發生，**立即重新評估並考慮減倉或全出**：

- **價格層面**：$198 有效收盤跌破（Google 認股權水下 + 估值地板失守，[PRICE_DATA_UNAVAILABLE — 估算]）
- **基本面層面**：Q3 FY27 單季營收低於 $29 億（指引 miss）；或 FY28 $18B 年度指引被管理層下修
- **合約層面**：Google 公開宣布縮減外部 ASIC 採購、加速自製化、或訂單轉向 Broadcom
- **毛利層面**：Non-GAAP 毛利率出現季度性收縮（訂價權喪失信號）

---

## Catalyst calendar

| 預估日期 | 事件 |
|---|---|
| 2026年11–12月 | Q3 FY27 財報——核心驗證節點：資料中心年增率 ≥60%？Google 訂單入帳？ |
| 2026年10–11月 | 半導體行業法說會季（AVGO、NVDA 法說可提供 AI ASIC 需求能見度） |
| 2026年持續監控 | Google 認股權行使價 $206.58 股價距離（[PRICE_DATA_UNAVAILABLE]） |
| 2026–2027年 | CPO（Co-packaged Optics）量產客戶認證公告 |
| 2027年 | FY28 指引季度追蹤（$18B 目標進度） |

---

TRADE PROPOSAL COMPLETE
