# Conservative risk view — TLN

## Where trader is too aggressive

- **倉位未經 vol 校準**：PRICE_DATA_UNAVAILABLE 導致 ATR 為零，1.5% NAV 的 Medium 建議缺乏波動率錨點支撐。無 ATR 基礎的倉位規模，在高波動事件（FERC 裁決、Fed 會議）前等同盲目下注。
- **Cornerstone 槓桿風險低估**：Cornerstone 完成後淨債務升至 $5.5–6.0B，超越原始模型 $4–5B 上限，但投資計畫對此只以「仍在 2.5–3.2× 目標區間」輕描淡寫。在 Fed 預期 2026-09-16 再升 25bp（利率區間至 3.75–4.00%）環境下，利息覆蓋率緩衝薄於假設。
- **內部人士淨賣出被過度淡化**：$1.1B 歷史累積淨賣出對比 $1.2M 買入，比率約 916:1。「破產後低成本股權套現」論點未被嚴格量化；若高管在 Q2 業績後以 $380 附近繼續拋售，訊號強度不容忽視。
- **核電 AI 主題集中風險**：若組合已持有 CEG 或 VST，TLN 的加入形成核電／AI 數據中心的隱性主題集中，個股 FERC/PPA 事件影響可同向共振。

## Tail scenarios

- **情境 A（概率 20%）**：FERC 正式暫停或拒絕 Susquehanna front-of-meter 傳輸重組 → AWS 計費時程延後 12–18 個月，EBITDA 下修 $200–400M → 論文核心假設瓦解，股價修正幅度參考類似事件（CEG 監管拒絕案例）可達 25–40%；NAV 損失：若持 1.5% 倉位，理論損失 0.38–0.60% NAV。
- **情境 B（概率 15%）**：Fed 9 月升息超預期（50bp）觸發信評機構對 TLN $5.5–6.0B 淨債務重新評估 → 信評下修至 B+ 區間 → 再融資成本大幅攀升，FCF 指引下修 → 股價回調 15–25%；NAV 損失：0.23–0.38% NAV。
- **情境 C（概率 10%）**：Q3 財報（2026-10 初）淨債務/EBITDA 突破 3.2× 且 AWS 實際計費 MW 低於預期 → 雙重負面催化劑疊加 → 股價急跌 30%+；NAV 損失：0.45%+ NAV。

## Recommended adjustments

- **Size**：Medium（1.5% NAV）→ Small（0.5% NAV）。理由：FERC 二元事件未解決、ATR 缺失、Cornerstone 槓桿超原始上限，三重不確定性同時存在時不應半倉建倉。0.5% 為「探索性持倉」，留 1.0% NAV 彈藥待確認後加碼。
- **Stop**：價格數據恢復後設定為入場價下方 1.5–2× ATR（而非 trade_proposal 未定義的開放止損）；以收盤價穿越 Stop 觸發，非盤中跳動。
- **Entry**：分批建倉：首批 0.5% NAV 僅在（1）價格數據管道恢復且 R:R ≥ 1.5 確認後；次批 0.5% 待 FERC 正式核准；末批 0.5% 待 Q3 財報 AWS 計費量 MW 符合預期。
- **對沖**：若已持有 CEG 或 VST，考慮買入 XLU put（到期 2026-12）作為核電主題集中的尾部保護。

## Position-level $ risk

PRICE_DATA_UNAVAILABLE，無法計算具體 $(entry − stop) × shares。以參數化方式呈現：若入場後 ATR 確認、止損設於入場下方 8%，則每 1% NAV 倉位的最大止損損失為 NAV × 1% × 8% = 0.08% NAV；0.5% 初始倉位對應最大損失 0.04% NAV，可接受。若因 FERC 衝擊股價跳空 25%（止損失效），損失擴大至 0.5% × 25% = 0.125% NAV，仍在合理範圍。**核心結論**：止損能否有效執行取決於 FERC 裁決是否為盤後突發事件；建倉前須確認流動性與裂口風險。

## What I'd push for

鑒於 PRICE_DATA_UNAVAILABLE 導致 R:R 無法驗算，且 FERC 裁決屬高影響二元事件、Cornerstone 槓桿已超原始上限、Fed 九月預期再次升息，現階段應將初始建倉壓縮至 Small（0.5% NAV），並以「三階段確認」機制取代一次性 Medium 建倉：第一階段等待價格數據恢復並確認 R:R ≥ 1.5；第二階段等待 FERC 正式核准；第三階段等待 Q3 財報 AWS 計費數據符合預期。若三項條件全部達成，可分批累積至 Medium（1.5% NAV）；若任一條件失敗，以 0.5% 倉位的有限損失退出，保留資本待更清晰機會。

CONSERVATIVE VIEW COMPLETE
