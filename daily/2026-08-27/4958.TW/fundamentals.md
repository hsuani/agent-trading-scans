# 基本面分析 — 4958.TW（臻鼎-KY）截至 2026-08-27

## 資料狀態

**DATA_UNAVAILABLE**

### 原因

代理閘道（proxy gateway）禁止訪問所有財務數據源：
- Yahoo Finance (fc.yahoo.com) — 403 CONNECT 被拒
- 鉅亨網 API (ws.api.cnyes.com) — 403 CONNECT 被拒  
- 台灣證券交易所 TWSE (mis.twse.com.tw) — 403 CONNECT 被拒

### 不可用數據類別

以下分析無法進行（不予發明數據）：

| 數據類別 | 狀態 |
|---|---|
| 公司概況與估值 | 無法取得 |
| 即時股價與移動平均 | 無法取得 |
| 年度與季度財報 | 無法取得 |
| 資產負債表 | 無法取得 |
| 現金流量表 | 無法取得 |
| 盈利預告與歷史 | 無法取得 |
| 內部人交易 | 無法取得 |
| 主要股東持股 | 無法取得 |
| 機構投資者持股 | 無法取得 |

### 執行步驟

1. 嘗試 yfinance info — 失敗 (CONNECT tunnel failed, 403)
2. 嘗試 yfinance fast_info — 失敗 (Yahoo Finance blocked)
3. 嘗試 cnyes fallback — 失敗 (proxy blocked)
4. 嘗試 TWSE API — 失敗 (proxy blocked)

### 建議

- 聯繫基礎設施團隊確認網路策略配置
- 檢查代理閘道的出站白名單設定
- 重新嘗試可用的本地資訊源（如果有）

---

## 報告狀態

無法進行盈利能力、現金流、資本結構、內部人信號、估值、催化劑等完整分析。

本報告無法提交給交易員做決策依據。

**FUNDAMENTALS REPORT INCOMPLETE — DATA UNAVAILABLE**
