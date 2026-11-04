# Sentiment — 1815.TWO (富喬工業) as of 2026-11-05

> 資料時效聲明: 本報告以 2026-11-05 為 as-of 日期, 但執行當下系統日期為 2026-11-04。可取得的最新市場資料約止於 2026-10-27 (外資買賣超) 與 2026-10-21 (股價); 2026-10-28 至 2026-11-05 之間的資料未取得。以下結論須視為 10 月下旬的快照。

## Analyst consensus

- 投資評等分布 (yf `rec_summary` / `recommendations`): DATA_UNAVAILABLE。yf 回傳全部為 0 (strongBuy/buy/hold/sell/strongSell 皆為 0), 且當次 Yahoo cookie/crumb 取得失敗, 無法判斷是「無券商覆蓋」還是「資料抓取失敗」, 因此不視為真實零評等。
- 券商目標價與評等變動: DATA_UNAVAILABLE。WebSearch 未找到任何券商的目標價或評等公告; 搜尋結果僅有股價與營收頁面。
- 近期外資動向 (非評等, 但為法人情緒代理指標): Goodinfo 頁面顯示 10/27 外資買進 22,520 張、賣出 27,397 張, 買賣超 -4,878 張, 連續 4 日賣超。另一則 Yahoo 股市頁面顯示 2026/01/19 外資買超 15,197 張, 代表年初曾為連續買超。兩筆皆來自搜尋摘要, 未逐頁核實。
- 結論: 無法給出 buy/hold/sell 分布。法人情緒僅能以外資買賣超方向代理, 且近期偏向賣超。

## Retail social

- Reddit (r/stocks, r/wallstreetbets): 沙箱封鎖, WebFetch 回傳 "unable to fetch from www.reddit.com", 未重試。標記 DATA_UNAVAILABLE。
- StockTwits: DNS 解析失敗 (api.stocktwits.com 不在允許網域內), 未重試。標記 DATA_UNAVAILABLE。若要啟用, 需在 session 網路設定中允許 api.stocktwits.com。
- 聲量 (buzz volume): DATA_UNAVAILABLE, 無法與歷史基準比較。
- X / 新聞與論壇 (WebSearch 替代): 僅有 CMoney 投資論壇彙整頁 (無日期, 使用者生成內容, 證據力弱), 其中部分發言者表示有法人買盤支撐, 另一部分則「對股價後市保持謹慎」, 認為再跌幅度難以預測。整體屬於 **多空分歧、偏保守**。
- 樣本量過小 (僅 1 個論壇頁與數則新聞摘要), 不足以量化 retail tilt 的強度。

## Retail tilt 與主要主題

- Retail tilt: 混合偏保守 (mixed-to-cautious), 信心低。
- 主要主題 (依可取得的來源整理):
  1. 基本面成長: 營收高速成長。histock 財務報表摘要顯示 2026/06 合併營收約 6.89 億, 年增 46.4%, 1 至 6 月累計年增 43%。StatementDog 摘要顯示 9 月營收年增 82.14%。
  2. AI 基礎建設題材: 公司表示 AI 資本支出增加帶動高階玻纖布需求, 先進製程產品產能比重預期提升至 60% 以上 (時報旺得富, 2026/02)。
  3. 估值: Yahoo 技術分析頁顯示本益比約 38.6, 同業平均約 92.9, 估值相對同業偏低。StatementDog 另列 10/21 本益比約 44.7。
  4. 股價走弱與法人賣超: 10/21 收 147 元, 10/27 收 131 元 (跌幅約 11%), 外資連賣 4 日。論壇發言多集中於「是否還會再破前低」。
- 代表性論壇意見 (摘錄, ≤15 字): 「部分同學對股價後市保持謹慎」 (CMoney 論壇彙整)。

## Insider activity

Net 6mo: DATA_UNAVAILABLE (金額)。
- yf `insider` 回傳空陣列, 無法判斷是否真的沒有內部人交易, 或資料源失敗。
- 唯一可見的申報紀錄 (Yahoo 內部人交易頁摘要): 2026/01/12, 董事長張元賓以信託方式申報 441 張 (董事 (信託)), 另有多位經理人與董事同日申報。僅能確認股數 (441 張 ≈ 441,000 股), 無成交價, 無法換算 TWD 金額。
- 2026 年股東會 (06/23) 後之董監持股變動申報: 未找到, DATA_UNAVAILABLE。
- 方向判定: 無法確定。唯一可見紀錄為買進或申報持有 (信託) 類型, 不宜解讀為淨買進。

## Ownership shifts

- yf `major_holders` (單一快照, 無時間序列):
  - 內部人持股 (insidersPercentHeld): 23.94%
  - 機構持股 (institutionsPercentHeld): 10.31%
  - 機構持股占流通股比 (institutionsFloatPercentHeld): 13.56%
  - 機構數量 (institutionsCount): 22
- 趨勢 (近 2-4 季機構持股變化): DATA_UNAVAILABLE。機構持股比率偏低, 內部人持股比率高, 籌碼集中於大股東。
- 注意: 該快照來自 yf, 且當次 cookie 取得失敗, 數值可能非最新。

## Net sentiment score

- Analyst 面: DATA_UNAVAILABLE (無評等分布); 法人買賣超方向為偏空 (近 4 日連續賣超)。
- Retail 面: 混合偏保守 (低樣本)。
- 基本面與估值面 (非情緒, 僅作背景): 營收成長強、估值低於同業, 與股價近期走弱形成反差。
- Composite: **偏空 (bearish-leaning neutral), 信心低 (low)**。主要依據為 10 月下旬外資連續賣超與股價回檔, 而非分析師或零售共識。缺少 Reddit, StockTwits, 券商評等與內部人金額等核心來源, 信心不足以支撐強烈判斷。
- Divergence flag: **無法判定 (DATA_UNAVAILABLE)**。因缺少券商評等分布, 無法比較 retail tilt 與 analyst tilt 是否反向。若之後取得券商評等, 且其偏多而論壇偏空, 應標記為 divergence。

## 資料來源狀態

| 來源 | 狀態 | 備註 |
|---|---|---|
| yf recommendations / rec_summary | DATA_UNAVAILABLE | 全部回傳 0, cookie/crumb 失敗 |
| yf insider | DATA_UNAVAILABLE | 空陣列 |
| yf major_holders | 可用 (快照) | 無時間序列, 可能非最新 |
| Reddit r/stocks, r/wallstreetbets | DATA_UNAVAILABLE | 沙箱封鎖 (WebFetch 錯誤) |
| StockTwits | DATA_UNAVAILABLE | DNS 解析失敗, 需允許網域 |
| WebSearch 新聞與論壇 | 部分可用 | 多為 2026 年 7 月至 10 月摘要, 未逐頁核實 |
| 券商目標價 / 評等 | DATA_UNAVAILABLE | 搜尋未找到, 建議查 MoneyDJ, 鉅亨網, CMoney 法人評等頁 |
| 內部人金額 (6 個月) | DATA_UNAVAILABLE | 僅見 2026/01/12 股數紀錄, 無金額 |

## 建議後續查證 (不構成交易建議)

- 公開資訊觀測站 (MOPS) 查詢 2026 年股東會後董監持股變動申報, 以及 2026 Q3 合併財報 (預計 11 月前後公告)。
- 查詢 MoneyDJ / 鉅亨網「法人評等」頁, 取得券商目標價與評等分布。
- 補抓 2026-10-28 至 2026-11-05 的外資買賣超與股價, 確認 10 月下旬的賣壓是否延續。

SENTIMENT REPORT COMPLETE
