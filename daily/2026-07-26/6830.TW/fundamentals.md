# 基本面分析 — 6830.TW (汎銓科技) 截至 2026-07-26

## 執行總結

**DATA_UNAVAILABLE：無法獲取財務數據**

由於組織的出境代理政策限制，無法訪問以下必要的數據來源：
- Yahoo Finance (fc.yahoo.com) — yfinance 工具依賴
- 台灣證券交易所 (mis.twse.com.tw)
- 台灣財經數據服務 (ws.api.cnyes.com)

本報告無法完成基本面分析。

## 數據可用性狀態

### 嘗試收集的數據點

| 數據類別 | 狀態 | 錯誤說明 |
|---------|------|--------|
| 公司信息 (info) | DATA_UNAVAILABLE | ProxyError: CONNECT tunnel failed, 403 |
| 即時價格與均線 (fast_info) | DATA_UNAVAILABLE | ProxyError: CONNECT tunnel failed, 403 |
| 年度財務報表 (financials) | DATA_UNAVAILABLE | 空結果 |
| 年度資產負債表 (balance_sheet) | DATA_UNAVAILABLE | 空結果 |
| 年度現金流量表 (cashflow) | DATA_UNAVAILABLE | 空結果 |
| 財報公告日期 (earnings_dates) | DATA_UNAVAILABLE | ProxyError: CONNECT tunnel failed, 403 |
| 董監持股交易 (insider) | DATA_UNAVAILABLE | ProxyError: CONNECT tunnel failed, 403 |
| 主要股東 (major_holders) | DATA_UNAVAILABLE | ProxyError: CONNECT tunnel failed, 403 |

### 代理政策錯誤日誌

根據 `curl -sS $HTTPS_PROXY/__agentproxy/status` 的最近失敗記錄：

```
時間戳：2026-07-25T18:19:06.807Z
連接類型：connect_rejected
詳細：gateway answered 403 to CONNECT (policy denial or upstream failure)
主機：mis.twse.com.tw:443

時間戳：2026-07-25T18:19:09.574Z
連接類型：connect_rejected
詳細：gateway answered 403 to CONNECT (policy denial or upstream failure)
主機：fc.yahoo.com:443
```

## 公司背景

**公司名稱**：汎銓科技 (Marketech International)  
**代號**：6830.TW  
**交易所**：台灣證券交易所 (TWSE)  
**產業**：半導體光電測試/材料分析  
**主要業務**：
- 半導體製程測試與計量 (metrology)
- 先進封裝與 CPO (Chiplet/光學連接) 測試
- 光電子與光子測試服務

## 預期分析內容（未能完成）

### 營收與獲利能力
- 3-5年複合年增長率 (CAGR)：DATA_UNAVAILABLE
- 年增長率趨勢 (YoY)：DATA_UNAVAILABLE
- 業務分項結構：DATA_UNAVAILABLE
- 毛利率/營業利率/淨利率趨勢：DATA_UNAVAILABLE
- 股東權益報酬率 (ROE)：DATA_UNAVAILABLE
- 投入資本報酬率 (ROIC)：DATA_UNAVAILABLE

### 現金流量與資產負債表
- 自由現金流邊際 (FCF margin)：DATA_UNAVAILABLE
- FCF/淨利比率：DATA_UNAVAILABLE
- 淨債務 (Net Debt)：DATA_UNAVAILABLE
- 流動比率 (Current Ratio)：DATA_UNAVAILABLE
- 債務/權益比 (Debt/Equity)：DATA_UNAVAILABLE
- 現金部位：DATA_UNAVAILABLE

### 資本配置與內線訊號
- 資本支出趨勢 (Capex)：DATA_UNAVAILABLE
- 回購活動：DATA_UNAVAILABLE
- 現金股利覆蓋率：DATA_UNAVAILABLE
- 近 6 個月內線交易活動：DATA_UNAVAILABLE
- 內線淨買入/賣出vs市值規模：DATA_UNAVAILABLE

### 估值指標
- 尾隨本益比 (Trailing P/E)：DATA_UNAVAILABLE
- 前瞻本益比 (Forward P/E)：DATA_UNAVAILABLE
- EV/EBITDA：DATA_UNAVAILABLE
- P/FCF (價格/自由現金流)：DATA_UNAVAILABLE
- P/S (價格/銷售)：DATA_UNAVAILABLE
- 與產業中位數比較：DATA_UNAVAILABLE

### 關鍵催化劑
- 下次財報公告日期：DATA_UNAVAILABLE
- 近期指引與收入預期：DATA_UNAVAILABLE
- 產業動態 (CPO 測試需求、封裝技術轉變)：DATA_UNAVAILABLE

## 關鍵指標表

| 指標 | 最新值 | YoY 變化 | 產業中位數估計 | 評價 |
|-----|-------|---------|------------|------|
| 營收 (年度) | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | n/a |
| 毛利率 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | n/a |
| 營業利率 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | n/a |
| 淨利率 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | n/a |
| ROE | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | n/a |
| 股東權益 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | n/a |
| 流動比率 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | n/a |
| 本益比 (P/E) | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | n/a |
| 自由現金流 | DATA_UNAVAILABLE | DATA_UNAVAILABLE | n/a | n/a |

## 風險旗標

### 數據缺失風險
- ❌ 無法驗證公司財務健全度
- ❌ 無法評估營收增長動力 (尤其是 CPO 測試需求)
- ❌ 無法確認現金流質量與資本結構健全性
- ❌ 無法評估內線持股者信心

### 建議後續行動

1. **代理政策協調**：向組織管理部門或 Anthropic 支援報告對台灣金融數據來源 (TWSE、Yahoo Finance) 的封鎖
2. **替代數據來源**：
   - 查詢公司官方 IR 網站是否提供英文財報或 ADR 上市資訊
   - 考慮使用本地台灣財務數據服務 (需組織政策解禁)
   - 尋求本地研究報告或主經紀人研究
3. **後續分析時機**：待代理政策更新後，重新執行完整基本面分析

---

**報告狀態**：DATA_UNAVAILABLE  
**生成時間**：2026-07-26  
**數據來源**：yfinance API (blocked by proxy policy)  

**基本面分析未能完成** ❌

FUNDAMENTALS REPORT COMPLETE
