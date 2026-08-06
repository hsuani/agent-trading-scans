# Neutral risk view — S (SentinelOne)

## Points of agreement (both sides)
- ARR <20% 為不可妥協的基本面止損線，雙方無異議
- Conviction LOW 下不應建立全倉（>1% NAV）
- PRICE_DATA_UNAVAILABLE 使技術止損無法量化，任何倉位均缺乏 vol-adjusted 依據
- Q3 FY2026 財報為核心二元事件，財報前持有完整倉位存在不可對沖的尾部風險
- Goldman Sachs $15.50 目標為有意義的下行錨點，不應被忽視

## Aggressive overreach
- **Where：** 主張立即以 1% NAV 建倉、並配合 call spread 達 1.5% 等效暴露，且不等待價格資料恢復
- **Why：** PRICE_DATA_UNAVAILABLE 下 ATR 全無，加大倉位等同在暗室加注。S 的歷史日波動率可達 3–5%，1% NAV 名義部位的實際風險等同正常環境下 2–3% NAV 水位，遠超 conviction LOW 所允許的暴露。催化劑時效性是有效論據，但不能用來替代基本風控量化依據。

## Conservative overreach
- **Where：** 建議降至 0.25% NAV 甚至完全待機至財報後（100% 現金）
- **Why：** 全面放棄忽視了自治 SOC 情緒窗口的選擇價值與財報前漂移（pre-earnings drift）的潛在收益。$1B ARR、78% 非 GAAP 毛利率均屬具體可查驗的財報數字，合規需求底撐真實；以 0.25% NAV 甚至零倉應對有結構支撐的多方論據，是反射性謹慎而非有論據的風控。

## Balanced adjustment proposal
- **Size：** 維持 **0.5% NAV**（原始提案）；無 ATR 無法上調；有基本面支撐不應低於此
- **Stop：** 僅設**基本面止損**：ARR <20% 無條件全數出場，不設緩衝；技術止損待價格資料恢復後以 ATR 補設
- **Entry：** 分批進場——價格資料恢復後先建 0.25% NAV 觀察倉；Q3 財報確認 ARR ≥24% 或自治 SOC 量化披露後追加至 0.5% NAV
- **Hedge：** 若財報前持有，考慮 OTM put（行使價參考 $17，待價格資料恢復後確認 delta）；hedging 成本上限 0.1% NAV
- **Time horizon：** 1–3 個月，以 Q3 FY2026 財報（預期 2026 年 8–9 月）為核心決策節點；財報後依 ARR 數據決定加至 1% NAV 或完全退出

## Net $ risk if stop hits

以文件代理價格估算（PRICE_DATA_UNAVAILABLE，非即時報價）：
- 入場錨點 $20.05（news.md 52 週高點）→ GS 下行目標 $15.50，每股損失 $4.55
- 以 $1M NAV 為例，0.5% NAV = $5,000（約 249 股）
- 止損觸及 GS 目標：損失約 **$1,133（~1.1% NAV）**
- Scenario B（整合失敗，$13–14 區間）：損失約 **$1,500–$1,600（~1.5% NAV）**

## Net $ upside at T1 / T2

- **T1**（ARR ≥26%，自治 SOC 量化披露）：+15–20% 溫和重評 → 約 **$750–$1,000（~0.8% NAV）**；隱含 R:R ≈ 0.7：1
- **T2**（FCF margin 穩定轉正，NRR >120%，分析師升評）：+30–40% 倍數重評 → 約 **$1,500–$2,000（~1.7% NAV）**；隱含 R:R ≈ 1.5：1
- R:R 僅在 T2 情境下才算合理，進一步印證低信念小倉、靜待財報確認的策略方向

NEUTRAL VIEW COMPLETE
