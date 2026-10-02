# Neutral risk view — UUP

## Points of agreement (both sides)
- 現價 $28.96 緊貼 52 週高點 $29.00、RSI14 77.84、BB %B 0.962，雙方都同意現價不宜以 Medium/Large 新建倉位。
- 趨勢結構（MA20>MA50>MA200、MACD 柱狀擴張）完整偏多，雙方都不主張放空或翻空。
- CFTC 美元淨部位處 18 個月高點（13.9% 未平倉），雙方都視為風險因子，差異只在「擁擠程度」解讀。
- FOMC/CPI 日期與升息機率在各報告間互相矛盾，雙方都承認需即時核實，執行前不可照單全收。

## Aggressive overreach
- Where：現價直接進 Medium、站穩後加碼 Large，並把停損從 $27.87 放寬到 $27.63。
- Why：trade_proposal.md 已算出現價進場 R:R 僅約 0.04，aggressive 並未反駁此數字，只用「波動率低、政策分化明確」帶過；停損放寬疊加 size 放大至 Large，美元風險被同時從兩端放大（風險區間擴大近 2 倍 × 名目部位擴大近 1.7 倍），與「ATR 極低應可承受更大名目部位」的論點方向相反——ATR 低其實支持「維持緊停損、用部位大小調風險」，而非「放寬停損再加大部位」。Call spread 疊加現貨部位在催化劑日期未定（CPI/FOMC 確切日期矛盾）的情況下，等於對一個尚未釐清時點的事件額外付權利金，屬槓桿偏好而非風險管理。

## Conservative overreach
- Where：停損收緊至 $28.05，且要求 CPI 或 FOMC 至少一項公布後才可進場。
- Why：$28.05 落在建議進場區間 $28.22-$28.39 的正下方僅 0.17-0.34 美元，等於把正常區間內的價格雜訊也視為出場訊號，與 conservative 自己提出的 Scenario B（跳空穿越 $27.87，實際成交恐落在 $27.50-$27.60）邏輯矛盾——更緊的停損只會更早、更頻繁地被雜訊洗出，無助於應對跳空風險。要求等待催化劑才進場，則等於否決了 investment_plan.md 已定的 NEUTRAL 偏多結論與既定回檔進場劇本，若 CPI/FOMC 延後至 11 月且期間先行回檔再站穩 $29.00，將完全錯過戰術進場窗口，屬於防禦性偏誤而非基於數據的判斷。

## Balanced adjustment proposal
- Size：維持 Small（0.5%）起始試單，於回檔至 $28.22-$28.39 且 RSI14<70 進場；加碼至 Medium（1.5%）的門檻改為「CPI 或 FOMC 至少一項已公布且結果偏多」，不預設僅憑 RSI 回落即可加碼；不建議 Large。
- Stop：採 $27.87（trade_proposal 原案），介於 aggressive 的 $27.63 與 conservative 的 $28.05 之間，位於二級支撐、進場區間下緣之外，兼顧假跌破緩衝與風險上限。
- Entry：維持分批回檔進場（不追現價），但不強制等待催化劑公布，回檔確認即可啟動 Small 試單。
- Hedge：新建倉位不預設 options overlay；僅當既有多頭部位偏大且同時持有其他做多美元曝險（美元期貨、日圓空頭）時，才加入短天期 put 做局部對沖。
- Time horizon：戰術 1-4 週（涵蓋 CPI/FOMC 落地），策略 1-3 個月。

## Net $ risk if stop hits
以 NAV $100,000、進場 $28.30、停損 $27.87（風險 1.52%）計算：Small（$500）≈ $7.6（0.008% NAV）；確認後加碼至 Medium（$1,500）累計風險 ≈ $22.8（0.023% NAV）。

## Net $ upside at T1 / T2
T1 $29.00（+2.47%）：Small ≈ $12.4／Medium ≈ $37.1。T2 $30.00（+6.01%，六個月框架）：Small ≈ $30.1／Medium ≈ $90.2。

NEUTRAL VIEW COMPLETE
