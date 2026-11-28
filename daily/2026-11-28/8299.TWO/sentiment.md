# Sentiment — 8299.TWO (群聯電子 Phison) as of 2026-11-28

## 資料來源狀態
- pipeline/tools/yf 8299.TWO rec_summary / recommendations: 可用 (live 失敗, 回退 prices/yf/8299.TWO.json, _refreshed_at 2026-11-28T03:34:44Z, _misses 為空)
- insider: 回傳空陣列, live 與快取皆無資料 → DATA_UNAVAILABLE (無法區分「無交易」與「資料缺漏」)
- inst_holders: 空陣列 → DATA_UNAVAILABLE (僅有彙總持股比例)
- major_holders: 可用, 但單一快照, 日期不明, 無趨勢
- Reddit / StockTwits: 依指示未抓取 (屬封鎖類來源). WebSearch 未找到 PTT / Dcard / r/wallstreetbets 對 8299 的個別討論串 → 散戶直接貼文內容 DATA_UNAVAILABLE
- 股價: 各來源互相矛盾 (1,500 / 1,650 / 1,730 / 1,875 / 2,380 TWD, 另有 564 TWD 疑似錯誤前收), 本報告不以價格作判斷依據

## 分析師共識 (Analyst consensus)
最新快照 (0m): 4 strong buy / 7 buy / 0 hold / 2 sell, 共 13 家 (Yahoo 彙總, 無個別券商歸屬).
- 近一月 (-1m) 為 4 / 7 / 1 / 1, 最新月份 hold 1 → 0, sell 1 → 2, 合計不變, 表示有一家由 hold 轉為 sell.
- 過去 -2m, -3m 結構穩定 (4 / 7 / 1 / 1).
- 注意矛盾: 新聞稱統一投顧由買進降為中立 (hold), 但彙總 hold 為 0. 可能是降評時點或歸類方式不同, 無法在此釐清.

近期評等與目標價變動 (新聞報導, 非 yf 資料):
- 外資: 投資評等降至「減碼」(Underweight), 目標價由 2,588 TWD 大幅下修至 1,357 TWD (11/11 報告). 外資自承先前估值模型計算錯誤.
- 凱基投顧: 維持增加持股, 目標價由 2,900 下修至 2,700 TWD.
- 永豐投顧: 維持買進, 目標價由 2,998 下修至 2,070 TWD.
- 另有買進評級報導目標價 3,080 與 3,420 TWD (未標註日期與券商).
- 9 月報導: 宏遠 3,726 / 玉山 2,970 / 富邦 2,730 / 中信 2,785 TWD.
- 第三方彙整頁 (undated): 平均目標價約 2,977 TWD, 高 4,130, 低 2,240 TWD. 低標 2,240 與外資 1,357 明顯不一致, 此彙整值僅供參考.

目標價分散度極大 (約 1,357 至 3,726 TWD), 且多數報導日期集中於 9–11 月, 不宜直接平均.

## 基本面脈絡 (影響情緒的新聞事件)
- Q3 營收 860.76 億 TWD (季增 26.8%, 年增 374.6%), 毛利率 59.7% (低於 Q2 歷史高點), EPS 138 TWD, 歸屬淨利約 305 億 TWD.
- 驗算: EPS 138 × 股本 2.194 億股 (shares outstanding 219,439,000) ≈ 303 億 TWD, 與 305 億 大致吻合, 單位無誤.
- 11/6 法說: 執行長表示長期維持 60% 以上毛利率「不合理」, 守住 50% 以上即可. 企業級 SSD 明年需求看增. AI 生態系業務占營收 65% (10 月).
- 11/9 董事會通過買回 2,000 張 (約 200 萬股, 佔已發行股數約 0.91%), 價格區間 1,680–2,280 TWD, 上限 45.6 億 TWD. 消息後股價漲停.
- 下半年毛利率因基期墊高恐下滑 (管理層與法人看法).
- 風險論述: NAND 循環 (研調示警 2027 年下半 NAND 可能供過於求); 大廠 (Samsung, Micron) 垂直整合威脅 controller 業務 (Simply Wall St bear narrative).

## Retail social
- Reddit: DATA_UNAVAILABLE (來源封鎖, WebSearch 未取得個別討論串)
- PTT / Dcard: DATA_UNAVAILABLE (WebSearch 未取得股版討論內容)
- StockTwits: DATA_UNAVAILABLE (來源封鎖)
- X / 媒體鏈接: 僅能取得媒體與投顧報導, 語氣分歧. 無法量化聲量, 「相對typical 的聲量」DATA_UNAVAILABLE.
- 替代訊號 (非散戶原始貼文): Simply Wall St 報導平均週波動 10.1%, 高於半導體產業 6.1%, 顯示波動度高, 有利於短線討論熱度 (屬推論). 一則未標註日期的 LinkedIn 文稱 NAND 合約價 11 月漲約 50%, 可信度低, 不採信為事實.
- 主題 (由媒體與論壇摘要推斷, 非原始貼文統計): (1) AI 與企業級 SSD 題材; (2) 毛利率是否正常化; (3) NAND 景氣循環何時反轉; (4) 買回與估值 (外資模型錯誤爭議); (5) 目標價分歧.

## Insider activity
DATA_UNAVAILABLE. yf insider 回傳空陣列, 快取亦為空, 無法判定 6 個月內淨買賣金額, 亦無法判斷 CEO / CFO 是否交易.
補充: 公司層面有庫藏股買回 (2,000 張, 上限 45.6 億 TWD), 屬公司行為而非內部人交易, 不應計為 insider 買入.

## Ownership shifts
- insidersPercentHeld 15.8%, institutionsPercentHeld 20.6%, institutionsFloatPercentHeld 24.5%, institutionsCount 182 (單一快照, 日期不明).
- 機構持股趨勢: DATA_UNAVAILABLE (僅一期快照, 無歷史比較). inst_holders 明細 DATA_UNAVAILABLE.

## Net sentiment score
- 分析師面 (bullish-leaning): 13 家中 11 家 buy 以上, 但外資 underweight 且目標價大砍, 本國投顧目標價仍高於現價 (以媒體報導價位推估). 內部分歧明顯.
- 散戶面: DATA_UNAVAILABLE, 無法評分.
- 媒體面: 基本面數據 (營收, EPS) 仍創高, 但毛利率正常化與 NAND 循環爭議主導語氣, 偏中性.
- 綜合: NEUTRAL (略偏多, 信心 低). 理由: 分析師共識仍偏買進, 但評等與目標價分歧擴大, 散戶與內部人資料缺失.

Divergence flag: 無法判定 (散戶資料 DATA_UNAVAILABLE). 分析師內部存在明顯分歧: 外資 Underweight 與本土投顧 Buy 方向相反. 若日後補上散戶資料, 需再比對.

## 不足與後續建議
- 補抓 insider 與 inst_holders 的 live 資料 (或確認快取為真實空值), 以判斷內部人與機構流向.
- 補查 PTT 股版 / Dcard 8299 討論串 (WebSearch 需更精確的關鍵字或站內 query).
- 統一股價基準 (建議以同一日 TWSE/TPEX 收盤為準), 目前來源價格互相矛盾.
- 確認統一投顧降評日期, 並核對彙總 hold=0 與新聞之矛盾.

本報告為情緒資料整理, 不構成交易建議.
