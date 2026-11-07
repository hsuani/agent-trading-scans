# Sentiment — 4908.TWO 前鼎光電 as of 2026-11-08

資料完整度：低。本次 yf 的 recommendations、rec_summary、insider 皆回傳空陣列（即時來源被擋，repo cache `prices/yf/4908.TWO.json` 內對應欄位也是空的），只有 major_holders 可用。Reddit、StockTwits 無法連線。WebSearch 找到的社群內容多為舊文或無日期摘要，且最新可查到的股價停在 2026-10 下旬，11 月行情未取得。下列結論可信度低。

## 資料取得狀況

| 來源 | 狀態 | 說明 |
|------|------|------|
| yf recommendations / rec_summary | 失敗（空陣列） | Yahoo cookie/crumb 失敗，cache 內也是空值 |
| yf insider | 失敗（空陣列） | 同上 |
| yf major_holders | 成功 | 見「Ownership」 |
| Reddit r/wallstreetbets、r/stocks | 未取得 | 依任務指示改用 WebSearch，本次未對 Reddit 直接抓取 |
| StockTwits | 未取得 | 本沙箱無法連線 |
| WebSearch（中文、英文） | 部分取得 | 找到 CMoney 討論區摘要、PTT 舊標題、法人評價與注意股報導，多數無精確日期 |

## Analyst consensus

0 buy / 0 hold / 0 sell（本次無資料，不代表無評等）。

- 無法取得 buy/hold/sell 分布，也無近期升降評或目標價變動。
- WebSearch 找到一篇財經週刊引述的法人預估：今年 EPS 2.94 元、明年 EPS 4.40 元。報導未標日期，券商與發布日期無法確認，僅作參考。
- 2026-06-24 與 2026-07-21 的既有報告也記載：Yahoo Finance 及主流國際券商對本股無專業分析師覆蓋，台灣本地平台亦無官方目標價統計。

## Retail social

- Reddit：未取得。既有 2026-06-24 報告指出 wallstreetbets 與 stocks 幾乎沒有 4908 討論，本次不能更新。
- StockTwits / X：未取得 StockTwits。WebSearch 未找到 X 上 11 月的相關討論。
- PTT 與 CMoney：搜尋到 PTT 股票板的舊文標題（約 2023 年，不能代表現況）。CMoney「股市爆料同學會」有一段無日期的社群摘要，整理為：
  - 偏空一方認為缺乏主力支撐、股價走弱、籌碼面不佳，短線可能震盪。
  - 偏多一方認為 213 元以上有買盤承接，態度樂觀。
  - 有傳聞公司轉型、不做光通訊，市場反應偏負面。
  - 討論區發言品質也有爭議。
- 聲量：無法量化。WebSearch 結果顯示 4908 在 2026 年 4 月、6 月、9 月多次被櫃買中心列為注意股，媒體報導頻率高於一般小型上櫃股，但這是新聞曝光，不等於社群討論量。
- 本次無 11 月的社群文章可引用。

## Themes（沿用與本次搜尋交叉比對）

- 看多主軸：CPO 與外置光源（ELS/ELSP）切入進度、800G/1.6T 交換機應用、自建 Chip on Carrier 產線（公司預計 2026 年第三季完工）。
- 獲利回升：2026 年 1 至 8 月營收累計 7.17 億元、年增 28.29%；7 月自結單月獲利 2,400 萬元、年增 140%。
- 看空主軸：本益比過高（9 月初約 91 倍，6 月中約 107 倍）、短期漲幅過大觸發注意股、400G 仍在送樣、2025 年營收微幅衰退、股價大起大落（5 月高點約 267 元，7 月約 138 元，10 月約 200 元）。
- 籌碼：WebSearch 轉引的外資買超報導（時間不一）顯示外資曾連續買超；另有 10 月 Goodinfo 頁面列出外資當日賣超。方向在不同時段反覆，無法判定近期趨勢。

## Insider activity

Net 6mo: 無法計算（yf insider 空陣列，無內部人申報明細）。

既有資料（需注意日期，非本次取得）：
- 2026-06-24 報告：董監持股約 13.14%，無質押紀錄。
- 2026-07-21 報告：未見董監或內部人明顯大額買進或賣出。董事長葉政彥、總經理李昌祐。2026 年 5 月決議 2025 年度現金股利每股 1.00 元。

本次無法判斷 6 個月內 CEO / CFO 的買賣方向。建議查公開資訊觀測站的董監持股申報。

## Ownership

yf major_holders（本次可取得）：
- insidersPercentHeld：44.18%
- institutionsPercentHeld：0.90%（float 口徑 1.62%）
- institutionsCount：5

解讀與限制：Yahoo 的 insider 比例 44.18% 明顯高於既有報告的董監持股約 13%，兩者定義不同，可能把大股東或關係人合併計入，不宜直接採用。機構持股比例極低，符合上櫃小型股特徵。本次無機構持股變化的時間序列，無法判定集中度趨勢。

## Net sentiment score

綜合：中性（neutral），信心低。

- 正面訊號：營收與單月獲利年增幅高（約 28% 至 140%）、CPO 題材與外資買超報導、法人預估 EPS 上修空間。
- 負面訊號：本益比高、多次注意股處置風險、股價在 2026 年多次大幅回檔、社群內部意見分裂且偏謹慎。
- 缺口：analyst 與 insider 本期皆無資料，Reddit 與 StockTwits 未取得，11 月行情缺失，無法確認最新趨勢。

Divergence flag: 無法判定。缺少本期 analyst 評等與零售情緒的可比資料，不能確認兩者是否反向。

## 建議後續補充
1. 確認 Yahoo 即時資料可用後，補抓 recommendations、rec_summary、insider。
2. 改用台灣來源補 analyst 與 insider：鉅亨網研究評等、MoneyDJ、公開資訊觀測站的董監持股申報。
3. 取得 2026-11 的股價與櫃買中心注意股、處置股公告，確認最新市場狀態。
4. 在 session 網路設定中允許 Reddit 與 StockTwits 存取，或以 WebSearch 補 PTT 近期討論。

SENTIMENT REPORT COMPLETE
