# Final decision — 6217.TWO (中探針) as of 2026-11-07

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
Phase-1-only stub（非 positive pick，未進入 Phase 2-4 完整辯論）

## Phase-1 positive-pick 訊號評分
| 訊號 | 條件 | 結果 | 判定 |
|---|---|---|---|
| Fundamentals | Revenue YoY>15% 且 FCF/NI > -1 | 2025 營收 YoY +19.1%（過），但 2025 淨損 -1.85 億、FCF -6.95 億，連續三年 FCF 為負且淨負債年增 35%，獲利結構明顯惡化 | **FAIL** |
| Market（技術） | RSI14<72 且 MACD hist 非深度負值 且 價格>MA50 | RSI14=26.84（超賣）、MACD hist -6.57（相對股價 109 為深度負值）、收盤 $109 < MA50 $169.76（-35.8%） | **FAIL** |
| News | 淨頭條情緒偏多 | 判定「淨新聞傾向偏空，幅度中到大」：9 月營收年增僅 +0.7%、H1 虧損、多次列注意股/處置股、股價自高點已跌約 71% | **FAIL** |
| Sentiment | 分析師共識≥60% buy 或機構資金淨流入 | 無分析師評等資料（yf 回傳空值）；機構持股僅 1.84%（8 家），資料不足，綜合判定「中性」 | **FAIL** |
| Valuation | Forward P/E<35x 或明確 EPS 成長催化 | Forward P/E 27.4x 僅依賴 forward EPS 3.98 的轉盈假設（TTM EPS 為 -0.37，公司目前虧損中），非已確認催化 | **FAIL** |

**合格訊號數: 0/5（門檻為≥3）→ 不符合 positive-pick 標準，僅完成 Phase 1（+ Phase 1.5 evidence shadow），未進入 Bull/Bear 辯論、交易員規劃與風險委員會。**

## 為何不予完整分析
中探針是 tw_probe 四檔中財務與價格表現最弱者：營收成長但獲利未跟上（H1 虧損、子公司拖累）、FCF 連續三年為負、淨負債大幅攀升、股價自 5 月高點 371 元崩跌至 109 元（約 -71%），且多次列入注意股/處置股。五項訊號全數未過，暫不納入完整五階段辯論。

## 監控觸發（若未來重新評估）
- 若 Q3/Q4 財報顯示轉盈且 FCF 止血，基本面訊號可能轉強。
- 若股價止穩並收回 MA20（$163.43），技術面訊號可能轉強。
- 若取得分析師覆蓋或機構持股回升數據，情緒面訊號可重新評估。

## 資料限制聲明
本報告僅使用 2026-11-07 分析日工具輸出（yfinance/ta.py，price feed 來源為 cache，最新收盤為 2026-11-06）與同日 WebSearch 結果，未借用歷史 daily/<date>/ 報告的任何數字。

FINAL DECISION COMPLETE
