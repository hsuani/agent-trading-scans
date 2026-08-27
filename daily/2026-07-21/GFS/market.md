# 技術分析 — GFS (GlobalFoundries) 截至 2026-07-21

## 數據狀態

**PRICE_DATA_UNAVAILABLE**

無法取得 GFS 股價數據。API 呼叫返回 HTTP 403 錯誤，表示代理連線失敗。yfiance 資料源無法聯繫。

### 錯誤詳情
- 快照 (snapshot) 工具：Failed to perform, curl: (56) CONNECT tunnel failed, response 403
- 快速資訊 (fast_info) 工具：Failed to perform, curl: (56) CONNECT tunnel failed, response 403
- 狀態：GFS 可能已下市或股票代碼不再有效

## 技術分析無法進行

由於缺少價格數據，無法提供以下分析：
- 即時股價與移動平均線 (MA20/MA50/MA200) 比較
- RSI14、MACD、布林帶等技術指標
- 支撐與阻力位
- 波動率分析
- 趨勢與動量評估

## 建議後續步驟

1. 驗證股票代碼是否正確 (GFS - GlobalFoundries Inc.)
2. 確認 GFS 是否仍在 NASDAQ 上市
3. 檢查網路連線與代理設定 (/root/.ccr/README.md)
4. 重新嘗試數據取得

---

**報告生成時間**：2026-07-21
**數據來源**：pipeline/tools/ta.py, pipeline/tools/yf.py
**狀態**：資料不可用
