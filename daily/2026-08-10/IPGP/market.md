# 技術分析 — IPGP (2026-08-10)

## 狀態

**PRICE_DATA_UNAVAILABLE**

### 資料取得失敗原因

無法從 Yahoo Finance 數據源取得 IPGP 技術數據。網路策略阻止了對 fc.yahoo.com 的連接。

嘗試的資料來源：
- pipeline/tools/ta.py snapshot (--period 2y)
- pipeline/tools/yf.py fast_info
- pipeline/tools/yf.py history (--period 1y)

錯誤訊息：
```
Failed to get ticker 'IPGP' reason: Failed to perform, curl: (7) CONNECT tunnel failed, response 403.
gateway answered 403 to CONNECT (policy denial or upstream failure)
$IPGP: possibly delisted; no price data found (period=2y)
RuntimeError: no history for IPGP
```

### 後續步驟

- 檢查 IPGP 是否已退市或更改代碼
- 等待網路策略調整以允許 Yahoo Finance 連接
- 聯繫系統管理員確認資料源可用性

## 技術指標

無法計算。缺少必要的歷史價格數據。

---

**技術分析報告完成** — 資料不可用狀態
