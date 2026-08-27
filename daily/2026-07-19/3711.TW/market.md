# 技術面分析報告 — 日月光投控 (3711.TW)
**日期：** 2026-07-19
**分析師：** Phase-1 Market Agent
**類別：** 先進封測（CPO下游封裝測試）

---

## 一、價格資料狀態

```
PRICE_DATA_UNAVAILABLE
```

本次嘗試透過以下工具取得即時價格與技術指標資料：
- `python3 pipeline/tools/ta.py 3711.TW snapshot` → 失敗（HTTP 403 / curl tunnel error）
- `python3 pipeline/tools/yf.py 3711.TW fast_info` → 失敗（HTTP 403 / curl tunnel error）

台灣上市股票（.TW後綴）資料源當前遭proxy封鎖，無法取得即時或歷史OHLCV資料，因此以下技術指標**均無法計算**：

| 指標 | 數值 | 狀態 |
|------|------|------|
| RSI-14 | N/A | PRICE_DATA_UNAVAILABLE |
| MACD（12,26,9） | N/A | PRICE_DATA_UNAVAILABLE |
| MA-50 | N/A | PRICE_DATA_UNAVAILABLE |
| MA-200 | N/A | PRICE_DATA_UNAVAILABLE |
| Bollinger Bands | N/A | PRICE_DATA_UNAVAILABLE |
| 成交量趨勢 | N/A | PRICE_DATA_UNAVAILABLE |

---

## 二、網路搜尋補充之市場資訊（參考用，非官方即時資料）

根據網路搜尋結果所取得之非官方市場資訊（僅供參考，請以TWSE官方資料為準）：

| 項目 | 資訊 | 來源 |
|------|------|------|
| 近期高點 | 約 NT$729（2026-07-02創歷史新高） | 搜尋結果引用 |
| 近期參考價 | 約 NT$641（2026年7月） | 搜尋結果引用 |
| 外資目標價區間 | NT$520 ~ NT$840 | TradingView分析師預測 |
| 修正後目標價 | NT$840（由NT$750上調） | 外資報告 |
| BofA目標價（NYSE:ASX） | $48（由$36上調），維持Buy | 外資報告 |

**注意：** 上述數值為網路搜尋摘錄，非即時交易所資料，不得作為交易依據。

---

## 三、技術面背景解讀（基於基本面與新聞面推斷）

雖無法取得正式技術指標數值，以下為基於已知資訊之結構性判讀：

1. **趨勢背景：** 股價於2026-07-02觸及歷史新高NT$729，顯示中期多頭動能強勁。
2. **近期修正：** 高點後約回落至NT$641區域（約-12%），可能屬高位換手整理。
3. **RSI推測：** 從NT$729歷史高點後回落至NT$641，若拉長觀察窗口，RSI可能已自超買區間向下修正，惟實際數值需透過正式資料來源確認。
4. **MA結構：** 長期上升趨勢下，短線若整理完畢，支撐參考位可能落於NT$600~NT$630區間（推測），需實際K線確認。
5. **成交量：** Q2財報超預期（+26.7% YoY），基本面利多若帶動外資回補，成交量可能為確認訊號。

---

## 四、技術面判定

由於無法取得正式即時價格資料（PRICE_DATA_UNAVAILABLE），依照pipeline規則：

**M = N/A**

技術面判定暫時標記為N/A，不影響其他三項（F/N/S）之評分。建議於資料可用時重新執行技術面掃描。

---

## 五、後續行動建議

- 資料恢復後，優先確認：
  1. RSI-14是否已從超買區間（>70）回落至合理水位
  2. MACD是否形成金叉或維持正值
  3. 股價是否站穩MA-50（短期支撐確認）
- 若NT$641為近期整理底部且MA-50支撐有效，技術面轉PASS條件存在

---

> **M = N/A（PRICE_DATA_UNAVAILABLE）**

---
*資料來源：pipeline/tools/ta.py、pipeline/tools/yf.py（均返回403錯誤）；補充資訊來自TradingView搜尋結果（非官方即時資料）*
