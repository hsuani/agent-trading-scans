# Sentiment — SPAI as of 2026-10-26

## Analyst consensus
3 buy / 0 hold / 0 sell（strongBuy 0、strongSell 0）。近三期（0m、-1m、-2m）分布完全相同，代表近兩個月無評等變動。

Recent moves：`recommendations` 工具回傳內容與 `rec_summary` 相同，未見可辨識的升評或降評事件。yf 來源無目標價 (target price) 資料。第三方頁面（Benzinga，日期僅標示 "Oct 8" 無年份）列出平均目標價 $10、報價約 $4.51，並標示最近一次 initiation 為 2025-11。此資料日期不明、無法驗證，權重低。

覆蓋家數僅 3 家且全數買進、近期無變動，較像樣本少與資料陳舊，不宜解讀為強共識。

## Retail social
- Reddit：無法取得。r/wallstreetbets 與 r/stocks 的 search.json 皆回傳 "unable to fetch from www.reddit.com"，兩來源 soft-fail。本次無 mention count、無 tilt 判定、無代表性討論串。
- StockTwits：無法取得。api.stocktwits.com 解析失敗 (ENOTFOUND)，soft-fail。
- X / 新聞 chatter（WebSearch，僅得過期或低品質內容）：
  - Investing.com 社群喊單（2026-05 至 08）：多頭喊單有人在 6 月底前虧損約 12% 至 36%，亦有少數喊單獲利逾 30%，整體分歧。
  - 2026-04 多篇近似頁面（疑似自動生成）描述股價區間盤整、無異常量、無公司新聞，權重低。
  - 第三方情緒頁面標示 short interest 約 3.9% 且上升（日期不明）。
- Buzz volume：無可靠樣本，無法與常態比較，不以高低描述。
- Themes：無可靠的散戶主題。可見的反覆訊號為空方部位上升與近期喊單損益分歧，證據強度低。

## Insider activity
Net 6mo（2026-04-26 至 2026-10-26）：公開市場買入 $0；公開市場賣出 $4.0M（1,000,000 股 × $4.00，已手算核對）。

| 日期 | 人員 | 職位 | 類型 | 股數 | 金額 (USD M) |
|---|---|---|---|---|---|
| 2026-09-09 | Erdberg Daniyel | CEO | Sale | 1,000,000 | 4.0 |
| 2026-05-01 | Mack Brian William | Officer | Stock Award（授予） | 300,000 | 0 |

窗口外參考：2026-04-01 COO Mathews Jarret Daniel 股權授予 20,000 股；CEO 於 2026-03 與 2025-12 有贈與 (Gift) 紀錄，皆非市場交易。

重點說明：
- 窗口內唯一的公開市場交易是 CEO 於 9 月賣出 1,000,000 股、約 $4.0M，為本期最明確的內部人訊號，偏空。持股形式為直接持有 (Ownership: D)。
- yf 工具未提供交易代碼與 10b5-1 計畫資訊，無法判斷此賣出是否屬預定計畫，需查閱 SEC Form 4 確認。
- 其餘紀錄為股權授予與贈與，不計入淨買賣。
- 窗口內無內部人公開市場買入。

## Ownership shifts
- insidersPercentHeld：45.5%（內部人持股比重高）
- institutionsPercentHeld：12.1%；institutionsFloatPercentHeld：22.1%；機構家數 31
- 交叉驗算：流通股約為 1 − 45.5% ≈ 54.5%，機構 12.1% ÷ 54.5% ≈ 22%，與工具回傳的 22.1% 一致。
- 工具僅提供單一時點快照，無時間序列，無法判定機構持股的增減趨勢。
- 內部人與機構合計約六成持股，流通籌碼相對集中，股價對少量交易的敏感度可能偏高。

## Net sentiment score
Composite：**neutral**（信心：低）

- 分析師面：偏多。3/3 買進，但樣本少、近兩月無變動、目標價不可驗證。
- 內部人面：偏空。窗口內僅 CEO 一筆 $4.0M 公開賣出，無買入。
- 散戶面：無法判定。Reddit 與 StockTwits 皆取得失敗，X 來源僅過期或低品質內容。
- 空方部位：第三方資料顯示上升（日期不明），偏空，但單一來源。

Divergence flag：無法判定（N/A）。散戶端無可靠資料，無法確認散戶傾向是否與分析師偏多相反。若日後 Reddit 或 StockTwits 可取得，應重跑本節。

## 資料缺口
- Reddit（2 個 subreddit）：WebFetch 被拒，無資料。
- StockTwits：DNS 解析失敗，無資料。
- yf 工具：Yahoo cookie 與 crumb 取得失敗（工具回報 ConnectionError），但各項資料皆有回傳，數值未見異常。
- 目標價與股價：yf 無提供；第三方數字日期不明，未採用為正式依據。
- 新聞：本次 WebSearch 未找到 2026-10 的公司新聞或公告。

SENTIMENT REPORT COMPLETE
