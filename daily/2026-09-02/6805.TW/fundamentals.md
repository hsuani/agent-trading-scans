# 基本面分析 — 6805.TW (富世達) 截至 2026-09-02

## 執行摘要

**DATA_UNAVAILABLE** — yfinance 連線失敗，無法檢索財務數據。

組織代理政策阻止訪問 Yahoo Finance 伺服器 (query2.finance.yahoo.com、fc.yahoo.com、guce.yahoo.com 返回 connect_rejected)，導致無法獲取以下必要資料：
- 股價與技術指標 (fast_info)
- 年度與季度財務報表 (financials、quarterly_fin)
- 資產負債表 (balance_sheet、quarterly_bs)
- 現金流量表 (cashflow、quarterly_cf)
- 公司資訊與估值倍數 (info)
- 內部人交易記錄 (insider)
- 持股集中度 (major_holders、inst_holders)
- 盈利公告日期 (earnings_dates)

## 情況說明

富世達 (6805.TW) 是台灣冷卻與散熱元件製造商，於 2026 年 7 月被納入投資組合，供應鏈對標韋拉魯賓台灣計畫。據供應商背景，公司主要生產伺服器散熱組件，受惠於 AI 伺服器需求成長。

然而，無法透過現有數據工具驗證：
- 實際營收成長率 (目標：>15% YoY)
- 自由現金流品質 (FCF/NI > -1)
- 前向估值吸引力 (Forward P/E < 35x 或 EPS 成長催化劑)

## 建議

1. **替代資訊源**：
   - 直接從台灣證券交易所 (TWSE) 投資人關係網站下載 6805 年度/季度財務報表
   - 聯繫公司投資人關係部門取得最新指引與盈利預測
   - 查詢台灣證交所公開資訊觀測站 (mops.tse.org.tw) 的季報與年報

2. **代理設定**：
   - 確認是否可授權例外訪問台灣證券資料源或替代 API (如台灣 Bloomberg 終端、富邦金控研究部)
   - 考慮使用本地台灣財務數據庫 (如 Goodinfo、CMoney)

## 信號評估

由於數據不可用，無法評估以下信號：

| 信號 | 預期標準 | 結果 | 原因 |
|---|---|---|---|
| **營收成長** | >15% YoY | **DATA_UNAVAILABLE** | 無年度與季度財務數據 |
| **自由現金流** | FCF/NI > -1 | **DATA_UNAVAILABLE** | 無現金流量表 |
| **估值** | Forward P/E < 35x 或 EPS 成長 | **DATA_UNAVAILABLE** | 無股價、估值倍數或 EPS 指引 |

---

**報告狀態**：無法完成完整基本面分析  
**數據可用性**：0%  
**最後更新**：2026-09-02 (yfinance 請求失敗)

---

## 後續步驟

待數據源恢復或替代渠道建立後，需執行完整基本面審查，涵蓋：
- 3~5 年營收複合年增長率 (CAGR)
- 毛利率、營業利潤率、淨利率趨勢
- 資本配置 (資本支出、股票回購、股息覆蓋率)
- 內部人與機構持股動向
- 相對估值 (P/E、EV/EBITDA、P/FCF vs 台灣冷卻部門中位數)

