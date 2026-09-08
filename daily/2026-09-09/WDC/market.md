# Technical — WDC (Western Digital) as of 2026-09-09

## PRICE_DATA_UNAVAILABLE

技術分析工具（`ta.py` 及 `yf.py`）因代理伺服器封鎖 `query2.finance.yahoo.com` 無法取得行情資料。

```
錯誤：CONNECT tunnel failed, response 403
工具：python3 pipeline/tools/ta.py WDC snapshot → RuntimeError: no history
工具：python3 pipeline/tools/yf.py WDC fast_info → ConnectionError 403
```

**所有技術指標（RSI14、MACD、MA50/MA200、ATR、BB %B）均無法計算。**

## 影響

- 市場評分訊號（Phase 1 Signal #2）標記為「跳過 / 0」
- 下游 Trader 不得生成基於即時價位的進場/停損/目標價
- 若未來資料恢復，需重新執行本模組

## 已知背景（非價格）

以下為基於公開資訊的定性評估，**不含任何捏造數字**：

- WDC 在 NASDAQ 掛牌，分拆後成為純 HDD 標的
- 傳統上與 Seagate（STX）高度相關，同受 Nearline HDD 景氣影響
- 分拆重組完成後，機構持股重組中，股價反映轉型溢價
- Beta 預估 ~1.0–1.4（較 SNDK 穩定）

## 結論

**PRICE_DATA_UNAVAILABLE — 技術面訊號無法評分，本輪 Market Signal = 跳過**

MARKET REPORT COMPLETE
