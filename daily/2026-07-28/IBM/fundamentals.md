# 基本面分析 — IBM (International Business Machines) 至 2026-07-28

## FUNDAMENTALS_DATA_UNAVAILABLE

### 資料獲取狀態

使用 pipeline/tools/yf.py 獲取 IBM 基本面資料時遭遇代理阻擋：

**阻擋詳情：**
- **目標主機**：fc.yahoo.com:443 (Yahoo Finance)
- **錯誤代碼**：403 (Forbidden)
- **原因**：組織政策拒絕 (policy denial) — 代理網關上游拒絕該目標主機的連接
- **時間戳**：多次失敗於 2026-07-27 20:14 - 20:18 UTC

**嘗試的數據請求：**
- info (公司資料 + 主要統計)
- fast_info (即時報價)
- financials (年度損益表)
- quarterly_fin (季度損益表)
- balance_sheet (資產負債表)
- quarterly_bs (季度資產負債表)
- cashflow (現金流表)
- quarterly_cf (季度現金流表)
- earnings_dates (盈利預告及歷史)
- insider (內部交易)
- major_holders (主要持股人)
- inst_holders (機構持股人)

### 可用備選渠道

根據 yf.py 工具設計，當 Yahoo Finance 不可用時，存在以下備選方案：
- **TWSE/TPEX API**：僅適用於台灣上市股票 (.TW 或 .TWO)，不適用於 IBM (NYSE:IBM)
- **Cnyes API**：同樣因代理政策被阻擋 (ws.api.cnyes.com:443)

### 無法進行的分析

由於基礎財務數據無法獲得，以下分析項目無法完成：

1. **營收與成長**
   - 3-5 年複合年成長率 (CAGR)
   - 年度與季度營收趨勢
   - 軟體、顧問、基礎設施等事業部營收混合

2. **獲利能力**
   - 毛利、營業利潤、淨利潤率趨勢
   - ROE (股東權益報酬率)
   - ROIC (投資資本報酬率)

3. **現金流質量**
   - 自由現金流 (FCF) 邊際
   - FCF / 淨利潤比率

4. **資產負債表**
   - 淨債務狀況
   - 流動比率
   - 債務 / 權益比率

5. **資本配置**
   - 資本支出趨勢
   - 股票回購計畫
   - 股利覆蓋率

6. **內部人士交易信號**
   - 過去 6 個月淨買賣情況
   - 相對市值大小的交易幅度

7. **估值分析**
   - 本益比 (P/E)、預期本益比
   - EV/EBITDA
   - 本益比 / 自由現金流
   - 與科技業同業比較

8. **關鍵催化劑**
   - 下次盈利發佈日期
   - 最近 Q2 2026 盈利報告狀態
   - 量子計算投資進展
   - HashiCorp 整合影響
   - 股利與資本返還計畫

### 后续步骤建议

1. **解除代理限制**：需聯絡系統管理員或 Anthropic 支援，申請對 fc.yahoo.com:443 的存取權限
2. **替代數據源**：考慮使用 Bloomberg Terminal、FactSet 或其他獲授權的企業財務數據庫
3. **手動輸入**：若可取得最新 IBM 財務資訊 (例如官方投資者關係頁面或 SEC 檔案)，可手動補充分析

---

**報告生成時間**：2026-07-28  
**分析對象**：IBM (NYSE:IBM)  
**狀態**：基礎面資料不可用 — 代理政策阻擋

