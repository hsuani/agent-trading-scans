# 技術分析 — 6515.TW 截至 2026-07-18

## 資料取得狀態

**PRICE_DATA_UNAVAILABLE**

## 問題說明

無法取得 6515.TW (穎崴科技) 的技術分析資料。原因如下：

### 1. 網路連接問題
- 代理伺服器對 Yahoo Finance (fc.yahoo.com) 發出 403 Policy Denial
- 資料工具無法通過企業代理連線至資料來源
- 多次重試均失敗，連接遭到上游閘道拒絕

### 2. 資料可用性問題
- 系統回報：「$6515.TW: possibly delisted; no price data found」
- 該股票在 Yahoo Finance 無歷史資料可用
- 2 年期間 (--period 2y) 與 1 年期間 (--period 1y) 均無結果

## 無法進行的分析

下列指標無法計算：
- 價格與 MA20/MA50/MA200 關係
- RSI14 超買/超賣狀態
- MACD 信號與柱狀圖
- Bollinger Bands %B 位置
- ATR14 波動率
- 近期支撐/阻力位
- 技術走勢判定

## 建議行動

1. 驗證股票代碼是否正確 (TWSE: 6515.TW 或可能已變更)
2. 確認該股票是否仍在台灣證券交易所掛牌
3. 檢查代理伺服器政策設定，確認是否允許訪問 Yahoo Finance
4. 如股票仍在交易，可嘗試直接連接 TWSE 官方資料來源

---

**技術分析報告無法完成** - 資料不可用
