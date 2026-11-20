FINAL TRANSACTION PROPOSAL: **BUY**

# Final decision — EQIX as of 2026-11-21

## FINAL TRANSACTION PROPOSAL: **BUY**

## Verdict
MODIFY

（部位判定：EQIX 不在 `held_tickers.txt`，屬新倉，走 A 框架。）

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $987.79 – $996.00（限價分 2–3 筆；收盤跌破 $987.79 即取消未成交單） |
| Stop | $969.00（收盤確認制）；$931.20 為盤中硬出清線，觸及即全出 |
| Target 1 | $1066.51 |
| Target 2 | $1400.00（基本面情境上限，須待 2027-02-10 財報驗證，不計入近期風控） |
| Size | Small（0.5% NAV）；加碼上限 1.0% NAV |
| Horizon | 戰術 1–4 週（12/9 FOMC 為分水嶺）；論點驗證至 2027-02-10 |
| Conviction | L |
| R:R to T1 | 2.7（以 $995 進場、$969 出場計；若跳空至 $931.20 僅約 1.1） |

修改重點（相對 trade_proposal）：
- 加碼上限由 1.5% 降為 1.0%。
- 加碼條件：「收盤站回 $1018–$1028 均線帶且 MACD 金叉」或「12/9 FOMC 非鷹派」擇一成立，且只能在 12/9 之後執行。
- Stop 改收盤確認制，並加上 $931.20 硬出清線。
- 不採用 call spread 衛星倉位與利率避險：倉位太小，不成比例。
- 組合已持有 DLR、AMT，同屬利率敏感 REIT，其中 DLR 與 EQIX 同為資料中心。1.0% 上限即是為了控制這個因子集中度。

## Risk debate adjudication
- Aggressive's strongest point：$987.79–$996 是距停損最近、R:R 最佳的區間，等到 $1018 以上才動作是用更差的價格買同一個論點；$969 停損不應再收緊。
- Conservative's strongest point：2.7 的 R:R 假設停損一定在 $969 成交。FOMC 若跳空，實際虧損為每股 $64 而非 $26，不對稱優勢在尾部情境不成立；公司 TTM FCF -$1.66B、淨負債/EBITDA 5.7x，對利率高度敏感。
- Net：I weight neutral more here because 低信心來自三重疊加（AFFO 數據未經獨立驗證、死亡交叉、FOMC 二元事件），不是單一可避險的事件，所以不接受 aggressive 把首批加倍；但 conservative 要求的三條件同時成立實務上等於永不加碼，也與 investment_plan 的「多方小勝」結論矛盾。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 核心 AFFO/股成長 | 扣除一次性項目後維持雙位數 | Q3 YoY +18.4%，但含 atNorth 一次性 fee；數字來自新聞轉述，未經工具資料驗證 | 觀察中 |
| 估值與股利覆蓋 | P/AFFO 落在同業 20–30x 內；AFFO 派息率低於 60% | 約 22.8x；派息率約 46%（同樣依賴未驗證的 AFFO 指引） | 成立 |
| 預訂轉化為簽約營收 | 創紀錄預訂轉成 hyperscale 租約 | 預訂 $533M（+35% YoY）；xScale Hampton 租約未確認 | 觀察中 |
| 利率與再融資可承受 | 10Y 不突破 5.27%，利息保障倍數維持 4x 以上 | 10Y 約 5%，12 月升息機率約 80%（單一來源）；利息保障 4.05x；債務到期結構缺失 | 觀察中 |

## 論點失效條件
- 若 2027-02-10 Q4 財報顯示扣除一次性項目後核心 AFFO/股成長低於 8%，支柱一失效 → 出場，不等 Stop。
- 若 12/9 FOMC 升息、dot plot 顯示 2027 年續升、且 10Y 收盤突破 5.27% 三者同時成立，支柱四失效 → 出場；只成立其中一至兩項則不得加碼。
- 若任一季財報顯示含資本租賃淨負債/EBITDA 升破 6.0x，或利息保障倍數跌破 3.5x，支柱四失效 → 減碼一半。
- 若至 2027-02-10 財報仍未確認 Hampton 租約，且當季預訂 YoY 轉負，支柱三失效 → 減碼一半，取消 Target 2。

## Monitoring trigger
If 12/9 FOMC 前任一日收盤低於 $987.79 但仍高於 $969，或 10Y 收盤突破 5.15%，re-evaluate before stop is hit：取消未成交限價單，並重新檢視是否在 FOMC 前先行出場。

## Catalyst calendar
- 2026-12-09 — FOMC 利率決議與 dot plot
- 2027-02-10 — EQIX Q4 財報與 FY27 AFFO/股指引
- 2027 Q1 — Inference Exchange 上線
- TBD — xScale Hampton 租約簽署公告

FINAL DECISION COMPLETE
