# 技術分析 — SH (空頭 S&P 500 ETF) 至 2026-09-06

## 狀態
**PRICE_DATA_UNAVAILABLE**

無法取得 SH 及 S&P 500 (^GSPC) 即時技術數據。Yahoo Finance 連線因組織代理政策限制而遭拒（query2.finance.yahoo.com、guce.yahoo.com、fc.yahoo.com）。

## 詳情
- 命令: `ta.py SH snapshot --period 2y` 與 `yf.py SH fast_info`
- 命令: `ta.py ^GSPC snapshot --period 2y` 與 `yf.py ^GSPC fast_info`
- 結果: 代理層級連線被拒 (connect_rejected，HTTP 403 組織政策否決)
- 影響: 無法提取以下任何數據：
  - SH 及 S&P 500 實時價格
  - 移動平均線 (MA20/50/200)
  - RSI14、MACD、Bollinger Bands %B
  - ATR14 與 20 日波動率
  - 52 週高低
  - 支撐/阻力位

## 與情緒分析的交叉參考

儘管缺乏實時技術數據，自 2026-09-06 情緒分析已發佈以下結論：

### S&P 500 極度樂觀背景 (EXTREME GREED)
- **估值過度延伸**: 前瞻本益比 22 倍（較 30 年平均高出 33%）
- **期權市場自滿**: 股票 PCR = 0.67（極度看漲，歷史頂部特徵）
- **恐懼壓抑**: VIX = 16.34（2026 年最低 14.13 附近）
- **放空平倉**: SPY 放空股數 94.4M，較 3 月峰值 134.0M 下降 29.6%
- **估值集中風險**: 前 10 大股票佔 38%，Nvidia + Micron 驅動 1/3 盈利增長
- **零售情緒乖離**: 零售投資者 58% 看跌，但市場繼續上升（經典頂部警告）

### 情緒評分
情緒分析結論：**PASS** — 市場已達到極度樂觀/貪婪極端，滿足典型市場頂部所有條件。

## 分析結果

### 無法驗證的技術信號
由於缺乏實時價格數據，無法計算以下條件：
- RSI14 > 70（超買確認）或 RSI14 < 30（超賣）
- MACD 直方圖動量方向與加速度
- 價格對 MA50/MA200 的位置
- Bollinger Bands %B（> 1.0 = 上方帶延伸）
- 近期 52 週高點距離
- 局部支撐/阻力位置

### 訊號評估
根據提供的指示，SH 的「PASS」條件為：
> **PASS if S&P 500 technically overbought/at risk AND SH not in freefall**

**情緒層面滿足**: ✓ S&P 500 在極度樂觀/貪婪極端（多個指標一致）  
**技術層面**: ✗ 無法驗證（價格數據不可用）  
**SH 狀態**: ✗ 無法確認 SH 是否處於自由落體（缺少實時價格）

## 建議行動

1. **解決代理政策阻止**: 確認組織是否允許 Yahoo Finance 數據訪問
   - 聯絡網絡/安全團隊解除 query2.finance.yahoo.com 等主機的 403 阻止
   - 或提供替代數據來源 (Bloomberg Terminal、Wind、Refinitiv 等)

2. **利用已有情緒數據**: 情緒分析已確認 S&P 500 極度樂觀設置；若技術確認，SH 作為反向對沖可能有吸引力

3. **重試計劃**: 一旦數據訪問恢復，重新運行 `ta.py SH snapshot` 與 `ta.py ^GSPC snapshot` 以取得完整技術讀數

---

**MARKET COMPLETE** (受限於數據可用性)
