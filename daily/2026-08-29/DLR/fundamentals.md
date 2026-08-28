# DLR 基本面分析報告 — 2026-08-29

## 資料來源聲明

**PRICE_DATA_UNAVAILABLE** — 所有外部財務數據源均被組織網路政策阻擋：
- Yahoo Finance (query2.finance.yahoo.com, fc.yahoo.com) — HTTP 403 政策拒絕
- cnyes API (ws.api.cnyes.com) — HTTPS CONNECT 通道失敗
- 本地快取數據 — 不存在

無法取得實時價格、財務報表、現金流、資產負債表等任何關鍵 REIT 指標。

---

## 無法完成的分析範圍

因數據完全不可用，以下分析無法進行：

### 本應涵蓋的 REIT 特定指標（通常包括）
| 指標 | 目標 | 狀態 |
|---|---|---|
| FFO (Funds from Operations) 成長 | YoY >8-12% | **UNAVAILABLE** |
| AFFO (Adjusted FFO) 及覆蓋率 | AFFO / 股利 >1.2x | **UNAVAILABLE** |
| 佔用率（Occupancy Rate） | 90%+ | **UNAVAILABLE** |
| 債券水位（Net Debt / EBITDA） | <4.0x | **UNAVAILABLE** |
| 股利收益率（Dividend Yield） | 相對行業中位數評估 | **UNAVAILABLE** |
| 新簽租約（Lease Signings） | 規模及定價趨勢 | **UNAVAILABLE** |
| 區域組合（Geographic Mix） | 美國/歐洲/APAC 配置 | **UNAVAILABLE** |
| AI / 超大規模資料中心需求尾風 | 增長加速訊號 | **UNAVAILABLE** |

### 本應涵蓋的傳統財務指標
| 指標 | 狀態 |
|---|---|
| 營收及 3-5 年 CAGR | **UNAVAILABLE** |
| 淨利潤率、ROE、ROIC | **UNAVAILABLE** |
| 自由現金流（FCF）質量與 FCF/NI 比率 | **UNAVAILABLE** |
| 當前股價、P/E、EV/EBITDA、P/FCF | **UNAVAILABLE** |
| 內部人士交易活動（過去 6 個月） | **UNAVAILABLE** |
| 機構持股集中度 | **UNAVAILABLE** |
| 下一次財報日期及業績驚喜歷史 | **UNAVAILABLE** |

---

## 網路政策背景

組織代理（agent proxy）在以下域名級別阻擋了所有 HTTPS CONNECT 請求：
- `fc.yahoo.com` ×3 連接失敗
- `query2.finance.yahoo.com` ×4 連接失敗
- `guce.yahoo.com` ×3 連接失敗

根因：CONNECT tunnel failed, response 403 (organization policy)

該限制適用於所有嘗試的 API 端點（包括最初的 noProxy 例外清單之外的所有端點）。

---

## 建議的後續步驟

1. **網路政策豁免** — 聯繫 IT/安全團隊，是否可為交易掃描用途允許 Yahoo Finance 或替代財經數據源（例如 Alpha Vantage、Polygon.io）
2. **本地資料快取** — 在開始掃描前，預先下載並快取歷史財務數據至本地存儲
3. **替代數據源** — 若外網仍受限，考慮集成公開的 SEC 檔案（10-K、10-Q）爬蟲或其他本地化財經資料庫
4. **人工輸入** — 若此日期掃描為緊急優先，分析師可手動提供最新 FFO、佔用率、負債比率等關鍵 REIT 指標

---

## 核心指標摘要

| 指標 | 值 | YoY | 估計行業中位數 | 判決 |
|---|---|---|---|---|
| FFO 成長 | n/a | n/a | +8-12% | **DATA UNAVAILABLE** |
| 佔用率 | n/a | n/a | ~92% | **DATA UNAVAILABLE** |
| Net Debt / EBITDA | n/a | n/a | <4.0x | **DATA UNAVAILABLE** |
| 股利收益率 | n/a | n/a | ~3.5-4.0% | **DATA UNAVAILABLE** |
| 股價 / NAV | n/a | n/a | ~1.0-1.1x | **DATA UNAVAILABLE** |

---

## 紅旗清單

- 🚩 **零數據可用** — 無法進行基本面驗證
- 🚩 **無實時價格** — 無法計算任何估值倍數
- 🚩 **無現金流報表** — 無法驗證 FCF 質量或 FFO 可持續性
- 🚩 **無負債資訊** — 無法評估槓桿風險或利率敏感性
- 🚩 **無業績指導** — 無法捕捉短期催化劑或 AI 需求訊號

---

**Phase-1 Fundamentals Signal: NEGATIVE** (資料完全不可用，無法進行基本面評估)

**FUNDAMENTALS REPORT COMPLETE**
