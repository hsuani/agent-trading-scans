# 基本面分析 — IRM (鐵山公司) 截至 2026-07-25

## 執行總結

**數據可用性警告：無法獲取 Yahoo Finance 數據**

本分析無法完成。在 2026-07-24 至 2026-07-25 期間，yfinance 工具無法連接到 Yahoo Finance，代理閘道對 fc.yahoo.com 的 CONNECT 隧道連接返回政策拒絕 (403 錯誤)。嘗試檢索以下資料時失敗：
- fast_info (當前價格、50/200 日移動平均線)
- info (公司資訊、業務摘要、部門混合)
- financials (年度損益表)
- balance_sheet (年度資產負債表)
- cashflow (年度現金流量表)
- insider (內部人士交易記錄)

## 預期分析範圍 (未完成)

下列分析本應根據 yfinance 數據進行，但由於數據不可用而無法執行：

### 營收與成長性
- 記錄管理 (Records Management) 與數據中心 (Data Center) 的營收拆分
- 3-5 年年複合成長率 (CAGR)
- 年度環比 (YoY) 趨勢

### AFFO 與股息永續性
- 調整後營運現金流 (AFFO) 成長率
- 股息覆蓋率
- 股息收益率
- 股息支付比率

### 數據中心擴張
- Project Matterhorn 進展
- 超大規模數據中心贏單
- AI 尾風驅動的需求

### 槓桿與債務
- 淨債務 (Net Debt)
- 淨債務/EBITDA 比率
- 當前比率 (Current Ratio)
- 債務/權益比率

### 房地產投資信託指標
- 股息收益率
- 股息支付比率
- EV/EBITDA 估值倍數
- P/AFFO 估值倍數

### 內部人士活動
- 過去 6 個月的淨購買/售出
- 與市場資本額相對的規模

### 數位轉型與 AI 影響
- 數位轉型驅動的數據中心需求
- 超大規模客戶增長

## 技術障礙

**代理狀態：** 啟用，端口 42659
**TLS CA 束：** /root/.ccr/ca-bundle.crt (已安裝)
**近期中繼失敗：** 20+ 次對 fc.yahoo.com 的失敗 (2026-07-24 18:12:58 至 18:13:03 UTC)
**錯誤類型：** gateway answered 403 to CONNECT (policy denial or upstream failure)

建議行動：
1. 檢查上游 Yahoo Finance 可用性
2. 驗證代理策略對 fc.yahoo.com 的允許清單
3. 稍後重試或聯繫系統管理員

---

## 結論

**PRICE_DATA_UNAVAILABLE** — 無法檢索任何 IRM 基本面數據。報告無法完成。

FUNDAMENTALS REPORT INCOMPLETE - DATA UNAVAILABLE
