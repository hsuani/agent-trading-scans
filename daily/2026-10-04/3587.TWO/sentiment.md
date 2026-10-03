# 情緒分析 — 3587.TWO (閎康) 截至 2026-10-04

## 分析師共識
**DATA_UNAVAILABLE** — Yahoo Finance 推薦資料無法取得。yf.py 推薦與目標價歷史記錄查詢返回空陣列（API 連線失敗）。

## 零售社群聲量與傾向
**DATA_UNAVAILABLE** — 社群平台存取受阻：
- Reddit (r/wallstreetbets, r/stocks)：Claude Code 無法存取
- StockTwits API：代理伺服器封鎖 (EGRESS_BLOCKED)
- 網路新聞情緒搜尋：本 session WebSearch 預算已耗盡 (200/200)

## 內部人交易活動
**DATA_UNAVAILABLE** — 過去 6 個月內部人買賣淨額與具體交易詳情無法取得。yf.py insider 查詢返回空陣列。

## 所有權結構與集中度
依 yf.py major_holders 回傳（截至最新可得日期）：

| 持股類別 | 比例 |
|---------|------|
| 內部人持股比例 | 28.13% |
| 機構持股比例 | 8.84% |
| 機構持股（佔流通股） | 12.30% |
| 機構數量 | 16 家 |

**觀察**：內部人持股比例相對較高（28.13%），表明創始人/高管對公司有顯著信心與利益掛鉤。機構參與度溫和（8.84%），在全球光子芯片與台灣科技股中屬中低水位。

## 綜合情緒評分

**方向**：無法判斷（insufficient data）  
**信心度**：低 — 缺乏分析師評等、社群聲量、近期交易信號  
**牛熊分歧旗標**：無法評估

## 資料限制說明

本報告受制於以下取得限制：
1. **Yahoo Finance API 故障** — 推薦歷史、分析師目標價、內部人交易文件下載受連線問題影響
2. **社群平台封鎖** — Reddit、StockTwits 無法透過 Claude 直接存取
3. **搜尋預算用盡** — WebSearch session 額度已滿，無法進行補充新聞情緒掃描

## 建議後續動作

- 手動查閱：閎康 IR 網站、Taiwan Stock Exchange (TPEX) 公告、近期法人說明會紀錄
- 驗證內部人持股 28.13% 現況（可能已變動）
- 掃描光子芯片產業動向（5G、AI 晶片需求信號）

---

**SENTIMENT REPORT COMPLETE**

報告成生時間：2026-10-04  
數據時間基準：如API可得日期  
撰寫者：Shane (sentiment-analyst pipeline)
