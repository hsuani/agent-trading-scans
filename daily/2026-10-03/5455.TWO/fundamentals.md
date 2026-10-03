# Fundamentals — 5455.TWO as of 2026-10-03

## ⚠️ 資料完整性警示（ticker–公司對照錯誤）
**本報告發現 `universe.py`／任務指令中 tw_photonics 名單的 ticker 對照表有誤**：5455.TWO 經 yfinance info 查證，實際公司為 **昇益開發（Sheng Yi Development Co., Ltd.）**，一家新竹地區的**房地產開發商**（住宅建案、建材買賣），與矽光子／光通訊產業**完全無關**。
- 經 WebSearch 查證（investing.com、cnyes.com 等多方來源交叉比對），英特磊科技（IntelliEPI Inc., 矽光子磊晶廠商，任務指令原意所指公司）在 TPEx 的正確股票代號應為 **4971.TWO**，並非 5455.TWO。
- 此為第二起同類 ticker 碰撞案例（第一起見 2026-09 tw_probe 掃描報告中 6223.TWO/MPI Corp 資料污染事件），建議 universe.py 之 tw_photonics 清單將 5455.TWO 修正為 4971.TWO，並在下次排程前重新驗證全清單。
- 依「價格與身分完整性」原則，本檔**不得**冒用昇益開發的財務數據去分析英特磊，亦不得杜撰英特磊的任何數字。以下如實分析 5455.TWO（昇益開發）本身，其基本面與矽光子主題**無關**，僅供完整性記錄，本檔將維持 Phase-1-only，不進入 Phase 2-4。

## Executive summary
5455.TWO 實際為昇益開發（房地產開發商），非英特磊。2025 年營收年減 43.6%（NT$36.24 億→NT$20.44 億），營運現金流與 FCF 皆為負值，獲利能力指標（營業利益率 -1032.8%、淨利率 -156.4%，皆為 yfinance TTM 口徑，反映最新一期有異常虧損項目）顯示財務體質不穩定，與產業成長故事無關聯。

## revenue & profitability
- 2025 年營收 NT$20.44 億，較 2024 年 NT$36.24 億衰退 43.6%；近三年營收波動極大（2022 年 NT$6.0 億→2023 年 NT$16.2 億→2024 年 NT$36.2 億→2025 年 NT$20.4 億），符合房地產建案認列收入「完工時點不均」之典型特徵。
- yfinance TTM 口徑 revenueGrowth=-100%、operatingMargins=-1032.8%、profitMargins=-156.4%，顯示最新一期（可能為單季）認列虧損或一次性損失，惟房地產開發商財報常見巨幅波動,需以年度數字綜合判讀。
- ROE -3.0%、ROA -0.4%，資本效率為負。

## cashflow & balance sheet
- FCF（2025）NT$-17.98 億，營運現金流 NT$-18.08 億，財務體質疲弱。
- 現金僅 NT$0.20 億 vs 總負債 NT$27.95 億，負債權益比高達 205.0%，槓桿極高，速動比率僅 0.056，短期流動性緊張。

## capital allocation & insider signal
- 無股利配發（payoutRatio=0）。內部人持股高達 70.3%（公司屬性偏向家族／創辦人控股型態，常見於中小型營建股），機構持股 0%（0 家機構），顯示完全不在法人覆蓋範圍內。

## valuation
- Trailing/forward P/E 皆無法計算（獲利不穩定），P/B 1.48x、P/S 75.7x（P/S 畸高顯示營收與市值關係異常，典型房地產股以淨值法估值而非營收倍數）。
- Beta -0.029，幾乎與大盤無相關性,與高波動科技成長股特性截然不同,進一步佐證此檔與矽光子題材無關。

## key catalysts
- 無與矽光子/光通訊相關之催化劑可記錄（公司業務與此產業無關）。
- 房地產業務本身催化劑（建案交屋時程、建材成本）不在本次 tw_photonics 掃描研究範圍內。

## metrics table
| Metric | Latest | YoY | Sector median (estimate) | Verdict |
|---|---|---|---|---|
| Revenue (annual) | NT$20.44B | -43.6% | N/A（非光通訊業） | 不適用比較 |
| Net debt/equity | 205.0% | — | — | 高槓桿 |
| Institutional ownership | 0% | — | — | 無法人覆蓋 |

## red flags
- **最重大紅旗：ticker 身分與產業歸類錯誤**——本檔非光通訊/矽光子公司，不應計入 tw_photonics 同業比較或 Phase 5 排名。
- 即使就其實際業務（房地產）評估，財務體質亦顯示高槓桿（D/E 205%）、負 FCF、零法人覆蓋，體質偏弱。

FUNDAMENTALS REPORT COMPLETE
