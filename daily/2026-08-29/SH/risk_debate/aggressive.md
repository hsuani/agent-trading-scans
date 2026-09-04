# Aggressive risk view — SH

## Where trader是too cautious
- **倉位標籤與實際 dollar risk 脫節**：以「0.5% NAV」為 notional size（非 risk budget），entry $32.20、stop $31.70，stop 距離僅 1.55%。以 illustrative NAV $1,000,000 計算，0.5% NAV = $5,000 notional ≈ 155 股，觸及停損的實際 max loss 僅 $775（0.078% NAV）——這遠低於任何合理組合能承受的單筆風險上限。換言之，交易員把「小倉位」等同於「低風險」，但真正決定風險的是 stop 距離乘以股數，不是 notional 標籤本身。
- **Entry 已算積極**（現價即在 entry zone、不追高不等回檔），這點無需修正，予以肯定。
- **R:R 3.5-3.8x 未被倉位充分利用**：這是本輪辯論中少見「兩邊證據品質相近但風險報酬比仍然偏高」的設置——bear 論點強（6/10）主要針對「長期持有」的結構性衰減，但本次是嚴格天期（錨定 9/16 FOMC）的戰術倉位，衰減成本在 1-4 週窗口內僅 0.1-0.3%，遠小於停損定義的風險，也遠小於潛在報酬。

## Recommended adjustments
- Size：0.5% NAV → **1.0-1.5% NAV**（rationale：即使倉位翻三倍，max loss 仍僅 0.16-0.23% NAV，遠低於典型組合 0.5-1% 單筆風險上限；且此為有明確單一可證偽事件（FOMC 9/16）的短天期倉位，非長期核心持倉，risk budget 理應集中而非分散稀釋）。
- Stop：$31.70 → **$31.55**（給出略多緩衝，避開緊貼 52 週低點 $31.83 之下的整數關卡，該區間易成為 stop-hunt 集中地；ATR14 僅 $0.27，$0.65 停損距離仍只是 2.4x ATR，不算寬）。
- Entry：現在進場，維持交易員判斷，不需更早。
- Consider：**leveraged variant** — 現貨 VIX 14.2-14.9 屬歷史低位，選擇權隱含波動率便宜，可用 SH call spread $33/$35，到期 2026-09-18（涵蓋 FOMC 後首個交易週），以定額權利金取得凸性報酬，避開長天期日重置衰減，同時把 max loss 鎖定在權利金本身，可用相同 $ risk 換取更大 notional 曝險。

## Asymmetry argument
以 illustrative NAV $1,000,000、倉位升至 1% NAV（310 股，entry $32.20）計算：
Worst case max loss（跌破 $31.55）：$0.65 × 310 ≈ **$202**（0.02% NAV）。
Realistic upside（觸及 T1 $33.96）：$1.76 × 310 ≈ **$546**；觸及 T2 $34.09：$1.89 × 310 ≈ **$586**。
Ratio：B/A ≈ 2.7-2.9x（以擴大後倉位計，仍維持 stop 端優勢；若以停損距離而非絕對 $ 衡量則回到原本 3.5-3.8x R:R)。無論用哪個口徑，這都是 dollar risk 極小、payoff 明確不對稱的設置。

## What I'd push for
在承認此倉位本質是「組合保費」而非方向性核心押注的前提下，我仍主張把 notional size 從 0.5% NAV 提高到 1-1.5% NAV，並把 stop 從 $31.70 微調至 $31.55——因為目前的停損距離所定義的實際 dollar risk（即便升至 1.5% NAV 也僅約 0.03% NAV）遠低於「小倉位」這個標籤所暗示的保守程度，是在浪費一個有明確單一可證偽日期（9/16 FOMC）、R:R 逼近 4x 的稀有設置；若想進一步壓低 theta 衰減暴露，可將部分曝險轉為 SH call spread，用固定權利金取得更高 convexity，兩者搭配比現行純現貨小倉位更有效率地利用這個窗口。

AGGRESSIVE VIEW COMPLETE
