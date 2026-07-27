# 基礎分析 — QUBT 截至 2026-07-28

## FUNDAMENTALS_DATA_UNAVAILABLE

### 數據檢索失敗

**狀態**: 無法獲取財務數據

**原因**: 代理層級限制
- Yahoo Finance API 連接遭 403 策略拒絕
- fc.yahoo.com:443 連接被網關攔截
- yfinance 工具無法訪問後端數據源

**影響的數據點**:
- 年度財務報表 (income statement, balance sheet, cashflow)
- 季度財務報表
- 實時股價與移動平均線
- 公司基本信息 (P/E, 市值, 部門分類)
- 內部人士交易活動
- 機構持倉

### 市場背景 (已知信息)

**公司概況**: QUBT 是光子量子計算公司，專注於:
- 儲水池計算 (Reservoir Computing) / 光子退火 (Photonic Annealing) 產品
- 政府合約 (NASA, USAF)
- 盈利前階段

**分析視角**: 會議焦點應為
- 收入成長率同比 (目標 >15%)
- 現金燃燒率 / FCF / 現金跑道
- 前進型 EV/Revenue 或 P/S

### 下一步建議

1. 檢查代理政策例外清單，確認是否可以授予 fc.yahoo.com 訪問權限
2. 嘗試使用替代數據源 (如果可用)
3. 等待代理策略更新

---

**報告生成時間**: 2026-07-28  
**數據狀態**: FUNDAMENTALS_DATA_UNAVAILABLE  
**分析狀態**: 無法進行

