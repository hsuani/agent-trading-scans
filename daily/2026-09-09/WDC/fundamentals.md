# 基本面分析 — WDC (西部數據) 截至 2026-09-09

## 執行摘要

**數據可用性狀態：PRICE_DATA_UNAVAILABLE**

無法完成本報告。組織代理政策阻止了所有金融數據源的訪問：
- Yahoo Finance (finance.yahoo.com, query2.finance.yahoo.com, guce.yahoo.com) — 403 政策拒絕
- yfinance 庫連接失敗（CONNECT tunnel failed, response 403）
- 未提供替代內部數據源或 WebSearch/WebFetch 工具

## 資料蒐集嘗試

### 已嘗試的數據源
1. **yfinance 工具庫** (`~/.claude/tools/trading/yf`) — 工具不存在於預期路徑
2. **Python yfinance 庫** — 代理 403 連接拒絕
3. **代理狀態檢查** — 確認 Yahoo Finance 域名被組織政策阻止：
   - guce.yahoo.com:443 → connect_rejected (policy denial)
   - query2.finance.yahoo.com:443 → connect_rejected (policy denial)
   - finance.yahoo.com:443 → connect_rejected (policy denial)

### 網路配置限制
- HTTPS_PROXY：http://127.0.0.1:43209（組織強制代理）
- CA 束：/root/.ccr/ca-bundle.crt
- 選擇性阻止政策已啟用，Yahoo Finance 主機無例外

## 所需資料（無法取得）

本報告需要以下資料以進行完整分析：

### 1. 收入與增長
- 過去 3-5 年年度財務報表
- 季度營收趨勢
- YoY 成長率

### 2. 盈利能力
- 毛利率、營業利潤率、淨利潤率趨勢
- ROE (股東權益報酬率)
- ROIC (投資資本回報率)

### 3. 現金流品質
- 自由現金流 (FCF)
- FCF 保證金
- FCF / NI 比率

### 4. 資產負債表
- 淨債務
- 流動比率
- 債務/權益比
- 現金狀況

### 5. 資本配置
- 資本支出趨勢
- 股票回購活動
- 股利覆蓋率

### 6. 內部人士活動
- 過去 6 個月內部交易
- 購買/出售淨額 vs 市值

### 7. 估值指標
- P/E 比 (尾隨/預期)
- EV/EBITDA
- P/FCF
- P/S vs 行業中位數

### 8. 業務背景
- 行業分類
- 市值
- 貝塔係數
- 最近上調/下調指引
- HDD 與其他存儲產品的營收混合

## 公司背景 (一般知識)

西部數據 (WDC) 是存儲解決方案提供商。公司於近年完成了重要重組：
- NAND 快閃記憶體業務分拆為獨立公司（現為 SNDK）
- 重組後主要聚焦於硬碟驅動 (HDD) 業務

此背景來自一般知識，而非當前財務數據。不應依賴用於投資決策。

## 建議解決方案

要完成本分析，需要以下之一：

1. **獲得政策例外**：與組織網路政策團隊合作，為財務數據源（Yahoo Finance、AlphaVantage、SEC EDGAR 等）添加例外
2. **替代數據源**：
   - SEC EDGAR 直接訪問（美國上市公司財務申報）
   - 內部數據庫或許可的財務平台
   - 公司投資者關係網站的 PDF 申報
3. **代理繞過**：如果允許，配置旁通或安全的內部財務 API

## 技術障礙摘要

```
組織代理配置：
- HTTPS_PROXY = http://127.0.0.1:43209
- 所有 HTTPS 連接通過組織代理
- Yahoo Finance 主機被明確拒絕（403 政策拒絕）
- 無例外配置已知

狀態：無法克服此限制。
```

---

**報告日期**：2026-09-09  
**資料可用性**：PRICE_DATA_UNAVAILABLE  
**分析狀態**：未完成 — 等待數據訪問權限

FUNDAMENTALS REPORT COMPLETE
