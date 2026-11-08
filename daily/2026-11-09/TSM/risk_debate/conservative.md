# Conservative risk view — TSM

## Where trader is too aggressive
- 進場時機問題：目前價格仍低於三條均線、MACD 在零軸下方，11-05 爆量下跌只有一根反彈 bar，technical 尚未止跌確認，但 trader 選擇「現在即可建立 Small 倉位」而非等 11-10 營收公告出來再進場。在 8 天內有兩個二元事件（10 月營收、NVDA FQ3）的情況下，提早一天進場換不到額外報酬，卻多承擔一天的 gap 風險。
- Stop 位置本身距離合理（約 1.4 倍 ATR14），$ 風險也已用 Small/Medium 分級控制，這部分 trader 做得對，不應為了「更保守」而硬改。但 stop 之下到 52 週低點 $266.82 之間完全沒有確認支撐（跌破 $351.19 即再跌約 23%），代表若跳空（overnight 頭條，例如出口管制、台海地緣政治、NVDA 財報重挫）直接貫穿 stop，實際滑價虧損可能遠大於帳面的 $24.25/股估算，這個 gap 風險未被量化進風報比。
- 宏觀/產業風險低估：trade_proposal 與 investment_plan 皆未提及 2026-12 FOMC 以外的宏觀變數（如半導體出口管制、台海風險、AI 資本支出若放緩對同業估值倍數的連動壓縮），forward P/E 16.1x 的估值緩衝在「情緒性去槓桿」情境下可能與基本面無關地被壓縮。
- 隱性集中風險：此倉位的核心觸發變數（NVDA FQ3 財報）與市場上多數 AI/半導體相關持股（NVDA、AMD、SOXX 成分股）高度相關；若投資組合同時持有其他 AI 供應鏈倉位，TSM 並非獨立風險來源，而是放大同一個事件的曝險。

## Tail scenarios
- Scenario A（機率約 20%）：NVDA FQ3 財報/指引令市場大失所望 → 資料中心需求敘事破裂，TSM 跳空跌破 $351.19，直接下探 $300 附近，較帳面 stop 多損失約 2-3 倍。
- Scenario B（機率約 15%）：11-10 10 月營收 YoY 明顯低於 45% → 當日即觸發 invalidation，部位在验证窗口開始前就被打臉。
- Scenario C（機率約 10%）：12 月 FOMC 鷹派或中美出口管制升級 → 高估值半導體板塊整體去槓桿，forward P/E 自 16.1x 壓縮至 12x 左右，與 TSM 自身基本面無關仍下跌約 20-25%。

## Recommended adjustments
- Size：維持 Small 起始尚可接受，但建議 11-10 營收公告前只進場半個 Small（約 0.25% NAV），公告確認後再補到完整 Small，11-17 後再視三項加碼條件決定是否升至 Medium。
- Stop：$351.19 的邏輯位置可保留，但須外加「隔夜 gap 保護」——以選擇權（短期 put 或 collar）取代單純現股 stop，避免跳空貫穿造成實際損失遠超帳面估算。
- Entry：寧可等 11-10 營收數字出來後再進場，用一天的時間成本換掉一個二元事件的曝險，而非現在就進場「賭」營收。
- Consider：用 SOXX 或 NVDA 短期 put 作為 11-17 財報的事件避險，把 TSM 的 idiosyncratic 論點和 NVDA 財報的 beta 風險分開。

## Position-level $ risk
以代表進場價約 $375、stop $351.19 計，$ 損失/股 ≈ $23.81（約 6.3%）。Small（0.5% NAV）下觸發 stop 的組合虧損 ≈ 0.5% × 6.3% ≈ 0.032% NAV；若加碼至 Medium（1.5% NAV）則 ≈ 0.095% NAV。兩者在帳面上都屬可接受的小額風險，sizing 邏輯本身並不過度激進。真正的風險缺口在於 gap 情境下實際虧損可能是帳面的 2-3 倍，這是尚未被定價的尾部風險。

## What I'd push for
Trader 的分級加碼邏輯是對的，不需要整體砍倉,但應把「現在進場」改成「等 11-10 營收確認後進場」，把 stop 從單純現股停損升級為搭配短期選擇權的跳空保護，並在部位存續期間用 NVDA/SOXX put 對沖 11-17 財報的系統性事件風險，才能把帳面風報比和實際尾部風險對齊。

CONSERVATIVE VIEW COMPLETE
