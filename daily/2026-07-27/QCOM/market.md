# 技術分析 — QCOM，時間：2026-07-27

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

無法取得QCOM價格數據。系統級代理伺服器已封鎖對Yahoo Finance (fc.yahoo.com:443)的連接，返回403政策拒絕。

### 技術資訊無法生成的原因

本次分析依賴以下數據來源，目前均不可用：
- `ta.py snapshot` — 技術指標快照
- `ta.py series` — 歷史OHLCV數據與指標序列
- `yf.py fast_info` — 當前價格、MA20/MA50/MA200、52週高低

### 網絡狀態
```
Proxy Status: 403 CONNECT tunnel failed
Host: fc.yahoo.com:443
Reason: gateway answered 403 (policy denial or upstream failure)
```

## 無法提供的分析項目

由於缺乏實時價格與歷史數據，以下指標無法計算：

| 指標 | 狀態 |
|---|---|
| 當前價格 | 不可用 |
| MA20/MA50/MA200 | 不可用 |
| RSI14 | 不可用 |
| MACD | 不可用 |
| Bollinger Bands | 不可用 |
| ATR14 | 不可用 |
| 支撐/壓力位 | 不可用 |
| 成交量分析 | 不可用 |

## 趨勢判斷

無法進行。

## 技術訊號

**無法判定** — 缺乏數據支持

## 建議

- 待網絡連接恢復後重新執行分析
- 或由系統管理員配置代理以允許訪問Yahoo Finance服務

---

**分析時間**: 2026-07-27  
**資料來源**: 不可用  
**報告狀態**: PRICE_DATA_UNAVAILABLE

**市場報告完成**
