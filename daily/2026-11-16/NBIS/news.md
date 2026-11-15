# News — NBIS as of 2026-11-16

注意事項（先看）:
- `pipeline/tools/yf NBIS news` 失敗（代理 403，CONNECT tunnel failed），本報告的新聞來源全部來自 WebSearch 摘要。`pipeline/tools/yf NBIS info` 可用，但 info 的價格是 2026-11-13 收盤快照（cache 時間 2026-11-15），不是 11-16 盤中價。
- WebFetch 無法解析 www.cnbc.com 與 www.sec.gov（網域不可達），CNBC 與 SEC 6-K 的數字只來自搜尋摘要，未逐字核對。
- 讀取 /root/.ccr/README.md 的動作被權限分類器拒絕，代理狀態未檢查。
- 不採用過去 daily/ 報告的任何數字。

## Top company-specific headlines (last 14d)
- 2026-11-12 — Q3 2026 財報（BMO）: 營收 $0.98B（980.8M），YoY +571%、QoQ +68%，高於共識約 $0.91B（907.5M）；Nebius AI Cloud 營收 $0.97B，占比約 99%；GAAP 淨損 $37.5M（每股 -$0.13）；adjusted EPS $0.31 對照共識約 -$0.69；adjusted EBITDA $465.8M（Q2 為 $236.2M）。來源: CNBC 摘要（搜尋結果，未開啟）、Nebius 6-K 新聞稿（SEC 索引，未開啟）。Impact: 混合。營收與獲利優於預期，但 adjusted EPS 的超預期主要來自約 $325M 非經常性收入（管理層稱來自 asset-light 模式），品質需打折。
- 2026-11-12 — 財報後股價重挫，CNBC 報導下跌約 16%，原因是 2026 資本支出增加與全年指引偏弱（盤中或收盤幅度未確認）。Impact: 偏空。市場重視的是支出與指引，而非當季數字。
- 2026-11-12 — 管理層揭露: 第三季起至財報前，客戶新增合約價值超過 $12B；季內完成 $5.75B 債務融資。Impact: 混合偏多。需求訊號強，但槓桿與融資成本同步上升（yf: totalDebt 約 $16.1B、debt/equity 約 131%）。
- 2026-11-13 — 價格快照: 收盤 $115.88，較前收 $128.64 下跌 9.92%；盤中區間 $109.00–$123.97；盤後 $112.80（-2.66%）。來源: yfinance info（時間戳推算為 11-13 收盤）。Impact: 偏空。財報後延續賣壓，距 52 週高點 $299.86 約 -61%。
- 2026-11-06 — 同業 AI 雲端公司財報超預期帶動 neocloud 族群反彈，NBIS 單日上漲約 7%（TIKR）。此前 10/29–11/05 區間 NBIS 由 $171.99 跌至 $120.37（約 -30%）。Impact: 偏多但短暫，隨後被財報後下跌抵銷。
- 日期未確定（約 11 月初，TIKR 寫為「今日」）— 德州州長選舉由 Gina Hinojosa 勝選，她主張數據中心限制與暫停新核准。來源: TIKR、azat.tv、Motley Fool（數字衝突：TIKR 稱 NBIS -19%、IREN -20%；azat.tv 稱 NBIS -2%、IREN -5%）。Impact: 偏空。NBIS 未揭露德州據點（美國據點為 Pennsylvania、Missouri，TIKR 另提 New Jersey），主要是族群情緒與政策風險。
- 2026-11-10（CoreWeave 財報）— 同業 CRWV 營收超預期並上修全年指引，2026 資本支出指引約 $37–39B；盤後上漲約 5%；Stocktwits 引述分析師稱 backlog 約 $133B、總債務逼近 $47B。來源: SiliconANGLE（2026-11-10 標題）、Stocktwits。Impact: 偏多於族群情緒，但 CRWV 3 個月仍下跌約 47%（摘要數字），顯示市場對融資與資本支出仍有疑慮。

