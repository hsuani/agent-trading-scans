# 技術分析 — GFS 於 2026-07-26

## 狀態

**PRICE_DATA_UNAVAILABLE**

## 問題說明

無法取得 GFS（GlobalFoundries）的即時價格數據和技術指標。

### 根本原因
- 資料來源：Yahoo Finance (fc.yahoo.com) 
- 狀態：組織政策 403 禁止（Gateway 403 Policy Denial）
- 嘗試次數：3 次
- 工具：
  - `ta.py GFS snapshot` → 失敗
  - `ta.py GFS full` → 失敗  
  - `yf.py GFS fast_info` → 失敗

### 代理錯誤詳情
```
Failed to perform, curl: (56) CONNECT tunnel failed, response 403
Host: fc.yahoo.com:443
Reason: gateway answered 403 to CONNECT (policy denial or upstream failure)
```

## 無法進行分析之指標

下列技術指標無法計算：
- MACD、RSI14、Bollinger Bands
- 移動平均線（MA20, MA50, MA200）
- ATR14、成交量分析
- 支撐/阻力位
- 動能指標（1m/3m/6m/12m 報酬）
- 波動率分析

## 建議行動

1. 確認 Yahoo Finance 連線是否恢復
2. 檢查組織政策是否允許存取 fc.yahoo.com
3. 待網路連線恢復後重新執行分析

---

**報告日期**：2026-07-26  
**資料狀態**：不可用  
**MARKET REPORT COMPLETE**
