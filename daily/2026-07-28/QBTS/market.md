PRICE_DATA_UNAVAILABLE

# 技術分析 — QBTS (D-Wave Quantum) 截至 2026-07-28

## 資料狀態

無法獲取價格與技術指標資料。資料來源 (Yahoo Finance 及相關 API) 目前因代理 403 錯誤而無法訪問。

### 錯誤訊息
- `ta.py QBTS snapshot`: CONNECT tunnel failed, response 403
- `yf.py QBTS fast_info`: CONNECT tunnel failed, response 403
- 系統返回信息："possibly delisted; no price data found (period=1y)"

## 無法提供的分析項目

由於無法取得實時或歷史價格資料，以下分析項目無法完成：

- 快照資訊 (現價、MA20、MA50、MA200、RSI14、MACD)
- 趨勢分析 (價格相對移動平均線)
- 動能指標 (MACD、RSI、多時間框架回報)
- 超買/超賣狀態 (RSI、布林帶 %B)
- 波動率分析 (ATR14、年化波動率)
- 關鍵支撐/阻力水位 (52 週高位/低位、本地極值)
- 交易量確認

## 建議

請檢查：
1. 代理伺服器連接狀況 (查看 /root/.ccr/README.md 與 proxy 狀態)
2. QBTS 是否已退市或變更代碼
3. 數據源可用性

---

**報告完成** — 無法進行技術分析，資料不可用。

