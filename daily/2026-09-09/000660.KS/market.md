# Technical — 000660.KS (SK하이닉스) as of 2026-09-09

## PRICE_DATA_UNAVAILABLE

技術分析工具（`ta.py` 及 `yf.py`）因代理伺服器封鎖 `query2.finance.yahoo.com` 無法取得行情資料。

```
錯誤：CONNECT tunnel failed, response 403
工具：python3 pipeline/tools/ta.py 000660.KS snapshot → RuntimeError: no history
工具：python3 pipeline/tools/yf.py 000660.KS fast_info → ConnectionError 403
```

**所有技術指標（RSI14、MACD、MA50/MA200、ATR、BB %B）均無法計算。**

## 影響

- 市場評分訊號（Phase 1 Signal #2）標記為「跳過 / 0」
- 下游 Trader 不得生成基於即時價位的進場/停損/目標價
- 若未來資料恢復，需重新執行本模組

## 已知背景（非價格）

以下為基於公開資訊的定性評估，**不含任何捏造數字**：

- 000660.KS 在 KRX（韓國交易所）掛牌，因代理封鎖韓國市場資料源
- SK Hynix 為 KOSPI 市值前三大成份股
- 2025–2026 年因 HBM 超週期，股價較 2023 年低點大幅反彈（方向性判斷，無具體數值）
- 流動性充足，為 KOSPI 龍頭股，日成交量極高

## 結論

**PRICE_DATA_UNAVAILABLE — 技術面訊號無法評分，本輪 Market Signal = 跳過**

MARKET REPORT COMPLETE
