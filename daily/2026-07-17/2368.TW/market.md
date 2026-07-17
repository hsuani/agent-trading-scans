# 技術分析 — 2368.TW 截至 2026-07-17

## 狀態：資料無法取得

**PRICE_DATA_UNAVAILABLE**

### 原因
代理伺服器阻止了與 Yahoo Finance (fc.yahoo.com) 的連接，回應代碼 403。無法取得實時價格數據、移動平均線、RSI、MACD 及其他技術指標。

### 資料來源
- ta.py snapshot 呼叫：失敗 (HTTP 403)
- yf.py fast_info 呼叫：失敗 (HTTP 403)

### 影響
無法進行以下分析：
- 快照資訊（現價、MA20/MA50/MA200、RSI14、MACD）
- 趨勢判斷
- 動能評估
- 關鍵價位認定
- 波動率計算

---

**必須解決代理連接問題以恢復 2368.TW 技術分析能力。**

技術報告完成。
