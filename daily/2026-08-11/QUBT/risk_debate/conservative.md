# Conservative risk view — QUBT

## Where trader is too aggressive

- **0.5% NAV 探索倉仍嫌過大**：ATR 因 PRICE_DATA_UNAVAILABLE 完全無法量化，意味著倉位大小無法以 vol-adjusted risk 校準，本質上是盲目定規模。在波動率未知的情況下，即使是「探索性」的 0.5% NAV 可能隱含遠超預期的實際波動敞口。無 ATR 即無合理 sizing，標準做法應為「不建倉，等數據」。
- **opex 3.9× revenue 是結構性問題，非過渡期噪音**：Q2 淨虧損 QoQ +191%，遠超收入 QoQ +51%，損益表在加速惡化。三連收購（Luminar 2月、NuCrypt 3月、NHanced 6月）正是 opex 暴增的直接來源，整合期通常持續 12-18 個月，且歷史成功率偏低。投資計畫對此風險的權重仍不足。
- **EV/Revenue 31.8× 估值脆弱性被低估**：同業 Rigetti 8.6×、D-Wave 8.9×，QUBT 溢價幾乎完全依賴 NeuraWave 商業化預期的單一敘事。年化收入僅約 $22.8M、毛利為負，任何執行延誤均可觸發多重壓縮（multiple compression），壓縮回歸 10-15× 對應股價腰斬 -40% 至 -51%（即從參考價 ~$9.18 跌至接近 $4.50）。

## Tail scenarios

- **Scenario A（發生機率估 30%）**：NeuraWave Q3 2026 交付延遲，Planck Dynamics 未確認驗收 → 市場重新定價 NeuraWave 敘事，EV/Revenue 多重壓縮，股價測試現金底線 $6.25，若市場對整合失敗定價，進一步下探至熊市目標 $4.50；從 ~$9.18 計算最大跌幅約 -51%。
- **Scenario B（發生機率估 20%）**：第四宗收購公告（六個月第四宗），市場解讀為管理層以收購稀釋換取增長幻象，opex 進一步擴張，季度淨虧損突破 $15M 警戒線 → 觸發投資計畫明確列舉的「SHORT_OR_AVOID」條件，持倉必須立即清倉。
- **Scenario C（發生機率估 20%）**：Q3 毛利持續為負且虧損 QoQ 再度擴大，管理層在財報電話會議未能提供 Fab 1 毛利轉正具體時間表 → EV/Revenue 31.8× 溢價全面崩解，分析師目標價 $18.33 失去支撐，市場重估至 $4.50-$6.25 區間。

## Recommended adjustments

- **Size**：0.5% NAV → **AVOID（零倉位）**。理由：ATR 不可得使 vol-adjusted sizing 無從執行，0.5% NAV 在未知波動率下毫無意義；opex 結構失控 + 三連整合尚未交答卷，不符合「可接受預期損失」的基本門檻。
- **Stop**：PRICE_DATA_UNAVAILABLE — 正因為止損水位無法確定，更不應建倉。若日後數據恢復，止損應設於現金底線 $6.25 下方（硬性風險上限），而非以寬鬆停損容忍估值波動。
- **Entry**：不應分批進場（scale in）；應**全面等待（full wait）**，具體觸發條件：Planck Dynamics 5 套 NeuraWave 系統完成客戶驗收書面確認，且追加訂單 ≥20 套；或 Q3 毛利率數字首次轉正。
- **Consider**：若投資組合已有其他量子計算相關敞口（如 IONQ、RGTI），QUBT 所形成的隱性集中度（hidden concentration）風險不容忽視，建議排查相關性後再決策。

## Position-level $ risk

當前無法完整計算：Stop 水位 PRICE_DATA_UNAVAILABLE，ATR 未知，入場價未確認。以最壞情境粗估：若以參考價 ~$9.18 建倉並止損於現金底線 $6.25，每股損失約 $2.93；若股價觸及熊市目標 $4.50，每股損失達 $4.68（約 -51%）。0.5% NAV 倉位下，實際美元損失取決於 NAV 規模，但在 EV/Revenue 31.8× 且整合風險高企的條件下，-51% 的下行場景並非低機率尾部事件，**不可接受**。

## What I'd push for

當前最謹慎且可執行的立場是**完全空倉（AVOID），而非 HOLD 附帶 0.5% NAV 探索倉**。理由在於三個不可同時解決的問題共存：（一）ATR 不可得導致倉位規模無法以任何量化標準校準；（二）opex 3.9× revenue 加上三連收購整合，顯示虧損加速是結構性而非季節性；（三）EV/Revenue 31.8× 在商業化未驗證前屬脆弱溢價，執行失敗的懲罰是 -40% 至 -51%，遠大於等待確認所放棄的上行機會。建議：待 Q3 2026 財報（預估 2026 年 11 月）確認毛利率轉正且 NeuraWave 交付獲書面驗收後，屆時行情數據恢復可用，再以 vol-adjusted sizing 重新評估入場時機。現在進場是在以「小倉位」之名承擔無法量化的尾部風險。

---

RISK CONSERVATIVE COMPLETE