已排除的訊號（非本期或日期不可信）: Meta $3B 合約（2025-11）、Microsoft $17.4B 合約（2025-09）、2025 Q3 財報（營收 $146.1M）、Feb 2026 Q4 財報、Jul 2026 單日 -12.6%、Sept 2026 neocloud 下跌（invezz）、「股價 $224」與「CoreWeave $90.66」等數字（日期或來源不一致）。Finimize 顯示 11-16 為下次財報，與公司公告衝突，判定無效。

## Sector macro
- 2026 年多次 — 德州數據中心監管風險升高。Abbott 先前暫停電網互連，據 Blockspace 報導，環境與資源許可凍結至州長審計於 12 月結束；新任州長主張延長暫停並凍結電價。Impact on sector: 偏空。德州占美國規劃數據中心 GW 約 27%（Wells Fargo 估計，經 TIKR 引述），新據點審批與電力取得變難，影響 neocloud 擴產速度。日期為多來源拼湊，未逐一核實。
- 近期（日期不明）— 超大型雲端業者 2026 年資本支出合計約 $600B（TheStack，日期未標示）。Impact on sector: 偏多，需求面支撐，但數字為舊文，需視為背景。
- 2026-12-08 至 12-09 — FOMC（12/9 14:00 ET 決議；來源: federalreserve.gov 行事曆與多家日曆）。Impact on sector: 利率敏感。NBIS 負債重、融資成本上升會壓縮自由現金流（yf freeCashflow 約 -$20.4B TTM；operatingCashflow 約 $5.1B）。目前聯邦基金利率區間 3.50–3.75% 僅見非官方來源，未核實。
- 信用市場 — CRWV 2031 年期債券價格據報跌至 79.5 美分（azat.tv，德州事件後）。Impact on sector: 偏空，顯示融資成本壓力上升。

## Peer signals
- CRWV — Q3 營收超預期、上修全年指引，2026 資本支出 $37–39B；盤後上漲；債務與資本支出是主要疑慮。
- IREN — 德州選舉後跌幅較大（數字來源衝突，-5% 至 -20%）；Microsoft Childress 項目預計 2026 Q4 交付，Sweetwater（德州）第二據點在開發中。
- NVIDIA — Rubin 平台計畫於 2026 下半年部署（來源: Nasdaq/Zacks 摘要，未標示確切日期）；NBIS 管理層表示將於 AI Cloud 與 Token Factory 導入。供應鏈面偏多，但無 11 月新聞可確認。

## Forward calendar (next 14d)
- 2026-11-16 至 11-20 — 未查到 BLS CPI 公布日期，需另行核實。
- 2026-11-26（週四）— 美國感恩節，股市休市（固定假日，Thanksgiving 2026 為 11/26）。影響: 流動性下降、週末前消息面影響放大。
- 2026-11-30 前 — 未查到 NBIS 公司層級的已知事件（無財報、無法說會、無 M&A 公告）。
- 超出 14 天但需追蹤: 12-08/09 FOMC；12 月德州州長審計結束與數據中心審批政策；約 2027-02-11 Q4 財報（yfinance 日期為估計值，isEarningsDateEstimate = true）。

## Net read
Q3 財報本身數字偏多：營收 $0.98B、高於共識 約 8%，adjusted EBITDA $465.8M，客戶新增合約價值超過 $12B，融資 $5.75B 已到位。但市場以資本支出上修與偏弱指引為重，股價在 11-12 下跌約 16%、11-13 再跌約 10%，收於 $115.88，距 52 週高點約 -61%。獲利改善的主因是約 $325M 非經常性收入，品質不足以抵消支出與槓桿壓力。外部面，德州數據中心政策風險與同業 CRWV 債務成本上升，讓族群情緒偏弱；僅 CRWV 財報超預期提供短暫支撐。整體新聞面淨偏空，但並非單一負面事件，屬混合偏空，強度中高。本報告不提供交易建議。

NEWS REPORT COMPLETE
