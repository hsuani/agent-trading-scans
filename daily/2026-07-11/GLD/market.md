# Technical — GLD 2026-07-11

## Status

**PRICE_DATA_UNAVAILABLE**

無法取得 GLD 價格數據。技術分析工具對 Yahoo Finance 之連線遭到代理政策阻止 (HTTP 403)。

## 資料收集結果

| 嘗試來源 | 狀態 | 詳情 |
|---|---|---|
| ta.py GLD snapshot (2y) | 失敗 | fc.yahoo.com:443 連線被拒 - 政策阻止 |
| yf.py GLD fast_info | 失敗 | fc.yahoo.com:443 連線被拒 - 政策阻止 |
| ta.py GLD levels (1y) | 失敗 | fc.yahoo.com:443 連線被拒 - 政策阻止 |

## 無法進行之分析項目

因無價格數據，以下技術指標無法計算：

- **Trend (趨勢分析)**: MA20, MA50, MA200 位置無法確定
- **Momentum (動量)**: MACD, RSI14, 多時段報酬無法計算
- **Overbought/Oversold (超買/超賣)**: RSI14, Bollinger Bands %B 無法評估
- **Volatility (波動率)**: ATR14, 20日年化波動率無法估算
- **Key Levels (關鍵位置)**: 支撐/阻力位置無法識別
- **Volume Confirmation (成交量確認)**: 無成交量數據

## 建議行動

待外部數據源連線恢復後，重新執行技術分析掃描。

---

**MARKET REPORT COMPLETE** — 因數據不可用無法完成分析
