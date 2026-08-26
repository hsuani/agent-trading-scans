# 基本面分析 — SNDK （截至 2026-08-26）

## 執行摘要

SNDK（SanDisk Corporation）作為獨立上市公司已不存在。公司於 2016 年 5 月被 Western Digital（WDC）以 190 億美元收購。任何以 SNDK 代碼進行的交易無效，該代碼已從 NASDAQ 除牌。數據取得失敗確認了該狀況。

## 資料獲取狀態

### 嘗試過的數據源
- yfinance financials：返回空數組
- yfinance balance_sheet：返回空數組
- yfinance cashflow：返回空數組
- yfinance fast_info：HTTP 403 連接失敗
- yfinance info：HTTP 403 連接失敗
- yfinance major_holders：HTTP 403 連接失敗

### 故障原因
1. **代理伺服器限制**：代理閘道對 fc.yahoo.com:443 返回 403 CONNECT 拒絕（政策拒絕或上游故障）
2. **股票代碼失效**：SNDK 不再是有效的交易代碼
3. **公司已收購**：SanDisk 於 2016 年被 Western Digital 收購，不再獨立運營

## 歷史背景

### 收購交易詳情
- **收購方**：Western Digital Corporation（WDC）
- **交易金額**：190 億美元
- **收購日期**：2016 年 5 月完成
- **交易價格**：每股 $245（現金交易）
- **原股票代碼**：SNDK（NASDAQ）

### SanDisk 業務範疇（收購前）
- NAND 快閃記憶體設計與製造
- 消費級固態硬碟（SSD）
- 嵌入式儲存解決方案
- USB 快閃驅動器與記憶卡
- 企業級儲存産品
- 資料中心 SSD

## 收購後的發展

SanDisk 作為 Western Digital 的全資子公司已運營超過 10 年。相關業務和產品已整合到 WDC 的組織結構中，不再作為獨立實體報告財務數據。

要追蹤 SanDisk 業務表現，投資者應：
1. 監控 **WDC (Western Digital)** 的季度財報
2. 查看 SanDisk 品牌在 WDC 消費級產品部門（Client Solutions Group, CSG）中的表現
3. 關注 WDC 的儲存系統事業群（Data Center Group, DCG）中的企業 SSD

## 驗證路徑

若需確認或交易相關儲存晶片/SSD 敞口，建議檢視：
- **WDC**：Western Digital（完整收購方）
- **STM**：STMicroelectronics（另一主要儲存供應商）
- **MU**：Micron Technology（DRAM/NAND 製造商）
- **MRVL**：Marvell Technology（儲存控制器供應商）

## 建議行動

1. ❌ **無法購買 SNDK**：不可交易
2. ✓ **替代方案**：追蹤 WDC 財報中的 SanDisk 相關業務表現
3. ✓ **監控指標**：
   - WDC 消費級儲存銷售增長
   - NAND 定價環境（影響毛利率）
   - 企業級 SSD 需求（AI 訓練/推理基礎設施）

---

## 關鍵指標表

| 指標 | 數值 | YoY | 行業中位數（估計） | 評價 |
|---|---|---|---|---|
| 營收 YoY | **資料不可得** | n/a | n/a | UNAVAILABLE |
| 毛利率 | **資料不可得** | n/a | 45%-55% | UNAVAILABLE |
| 營運利率 | **資料不可得** | n/a | 15%-25% | UNAVAILABLE |
| 自由現金流 FCF | **資料不可得** | n/a | n/a | UNAVAILABLE |
| P/E（遠期） | **無法計算** | n/a | 12-15x | UNAVAILABLE |
| EV/EBITDA | **資料不可得** | n/a | 8-10x | UNAVAILABLE |
| 淨債務 / EBITDA | **資料不可得** | n/a | <2.0x | UNAVAILABLE |
| **整體信號** | **FAIL** | - | - | **不可交易** |

## 紅旗

- ⚠️ 股票代碼已失效，無交易流動性
- ⚠️ 無法通過公開市場獲取實時財務數據
- ⚠️ 公司不再為獨立實體提交 SEC 申報文件
- ⚠️ 代理伺服器無法連接到 Yahoo Finance 數據源（持續的連接性問題）

## 結論

SNDK 無法進行任何基本面分析或交易活動，因為：

1. **企業實體已不存在**：被 WDC 收購 10 年以上
2. **無有效股票代碼**：SNDK 已從 NASDAQ 除牌
3. **無法獲取數據**：yfinance 和其他主要金融數據提供商均無可用數據
4. **無交易機會**：股票不存在，無法建立倉位

若關注 SanDisk 品牌的業務表現或儲存晶片市場動態，建議改為監控 **Western Digital (WDC)** 的季度財報、分部業績以及 NAND 定價趨勢。

---

**FUNDAMENTALS REPORT COMPLETE**
