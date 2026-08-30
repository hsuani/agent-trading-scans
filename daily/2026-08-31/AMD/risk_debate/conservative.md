# Conservative risk view — AMD

## Where trader is too aggressive

**一、fundamentals.md 內部矛盾，立論基礎已動搖**
該報告宣稱「無重大減持、內部人信號正面」，但 investment_plan.md 白紙黑字確認：CTO、CFO、EVP、CEO 四人於 2026 年 8 月集中執行 10b5-1 賣出，合計逾 $40M。基本面報告對同一事件的描述截然相反，顯示該報告所依賴的訊息截止日期有誤，交易決策不應建立在此版本之上。

**二、P/E 水位嚴重低估**
fundamentals.md 以 Forward P/E 25-35x 作為估值框架，但這需要未來 12 個月 EPS 達到 $13-19（即每季 $3.25-4.75），相當於實際已報告 Q2 Non-GAAP EPS $1.66 的 2-3 倍。多頭的低 P/E 論述依賴尚未實現的 EPS 三倍成長，Trailing P/E 的真實水位約 70x，非 25-35x。

**三、-9% 財報後反應是明確分配訊號**
Q3 指引較預期高 $0.5B，市場仍賣出 9%，代表在 ~70x Trailing P/E 下容忍度接近零——任何單季失誤將同步壓縮倍數與盈餘，形成雙重打擊（multiple compression × earnings miss）。

**四、結構性毛利率劣勢不可輕描淡寫**
AMD 毛利率 53% vs NVIDIA 73%，差距 1,800bps，直接反映 CUDA 生態議價能力差異。此差距無法在 MI400 一個產品周期內彌合。P/FCF 60-80x 更高於 NVIDIA，資本效率倒置。

## Tail scenarios

- **情境 A（機率 25%）**：Q3 FY2026 財報數據中心增速低於 30%（高基期效應，+107% 不可持續），市場以 P/E 重估至 35-40x 回應 → 估值縮水幅度顯著，若 EPS 同步下修則雙重壓縮。**PRICE_DATA_UNAVAILABLE，無法量化具體美元損失，但邏輯路徑明確。**
- **情境 B（機率 20%）**：Fed 維持高息時間超預期 + 美國政府將 AI 伺服器 GPU 納入新一輪出口管制 → CSP 採購計劃推遲，數據中心營收 miss 指引，AMD 因毛利率缺乏緩衝空間而下行幅度大於 NVIDIA。
- **情境 C（機率 15%）**：Google TPU、AWS Trainium、Meta MTIA 自採比例快速上升，外採 GPU TAM 季環比萎縮，AMD「唯一替代方案」定位所依賴的市場本身縮小，+107% 增速的基礎消失。
- **情境 D（機率 10%）**：Q3 前後再度出現未在 10b5-1 計劃範圍內的高管減持（超 $20M），觸發 trade_proposal.md 自訂的止損條件，市場情緒短期崩潰。

## Recommended adjustments

- **Size**：維持 Small（0.5% NAV 以下）——**現持倉者不加碼，未持倉者歸零**。HOLD 意指守住現有部位，不是建立新部位的許可。
- **Entry**：等待 Q3 財報（2026 年 10 月中旬）確認數據中心增速 ≥50% 且毛利率 ≥56% 再考慮加碼；任何早於此時點的進場均屬在高基期不確定性下承擔不對稱下行風險。
- **Stop**：PRICE_DATA_UNAVAILABLE，無法指定具體止損價。定性止損條件依 trade_proposal.md：增速 <30%、毛利率 <52%、管理層連續第二次下修指引——三者任一觸發即出清。
- **Hedge**：若已持倉，考慮以 QQQ put spread（10 月到期）或 SOX ETF（SOXX）puts 對沖系統性半導體板塊風險，抵消-9% 財報反應所暗示的市場容忍度不足。

## Position-level $ risk

PRICE_DATA_UNAVAILABLE，無法計算 (entry − stop) × shares 的具體美元損失。然而，邏輯框架成立：在 ~70x Trailing P/E 且 EPS 成長預期需翻 2-3 倍的情況下，若 Q3 miss，估值回歸 25-30x Trailing 所對應的理論下行幅度，空方目標區間（investment_plan.md 引用）為 $228-137，即潛在跌幅 51-71%。即使以最保守的部分回歸計算，此交易的下行空間遠大於上行空間，R:R 不對稱對空方有利。NAV 0.5% 以下的倉位規模是目前情境下唯一可接受的風險承擔。

## What I'd push for

**立即結論：ZERO 新部位。** 現有持倉維持 Small（0.5% NAV 以下）不動。-9% 財報後賣壓是在指引上調情況下發生的，代表市場在 ~70x Trailing P/E 下對任何不確定性的容忍度為零。四位 C-suite 高管 8 月集中減持 $40M，是迄今最直接的方向性訊號，與「管理層信心確實」的基本面報告結論相悖，說明 fundamentals.md 該節分析已失效。在 P/FCF 60-80x、毛利率結構性落後 NVIDIA 1,800bps、高基期讓 +107% 增速下一季幾乎必然放緩的三重條件下，唯一理性策略是等待 Q3 財報提供增速與利潤率的實際驗證，屆時才重新評估加碼邏輯。

CONSERVATIVE RISK COMPLETE
