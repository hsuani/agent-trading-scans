# Sentiment — APD (Air Products & Chemicals) as of 2026-11-27

資料說明：yf 工具走 cache fallback（Yahoo cookie/crumb 連線失敗，屬預期情況），analyst 與 insider 數值為快取值，個別快照日期無法逐筆確認。Reddit / StockTwits 直連主機在本沙箱被封鎖，改以 WebSearch 取得間接資料。金額單位為 USD，以 M（百萬）表示。

## Analyst consensus

| 項目 | 數值（analysts 數） | 說明 |
|---|---|---|
| Strong Buy | 4 | 3 個月前為 3 |
| Buy | 11 | 3 個月內持平 |
| Hold | 9 | 3 個月前為 7，3 個月內增加 2 |
| Sell / Strong Sell | 0 / 0 | 全期間皆為 0 |
| 合計 | 24 | 偏多 15 / 持有 9 / 偏空 0 |

- 評等結構：多方評等佔比約 63%（15/24），無任何賣出評等。近 3 個月的變化主要是 Hold 增加，Buy 與 Strong Buy 大致持平，屬於「偏多但保守化」的軌跡。
- 近期評等動作（WebSearch 取得，日期多數無法確認）：
  - Barclays 初始覆蓋 Overweight，目標價 $353（聚合站點所載，日期為 2026-10-13，單一來源）。
  - Morgan Stanley 與 UBS 維持 Hold（Morgan Stanley 於 2026-05-05 目標價由 $290 調至 $310，來源為聚合站）。
  - JPMorgan 升評至 Overweight，目標價 $310（由 $280 調升，理由為氦氣價格回升，日期未知）。
  - BofA 降評至 Neutral，目標價 $350（日期未知）。
  - Wells Fargo 於 2025-12-19 降評至 Equal Weight，目標價 $250（屬 2025 年資料，已過時，不納入當前判斷）。
- 目標價：多個聚合站顯示 2026-11 平均目標價約 $334–336（來源未統一，屬估算值）。Simply Wall St 於 2026-09 所載共識目標價 $345.11。
- 股價參照：2026-11-13 收盤約 $316.20；2026-11-08 約 $304.84（聚合站）。
- 升降評歷史（`recommendations` 欄位）：工具只回傳計數變化，無個別升降評明細，逐筆升降評 DATA_UNAVAILABLE。

## Retail social

- Reddit（r/wallstreetbets、r/stocks）：WebSearch 未找到 2026 年 APD 相關討論串。WSB 提及次數趨勢來自 MarketBeat 頁面，但摘要中無具體數字。整體情緒傾向 DATA_UNAVAILABLE。
- StockTwits：直連被封鎖，WebSearch 找不到 2026 年 $APD 訊息流，無法判斷多空比例。DATA_UNAVAILABLE。
- X / 社群聚合：LunarCrush 頁面顯示近 24 小時僅 1 則提及 $APD（含 Reddit、X、YouTube 合計），聲量極低。
- 空單（聚合站）：MarketBeat 顯示 short interest 約 6.21M 股，月增約 16%（日期未明）。Benzinga 另列 short float 約 1.9%（2026-09 快照）。兩者口徑與日期不一致，只能視為參考。
- 情緒分析工具：TipRanks AI 模型標示 APD 情緒為 negative（日期未明，來源為聚合站摘要）。此為機器模型結果，非散戶實際發言。
- 主題（可得資料有限）：
  - 氫能與 helium（氦氣）價格循環，是分析師討論的核心變數。
  - 2026 年 Q3 調整後 EPS $3.47 優於預期 $3.34（Trefis 摘要，屬 fiscal Q3 2026）；Q4 2026 財報於 2026-11-05 發布，據稱再度超預期（單一來源，需再確認）。
  - 估值面：Simply Wall St 估計低估約 12%，屬被動的估值討論。
- 散戶傾向：DATA_UNAVAILABLE（缺乏可引用的散戶原文，聲量低，無法做有效的多空判斷）。
- 代表性引文：無（未取得可驗證的散戶原文，故不引用）。

## Insider activity

以 2026-05-27 至 2026-11-27 為 6 個月窗口：

- 買入：$0.00M（0 筆公開市場買入）
- 賣出：$0.14M（1 筆）
- 淨額：約 -$0.14M（小額、偏賣）

窗口內唯一交易：
- 2026-11-16，Kurt Lefevere（Officer），賣出 450 股，約 $0.14M（價格 $316.86）。

窗口外但仍值得注意的交易（參考背景，非 6 個月內）：
- 2026-05-01，CFO Melissa Schaeffer 賣出 2,714 股，約 $0.82M（$303.76）。
- 2026-02-12，Mantle Ridge, L.P.（10% 以上大股東）賣出 70,175 股，約 $19.94M（$284.21）。另有一筆 1,759 股的贈與（非交易）。
- 2025-12 起，多名高階主管有大量股票獎勵（Grant），屬薪酬性質，非市場買入。CEO Eduardo Menezes 於 2025-12-01 獲配 17,376 股獎勵。

判讀：窗口內內部人以小額賣出為主，沒有公開市場買入。大額賣出（Mantle Ridge）發生於窗口之外。獎勵型股票不應解讀為看多或看空訊號。

## Ownership shifts

- 內部人持股：約 1.9%。
- 機構持股：約 94.5%（float 口徑約 96.3%），機構數 2,246 家。
- 持股集中度趨勢：工具僅提供單一時點快照，無法判斷近季的增減。趨勢 DATA_UNAVAILABLE。
- 大股東：Mantle Ridge 於 2026-02 有大額減持（見上節）。目前持有量無法從資料確認。

## Net sentiment score

- 分析師面：偏多（bullish），信心中等。15/24 為 Buy 以上，0 賣出，但 Hold 近 3 個月增加，語氣轉趨保守。
- 內部人面：輕微偏空，信心低。窗口內僅 $0.14M 賣出，屬小額、單筆。
- 散戶面：無法判定（DATA_UNAVAILABLE）。聲量極低（24 小時 1 則），無法形成可靠的散戶傾向。
- 機器情緒（TipRanks AI）：negative，但來源與日期不明，權重低。

**綜合：偏多（bullish），信心低至中等。** 主要依據為分析師結構（無賣出、Buy 佔多數）。散戶面資料不足，不能支撐更強的結論。

Divergence flag：無法判定。散戶傾向 DATA_UNAVAILABLE，因此無法判斷是否與分析師傾向相反。分析師面與內部人面方向基本一致（偏多，內部人小幅賣出但金額很小）。

## 未取得資料（DATA_UNAVAILABLE）

- Reddit r/wallstreetbets、r/stocks 的 2026 年 APD 原文與多空比例。
- StockTwits 訊息流與多空比例（直連被封鎖，WebSearch 未取得）。
- 個別升降評日期與完整明細（`recommendations` 僅有計數）。
- 機構持股的時序變化（僅單一快照）。
- 2026-11 的正式 target price 共識（聚合站數字不一致，僅供參考）。

SENTIMENT REPORT COMPLETE
