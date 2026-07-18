# 技術分析 — 3443.TW 截至 2026-07-18

## 資料狀態

**PRICE_DATA_UNAVAILABLE**

代理網關對數據源的連接被政策拒絕。無法從以下來源擷取行情數據：

- `ta.py snapshot` — 失敗 (curl: (56) CONNECT tunnel failed, response 403)
- `yf.py fast_info` — 失敗 (curl: (56) CONNECT tunnel failed, response 403)
- Yahoo Finance (fc.yahoo.com:443) — 連接被拒絕
- Taiwan Stock Exchange (mis.twse.com.tw:443) — 連接被拒絕

### 錯誤詳情

```
gateway answered 403 to CONNECT (policy denial or upstream failure)
```

系統嘗試從 Yahoo Finance 及台灣證券交易所取得 3443.TW (創意電子 / Global Unichip Corp) 的實時市場數據，但代理網關基於政策限制拒絕了連接。

## 技術分析無法進行

由於完整缺乏價格數據，無法執行以下分析：

- MA20 / MA50 / MA200 移動平均線
- RSI14 相對強度指數
- MACD 動量指標 與 signal line
- Bollinger Bands 布林帶
- 支撐位 / 阻力位 (S/R levels)
- 交易量確認
- 短期 / 中期 / 長期動量

## 後續行動

1. 驗證代理配置 (`/root/.ccr/README.md`)
2. 聯絡系統管理員解除對數據源的連接限制
3. 確認台灣股票數據供應商是否可用
4. 重新執行技術分析流程

---

**分析日期**: 2026-07-18  
**Ticker**: 3443.TW (Global Unichip Corp / 創意電子)  
**上市地**: TWSE (Taiwan Stock Exchange)  
**業務**: ASIC 設計服務

MARKET REPORT COMPLETE
