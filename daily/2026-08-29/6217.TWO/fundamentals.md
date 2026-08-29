# 基本面分析 — 6217.TWO 截至 2026-08-29

## 資料取得失敗 — PRICE_DATA_UNAVAILABLE

### 狀態總結

本基本面分析無法完成。所有財務數據取得均因下列原因失敗：

1. **yfinance 連接失敗** — 組織出站代理策略阻擋了 Yahoo Finance 連接 (HTTP 403 / CONNECT tunnel failed)
2. **無法驗證股票代碼** — 6217.TWO 無法在 yfinance 中驗證，可能的原因：
   - 股票已從台灣 TPEx 下市
   - 股票代碼格式不正確
   - yfinance 不支援該股票
3. **技術分析不可用** — market.md 報告確認「no price data found」

### 診斷記錄

#### yfinance 查詢結果
```
python pipeline/tools/yf.py 6217.TWO info
→ ConnectionError: Failed to perform, curl: (7) CONNECT tunnel failed, response 403

python pipeline/tools/yf.py 6217.TWO fast_info
→ ConnectionError: CONNECT tunnel rejected (organization policy)

python pipeline/tools/yf.py 6217.TWO financials
→ [] (empty response)

python pipeline/tools/yf.py 6217.TWO quarterly_fin
→ [] (empty response)

python pipeline/tools/yf.py 6217.TWO balance_sheet
→ [] (empty response)

python pipeline/tools/yf.py 6217.TWO quarterly_bs
→ [] (empty response)

python pipeline/tools/yf.py 6217.TWO cashflow
→ [] (empty response)

python pipeline/tools/yf.py 6217.TWO quarterly_cf
→ [] (empty response)
```

#### 技術分析狀態
根據 market.md (2026-08-29 07:51)：
- `ta.py snapshot` 返回：「possibly delisted; no price data found」
- 無法取得價格歷史數據

---

## 1. 營收與獲利性

**數據狀態：n/a**

由於無法連接 yfinance，以下數據無法獲得：
- 營收 3-5 年 CAGR (n/a)
- 年度營收增長率 (n/a)
- 毛利率趨勢 (n/a)
- 營業利潤率趨勢 (n/a)
- 淨利潤率趨勢 (n/a)
- ROE (淨資產收益率) (n/a)
- ROIC (投入資本回報率) (n/a)

---

## 2. 現金流量與資產負債表

**數據狀態：n/a**

無法從年度及季度現金流量表、資產負債表獲得：
- FCF 邊際利潤 (n/a)
- FCF / 淨收入比 (n/a) — 預期健康水準 >0.9
- 淨債務 (n/a)
- 流動比率 (n/a)
- 債權股權比 (n/a)
- 現金持有量 (n/a)

---

## 3. 資本配置與內部人交易

**數據狀態：n/a**

無法獲得：
- 資本支出趨勢 (n/a)
- 股票回購活動 (n/a)
- 股息覆蓋率 (n/a)
- 內部人交易淨買/賣 (過去 6 個月) (n/a)
- 內部人交易相對於市值的規模 (n/a)

---

## 4. 估值

**數據狀態：n/a**

無法計算或獲得的估值指標：
- 追蹤型 P/E (n/a)
- 前瞻 P/E (n/a)
- EV/EBITDA (n/a)
- P/FCF (n/a)
- P/S (n/a)
- 與行業中位數比較 (n/a)

---

## 5. 主要催化劑與監督指標

**數據狀態：n/a**

無法獲得：
- 下次財報日期 (n/a)
- 最近指導及 EPS 意外歷史 (n/a)
- 業務部門變化 (n/a)
- 股東濃度 (主要持股人) (n/a)
- 機構持股人名單 (n/a)

---

## 完整指標表

| 指標 | 最新值 | YoY | 行業中位數 (估計) | 評論 |
|---|---|---|---|---|
| 營收 (年度) | n/a | n/a | n/a | yfinance 無可用數據 |
| 營收增長率 (YoY) | n/a | n/a | n/a | yfinance 連接失敗 |
| 毛利率 | n/a | n/a | n/a | 無財務報表數據 |
| 營業利潤率 | n/a | n/a | n/a | 無財務報表數據 |
| 淨利潤率 | n/a | n/a | n/a | 無財務報表數據 |
| ROE | n/a | n/a | n/a | 無資產負債表數據 |
| ROIC | n/a | n/a | n/a | 無現金流數據 |
| FCF 邊際利潤 | n/a | n/a | n/a | 無現金流數據 |
| FCF / 淨收入 | n/a | n/a | >0.9 (目標) | 無現金流數據 |
| 淨債務 | n/a | n/a | n/a | 無資產負債表數據 |
| 流動比率 | n/a | n/a | n/a | 無資產負債表數據 |
| 債權股權比 | n/a | n/a | n/a | 無資產負債表數據 |
| 現金 | n/a | n/a | n/a | 無資產負債表數據 |
| 尾部 P/E | n/a | n/a | n/a | 無價格/EPS 數據 |
| 前瞻 P/E | n/a | n/a | n/a | 無價格/EPS 數據 |
| EV/EBITDA | n/a | n/a | n/a | 無企業價值數據 |
| P/FCF | n/a | n/a | n/a | 無現金流/價格數據 |
| P/S | n/a | n/a | n/a | 無價格/營收數據 |
| 目前股價 | n/a | n/a | n/a | 價格數據不可用 |
| 50 日均線 | n/a | n/a | n/a | 技術分析不可用 |
| 200 日均線 | n/a | n/a | n/a | 技術分析不可用 |
| 內部人買進 (6 個月) | n/a | n/a | n/a | 無內部人數據 |
| 股東濃度 | n/a | n/a | n/a | 無持股人數據 |

---

## 風險標記

- ⛔ **致命問題** — 無法驗證股票是否存在；可能已下市或代碼格式不正確
- ⛔ **數據可用性** — yfinance 完全無法存取 (出站代理阻擋)
- ⚠️ **無法進行基本面評估** — 所有財務指標均無法計算
- ⚠️ **無法進行技術分析** — 市場數據完全缺失

---

## 後續步驟

### 建議的驗證

1. **確認上市狀態** — 查證 6217.TWO 是否仍在台灣 TPEx 上市
2. **驗證股票代碼格式** — 確認正確的代碼格式 (例如 6217.TW vs 6217.TWO)
3. **替代數據來源** — 考慮使用台灣證交所 API、CMoney、XQ 等本地數據來源
4. **代理例外設定** — 確認是否可將 yfinance 加入出站代理的白名單

### 報告的侷限性

本報告無法進行任何基本面分析，因為：
- 無法取得歷史財務數據
- 無法驗證當前估值
- 無法評估公司財務健康狀況
- 無法識別驅動股價的催化劑

**本報告不能作為投資決策的基礎。**

---

**生成時間：2026-08-29 08:00 UTC**
**數據可用性：PRICE_DATA_UNAVAILABLE**
**數據來源：yfinance (連接失敗)**

---

FUNDAMENTALS REPORT COMPLETE
