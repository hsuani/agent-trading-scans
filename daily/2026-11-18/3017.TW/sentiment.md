# Sentiment — 3017.TW (奇鋐 Asia Vital Components) as of 2026-11-18

資料說明：yfinance 即時抓取失敗（fc.yahoo.com 連線錯誤），以下 yf 數據取自 repo cache（`prices/yf/3017.TW.json`，refreshed 2026-11-17 15:52 UTC）。Reddit 與 StockTwits 無法存取，列為 DATA_UNAVAILABLE。

## Analyst consensus

18 位分析師：6 strongBuy / 12 buy / 0 hold / 0 sell，共識 `strong_buy`。

| 期間 | strongBuy | buy | hold | sell | strongSell |
|---|---|---|---|---|---|
| 本月（0m） | 6 | 12 | 0 | 0 | 0 |
| 前一月（-1m） | 6 | 11 | 0 | 0 | 0 |
| 前兩月（-2m） | 6 | 11 | 0 | 0 | 0 |
| 前三月（-3m） | 6 | 11 | 0 | 0 | 0 |

- 近期動向：買進家數由 11 增至 12，其餘不變；全部 18 家維持買進或以上，無降評紀錄。
- 目標價（cache info，TWD）：平均 4,181、最高 5,200、最低 3,200。以 cache 收盤價 2,470 計，平均目標價隱含上行約 +69%。
- 個別升降評與目標價變動明細：DATA_UNAVAILABLE（yf 僅提供彙總家數）。
- 外部搜尋到的個別券商數字不一致，未採用：Nomura 目標價 4,000（2026-08）、UBS 初始買進目標 2,000（日期不明）、某法人目標價 3,690（2026-06，工商時報報導）。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：DATA_UNAVAILABLE（reddit.com 無法抓取）。
- StockTwits：DATA_UNAVAILABLE（api.stocktwits.com 無法解析，需在 session 網路設定中允許該網域）。
- X / 論壇：WebSearch 未找到 PTT、Dcard 的股友討論串，結果以新聞與分析文章為主。無法量化討論量，零售情緒傾向無法判定。
- 新聞端語氣偏正面：法說會後媒體以「ASIC 營收超越 GPU」「水冷採用率 100%」等正面論述為主。這是媒體敘事，不等於散戶情緒。
- Themes（取自新聞與法說內容，非散戶貼文）：
  - 2027 年 ASIC 營收貢獻將超越 GPU，CSP 自研晶片帶動水冷需求。
  - 水冷採用率預估 2027 年底達 100%，供給仍不足。
  - 第三季毛利率 33.86%（第二季 32.57%），銅等原料成本可轉嫁。
  - 擴產與資本支出：2026 年約 150 億，2027 年 150 至 200 億，以越南擴廠為主。
  - 估值疑慮：外部來源提到本益比約 41.7 倍，高於 Quanta 與 Wistron（數據來源未確認時點）。

## Insider activity

Net 6mo：DATA_UNAVAILABLE。`insider` 工具在即時與 cache 皆回傳空陣列，無法區分「無申報交易」與「來源未覆蓋」。台灣內部人持股申報應以公開資訊觀測站為準，本次未取得。
Notable：無。

## Ownership shifts

- 內部人持股比例：17.27%（yf major_holders）。
- 機構持股比例：44.18%；佔流通股比例：53.40%；機構家數：362。
- 單季趨勢：無歷史對照，無法判定集中度變化方向。
- inst_holders 僅列一筆（Stanley-Laman Group, Ltd.，2026-09-30 申報，17,700 股，pctChange +38.3%），不足以代表整體機構動向。

## Net sentiment score

- 分析師面：bullish，信心高（18 家全數買進以上，無賣出評等）。
- 零售面：DATA_UNAVAILABLE，無法判定。
- 內部人面：DATA_UNAVAILABLE。
- Composite：**bullish（信心：中低）**。僅分析師面有可用資料，零售與內部人資料缺失，因此綜合分數主要來自分析師共識。

Divergence flag：**無法判定（no）**。零售傾向資料缺失，無法與分析師傾向比較。

### 資料一致性注意事項

- 股價未對齊：cache 收盤價 2,470 TWD（2026-11-17 refresh）；一則 MONEY LINK 頁面快照顯示盤中 3,050 TWD（標示 2026-11-13，但其法人買賣超表停在 2025-09，可信度低）；英文搜尋摘要提到 2,310 TWD（未標日期）。三者差距大，本報告以 cache 2,470 為準，需以即時報價核對。
- 財務數字交叉核對通過：
  - 市值 9,698.9 億 TWD（`marketCap` 969,894,920,192 ÷ 1e8），價格 2,470 TWD，反推股本約 3.93 億股。
  - 第三季 EPS 29.32 × 3.93 億股 ≈ 115.1 億 TWD 稅後純益。
  - 前三季 EPS 73.86 × 3.93 億股 ≈ 290.4 億 TWD，與新聞所載「前三季稅後純益 290.47 億」吻合。
- 第三季財報於 2026-11-10 公告，EPS 實際 29.32 vs 預估 28.01（+4.66%）。2026 年前三季 EPS 公告值皆高於預估（Q1 +4.75%、Q2 +6.84%、Q3 +4.66%）。

資料來源：
- yf cache：`prices/yf/3017.TW.json`（refreshed 2026-11-17 15:52 UTC）
- WebSearch：[uanalyze 法說會整理](https://uanalyze.com.tw/articles/9857458877)、[自由時報法說報導](https://ec.ltn.com.tw/article/breakingnews/5636154)、[uanalyze ASIC 營收分析](https://uanalyze.com.tw/articles/9896958909)

SENTIMENT REPORT COMPLETE
