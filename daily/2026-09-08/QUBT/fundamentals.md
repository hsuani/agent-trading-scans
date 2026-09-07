# Fundamentals — QUBT as of 2026-09-08

## 資料可用性狀態

**❌ DATA_UNAVAILABLE**

yfinance 資料源（Yahoo Finance：query2.finance.yahoo.com, fc.yahoo.com；備用源：cnyes）被組織 egress proxy 封鎖，HTTP 403 政策拒絕。Fundamentals Analyst 工具集受限於 Bash/Read/Write，無法繞過 proxy 存取替代網路資源。

### 技術詳情
- Yahoo Finance：connect_rejected (gateway answered 403)
- cnyes 備用 API：connect_rejected (gateway answered 403)  
- TWSE 台股 API：未測試（美股票）
- 本地快取資料：無

---

## 預期分析框架（資料遮擋）

以下指標在資料恢復時應分析。基於使用者提供的脈絡：QUBT = 光子量子計算（photonic quantum computing）、早期階段、最小化營收。

### 1. 營收與成長性
**應檢視：**
- 3-5年營收 CAGR（預期：極少或負數——早期公司）
- YoY 趨勢
- 政府研發合約收入佔比（QUBT 關鍵驅動因素）

**關鍵風險：** 純研發公司無產品營收常態。政府合約（DOE、NSF、DARPA 等）中斷風險。

### 2. 獲利性
**應檢視：**
- Gross Margin、Operating Margin、Net Margin（預期：所有為負——R&D 集約型）
- ROE、ROIC（預期：無意義——虧損模式）

### 3. 現金流與現金燒燒率
**應檢視（最關鍵指標）：**
- 運營現金流 FCF（預期：大幅負數）
- **現金燒燒率：** (OCF in absolute) / quarterly 總支出
- **現金跑道：** 現金結餘 / 月均燒燒率（應 ≥ 12-24 個月）

**關鍵風險：** 早期量子公司典型燒燒率高。跑道短於 12 個月 = 融資風險極高。

### 4. 資產負債表
**應檢視：**
- 現金與等價物（絕對金額最重要）
- 淨債務
- 流動比率
- 債務/權益

**關鍵風險：** 虧損公司依賴現金持有和股權融資。債務融資風險高。

### 5. 資本配置與稀釋風險
**應檢視：**
- CapEx 趨勢（量子硬體公司通常資本密集）
- 股票回購（無——虧損公司不買回）
- 股利（無——虧損公司無股利）
- **股份稀釋歷史：** 發行股份數 YoY 增長率

**關鍵風險：** 頻繁融資稀釋現有股東。檢查過去 12-24 個月發行股份數。

### 6. 內部人士活動
**應檢視：**
- 過去 6 個月內部人士淨買賣
- 相對於市值的幅度

**解釋：** 早期公司內部人士賣出通常 = 現金需求或信心下降。

### 7. 估值
**應檢視：**
- P/E（虧損公司無意義）
- EV/EBITDA（EBITDA 為負或零 = 無意義）
- P/S（Price-to-Sales：適用於營收小公司）
- P/B（Price-to-Book：適用於資產型公司）

**框架：** 早期量子公司估值純粹投機——基於技術進展時間表、競爭格局、融資燃燒、現金跑道。

### 8. 關鍵催化劑
**應檢視：**
- 下次財報日期 + EPS 預期
- 近期指引變動
- **政府合約公告**（QUBT 的生命線）
- 技術里程碑宣布
- 融資輪新聞

**QUBT 特有：** 量子運算進展新聞、與大科技公司的合作、政府資助變化。

---

## 風險清單（基於行業，資料前未驗證）

- **現金燒燒耗盡：** 跑道 < 12 個月 → 1-2 年內融資或破產風險
- **過度稀釋：** 年度股份增長 > 20% → 內在價值侵蝕
- **政府資金流失：** 合約終止或資金削減 → 營收驟跌
- **技術不可行性：** 量子硬體瓶頸（QUBT 的光子方法可能失利於離子陷阱或超導方向）
- **競爭加劇：** IBM、Google、IonQ、Rigetti 等大參與者投資增加
- **股權融資完全稀釋：** 過度融資導致現有股東實質上毫無價值

---

## 指標表（資料遮擋）

| 指標 | 最新值 | YoY | 行業中位數估計 | 判定 |
|---|---|---|---|---|
| 營收（年） | n/a | n/a | n/a | ❌ |
| 營收成長 CAGR (3y) | n/a | n/a | n/a | ❌ |
| Gross Margin | n/a | n/a | n/a | ❌ |
| Operating Margin | n/a | n/a | n/a | ❌ |
| Net Margin | n/a | n/a | n/a | ❌ |
| ROE | n/a | n/a | n/a | ❌ |
| ROIC | n/a | n/a | n/a | ❌ |
| FCF Margin | n/a | n/a | n/a | ❌ |
| FCF / NI Ratio | n/a | n/a | n/a (N/A — NI < 0) | ❌ |
| 現金燒燒率（月） | n/a | n/a | n/a | ❌ |
| 現金跑道（月） | n/a | n/a | ≥ 12-24 (最低) | ❌ |
| 淨債務 | n/a | n/a | n/a | ❌ |
| 流動比率 | n/a | n/a | ≥ 1.5 | ❌ |
| 債務/權益 | n/a | n/a | < 1.0 | ❌ |
| P/E (Trailing) | n/a | n/a | n/a | ❌ |
| EV/EBITDA | n/a | n/a | n/a | ❌ |
| P/FCF | n/a | n/a | n/a | ❌ |
| P/S | n/a | n/a | n/a | ❌ |
| 內部人士淨買賣（6M） | n/a | n/a | n/a | ❌ |
| 股份稀釋 YoY | n/a | n/a | ≤ 5% (健康) | ❌ |

---

## 摘要

**基本面信號：❌ UNAVAILABLE — 代理工具集網路限制**

完整的 QUBT 基本面分析無法進行，因為 yfinance 後端被組織政策封鎖。推薦行動：

1. **要求 proxy 存取 yahoo.com** 以恢復 yfinance 功能
2. **替代方案：** 尋找企業提供的投資人關係資料或 SEC 提交文件（如 QUBT 上市 → 10-K / 10-Q），但此方法超出 Bash/Read/Write 工具集範圍
3. **本輪判定：** Fundamentals 信號 = ❌ UNAVAILABLE，不計入交易決策

---

*Phase 1 Fundamentals 框架存根 — 非主動分析結果*

FUNDAMENTALS REPORT COMPLETE
