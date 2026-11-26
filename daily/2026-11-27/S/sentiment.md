# Sentiment — S (SentinelOne) as of 2026-11-27

注意: 今天日期為 2026-11-26，2026-11-27 為指定的 as-of 日期，實際資料最新只到 11 月中旬，已於各節標註。

## Analyst consensus

資料來源: pipeline/tools/yf.py 的 rec_summary (cache 來源，屬預期)，Yahoo cookie 取得失敗但數值可用。

| 期間 | Strong Buy | Buy | Hold | Sell | Strong Sell | 合計 |
|---|---|---|---|---|---|---|
| 本月 (0m) | 3 | 15 | 16 | 0 | 0 | 34 |
| 1 個月前 | 3 | 15 | 15 | 0 | 1 | 34 |
| 2 個月前 | 3 | 16 | 15 | 0 | 0 | 34 |
| 3 個月前 | 3 | 18 | 14 | 0 | 0 | 35 |

目前為 18 買進 / 16 持有 / 0 賣出 (含 Strong Buy)。3 個月內買進家數由 21 降至 18，持有由 14 增至 16，沒有賣方評等。

Recent moves (WebSearch 結果，單一來源，未經 yf 驗證):
- Needham 維持 Buy，目標價 26 → 31 (2026-10-13)
- Baird 維持 Outperform 並上調目標 (2026-10-14，目標價數字未取得)
- Wedbush 維持 Outperform，目標價 25 → 27 (2026-10-22)
- Rosenblatt 目標價 25 → 28 (2026-10-23)
- Bernstein 降評，目標價 25 (2026-09-17)，與其他 Buy 評等並存，需再核對降評後評等
- 共識目標價: Benzinga 平均約 24 USD，區間 15 至 31 USD，共 33 位分析師; StreetInsider 平均約 23.98 USD，高 32 (Yorkville Ives)、低 14.50 (Goldman Sachs)。兩者日期為 2026-10 前後。
- 個別升降級的完整逐筆歷史: DATA_UNAVAILABLE (yf recommendations 工具只回傳家數，不含逐筆評等變動)

價格參考: Benzinga 報 2026-11-13 收盤 22.20 USD，另一來源有 11-06 收盤 21.41、11-11 收盤 23.78，數字不一致，視為約 22 USD 區間。

## Retail social

Reddit:
- 直接 Reddit JSON 在此沙箱無法存取，依指示改用 WebSearch。
- 搜尋未找到 2026 年 r/wallstreetbets 或 r/stocks 上近期的 S 相關討論串，逐篇樣本: DATA_UNAVAILABLE。
- AltIndex 估計 Reddit 提及量接近每日零，在同業中排名最後，情緒分數 72/100 (標示為中性)，方法論與日期不明，僅供參考。
- 2026-02 有一篇 r/Valueinvesting 的看多論點被 Finviz 轉述，屬於價值投資面的看多聲音。
- 整體 tilt: 無法判定，偏低關注度。

StockTwits / X:
- StockTwits 直接 API 在此沙箱無法存取，且搜尋未找到 2026-11 的情緒讀數: DATA_UNAVAILABLE。
- 歷史參考 (2026-03 前後): 財報指引後散戶情緒一度降至極度看空 (2/100)，另一篇則稱 Q1 營收優於預期後「散戶在買低」。標題如「Retail Mood Hits Rock Bottom」、「Retail Is Buying The Dip」反映該時期的分歧。這些皆為數月前資料，不代表現況。
- AltIndex 給予 100/100 的非常正面分數，方法論不明，權重極低。
- X: 未取得有效結果: DATA_UNAVAILABLE

Buzz volume: 相對典型水準偏低 (AltIndex 排名同業末位，屬定性判斷)。

Themes (依現有來源):
1. 內部人持續減持，與分析師偏多形成對比
2. ARR 突破 10 億 USD 的成長敘事，但股價一年報酬仍為負值 (Simply Wall St，日期不明)
3. 估值爭議: 深度價值派與成長懷疑派並存
4. CFO 異動的報導 (AOL 指 2026-01 CFO 離職)，但 Form 4 仍見 Sonalee Parekh 以 CFO 身份交易，需再核對
5. 下一次財報: Benzinga 列為 2026-12-03 (FQ3 FY27，EPS 預估 0.05 USD、營收預估 3.102 億 USD)，單一來源，尚待核實，屬近期催化劑

## Insider activity

資料區間: 2026-05-27 至 2026-11-27 (yf insider，數字為 USD)

Net 6mo: 公開市場賣出 31 筆、約 140 萬股、約 30.2 百萬 USD (30.19 USD M)；買進 0 筆、0 USD。另有董事於 2026-06-25 的股票獎勵 (無現金價值) 與 2026-04-15 的獎勵。
- 註: Quiver 報導 6 個月內 24 筆賣出，計數方式不同 (逐筆 vs 逐次)，本報告以 yf 逐筆為準。

按人員 (賣出金額 USD M):
| 人員 | 職位 | 賣出金額 (USD M) |
|---|---|---|
| Tomer Weingarten | CEO | 23.04 |
| Sonalee Parekh Elizabeth | CFO | 2.57 |
| Keenan Michael Conder | Officer | 1.39 |
| Robin Tomasello | Officer | 1.17 |
| Barry L. Padgett | President | 1.07 |
| Ana G. Pinczuk | Officer and Director | 0.95 |

Notable:
- CEO Weingarten 2026-10-05 以 9.74 USD 行權 500,000 股，同日以約 25.26 USD 賣出 527,368 股 (約 1,332 萬 USD)，屬行權後賣出。
- 2026-05 至 2026-11 的賣出多集中在每月 1 日至 11 日 (如 5/6、6/8、7/1、8/6、9/8-11、10/5-6、11/6-9)，有明顯固定時程特徵。推論可能是預定交易計畫 (10b5-1)，但未經 Form 4 附註確認，標為推論。
- 買進: 無，DATA_UNAVAILABLE 以外無其他內部人買進紀錄。

## Ownership shifts

- 機構持股 88.7%，機構數 678 家 (yf major_holders 快照)
- 內部人持股 0.9%
- 歷史機構持股趨勢: DATA_UNAVAILABLE (只有單一快照，無法判斷增減)

## Net sentiment score

- 分析師面: 偏多 (18 買 / 16 持有 / 0 賣，目標價均值高於近期價格約 22 USD，信心中)
- 內部人面: 偏空 (6 個月約 30 百萬 USD 賣出、0 買進，但多為規律性且可能為預定交易，信心中低)
- 散戶面: DATA_UNAVAILABLE (Reddit、StockTwits 近期讀數皆無法取得，僅有低關注度與歷史分歧的間接證據)

綜合: 中性 (信心: 低)。分析師偏多與內部人減持互相抵消，散戶面缺乏近期資料，無法給出可靠的方向判斷。

Divergence flag: 是 (分析師偏多 vs 內部人偏空)。與散戶的分歧: DATA_UNAVAILABLE，無法判定。

限制與缺漏:
- 資料最新僅到 2026-11-13 左右，非 as-of 11-27 的當日資料
- Reddit、StockTwits、X 近期讀數均無法取得
- 逐筆評等變動與目標價調整的完整歷史無法取得
- 本報告不含交易建議
