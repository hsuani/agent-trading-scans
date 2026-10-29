# Sentiment — FANUY (Fanuc Corp ADR) as of 2026-10-30

注意事項：本報告以今日（2026-10-29）可取得的資料為準，DATE 設定為 2026-10-30 屬於未來日期，部分資料可能需於 10-30 後再更新。

資料來源狀態：
- yf 工具（Yahoo）：連線失敗（ConnectionError，無 cookie/crumb），回傳值可信度低，insider 回傳空陣列，無法視為「無內部人交易」。
- Reddit（r/stocks、r/wallstreetbets）：WebFetch 遭拒（無法存取 www.reddit.com），視為 soft-fail。
- StockTwits：api.stocktwits.com DNS 解析失敗，需在 session 網路設定中允許該網域後才能重試。
- WebSearch（新聞/評級聚合站）：有可用資料，但多為彙總網站，日期與數字不一致。

## Analyst consensus

覆蓋極薄，US 上市 ADR 僅約 1–2 位分析師有可比評級。
- yf rec_summary（當期 0m）：1 strong buy / 0 buy / 1 hold / 0 sell / 0 strong sell，即 2 家；前兩期（-1m、-2m）皆為 2 hold，評級未變動但也沒有 Sell。
- Investing.com（截至 2026-08）：2 家皆 Hold，平均 12 個月目標價約 US$21.72（高 22.81 / 低 20.63）。
- StockHub（2026-07-16 彙總）：Buy，目標價均值約 US$23.33（區間約 20.33–26.33），樣本僅 2 家，與 Investing 來源不一致。
- TipRanks：1 Buy + 數家 Hold，無平均目標價。
- Walnut（2026-07）：認為缺乏有意義的共識目標價。
- Seeking Alpha（2026-10-08）：Buy，理由為美國回流（reshoring）帶動工廠自動化與機器人需求。
- Zacks：Rank #2（Buy）。
- MarketBeat：資料多為 2025 年，不採用。

近期變動：未見 2026-10 內的明確上調或下調紀錄。共識傾向 Hold 至 Buy 之間，取決於來源，且樣本不足以視為可靠共識。

## Retail social

- Reddit：無法存取。WebSearch 也未找到 r/wallstreetbets 或 r/stocks 中關於 Fanuc/FANUY 的討論串，因此無法判斷 tilt。
- StockTwits / X：StockTwits 無法連線。X 與社群面未找到可用的近期討論。
- 整體聲量：以搜尋結果判斷屬低（qualitative，信心低）。多數曝光來自新聞、評級站與自動化的股價頁，而非散戶社群。
- 散戶傾向：無法判定（bullish / bearish 皆缺乏足夠樣本）。
- 主題（來自新聞面，非散戶貼文）：
  - 美國回流與機器人需求：FANUC America 規劃約 US$90M 的密西根（Rochester Hills）新廠，預計 2027 年啟用，約 225 個就業機會。
  - 北美機器人業務：Seeking Alpha 提到北美機器人部門銷售年增約 21%。
  - 財報：截至 2026-06-30 季度的銷售與淨利皆年增（聚合站數字：銷售約 ¥231,035 百萬，即約 2,310 億円；淨利約 ¥50,981 百萬，即約 510 億円）。需以公司公告核對。
  - 股價波動：ADR 52 週區間約 US$10.54–22.84，近期約 US$20.72（M1 頁面，延遲報價）。

## Insider activity

Net 6mo: 無法確認（yf 回傳空陣列，但因 Yahoo 連線失敗，不能推論為零交易）。
Notable: 無可用資料。
Note: Fanuc 為日本上市公司，內部人申報制度與 SEC Form 4 不同，即使有資料也需以 TSE 揭露為準。

## Ownership shifts

yf major_holders：institutionsCount 27；institutionsPercentHeld 約 0.23%；insidersPercentHeld 0.0%。
- 0.23% 的機構持股比例明顯不合理（應為計價或單位錯誤），判定為資料異常，不採用。
- 無法判斷機構集中度趨勢。

## 其他資料異常

- Digrin 的 FANUF（OTC 普通股線）顯示約 US$39.69，與 ADR 約 US$20 的價位不一致，兩者為不同證券或比例，不可混用。
- MarketBeat 的 short interest "days to cover" 267.27 明顯為資料錯誤，不採用。
- Yahoo 列出的下次財報日 2026-10-23 已過，但未找到該季結果的確認資料。

## Net sentiment score

Composite: **中性偏多（neutral-to-mildly-bullish），信心低**。
- 分析師面：Buy 與 Hold 混合，樣本 1–2 家，傾向略偏正面（Seeking Alpha Buy、Zacks Rank #2、yf 有 1 strong buy）。
- 新聞/基本面面：美國回流投資與北美機器人需求為正面主題，但來源為聚合站，缺乏原始公告核對。
- 散戶面：無資料，無法納入權重。
- 內部人面：無法判定。

Divergence flag: **無法判定**。散戶 tilt 缺乏樣本，無法與分析師 tilt 比較，因此不標記背離。

信心低的主要原因：分析師覆蓋過少、散戶來源全數失效（Reddit 遭拒、StockTwits DNS 失敗）、yf 內部人與持股資料異常。建議在 StockTwits 網域放行並修復 yf 連線後重跑本報告。

SENTIMENT REPORT COMPLETE
