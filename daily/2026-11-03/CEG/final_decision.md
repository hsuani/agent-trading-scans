## FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — CEG as of 2026-11-03

## Verdict
REJECT

## 持倉判定
CEG 不在 `pipeline/tools/held_tickers.txt`，屬新倉，採 A 框架。問題是「該不該進」，答案是：財報前不進。

## Final trade card
無。REJECT 不建立新部位，不提供 Entry/Stop/Target。
（資料基準：ta 收盤 $267.39，2026-11-02；11-03 K 線尚未產生。）

## Dealbreaker
Q3 財報（預估 11-09，另一來源 11-06，未經公司確認）是二元事件，而且它正好決定了整場辯論的勝負：H1 2026 FCF -0.97B、TTM FCF/NI 0.09x、股利/FCF 0.56x、現金僅 0.70B，這些是硬數據；Google 20 年 PPA 與 Q2 上調指引是硬催化。兩邊證據品質相當，在 ATR14 $11.60（4.3%）、20 日年化波動率 64.7% 的環境下開新倉，等於用 NAV 賭擲硬幣。價格同時低於 MA20/50/200、MA200 下彎、區間 $247.20–$282.77 未突破任一端，技術面也給不出 R:R 基礎。

Aggressive 建議的 $280/$300 call spread 是合理的 defined-risk 工具，但本 pipeline 只輸出一張現股 trade card，不以選擇權變體繞過「不進場」的結論。

## Risk debate adjudication
- Aggressive's strongest point：等「站穩 MA200」才進場，確認往往發生在跳空之後，屆時 R:R 已劣化。這是真的，但它是一個「錯失成本」論點，而非「現在進場有正期望值」的論點。
- Conservative's strongest point：11-06 VST 財報、11-09 CEG 財報、11-16 FERC 期限兩週內疊加，是連續事件風險而非單一事件；同時其 Scenario B（-42%～-55%）沿用了 investment_plan 已指出的雙重保守假設，我不採納該尾部機率。
- Net：我偏向 **neutral** 的判斷。Aggressive 把「雙底未破」等同「FCF 問題是暫時性」，這是邏輯跳躍；Conservative 把未經獨立驗證的 bear case 當尾部情境。對新倉而言，正確答案就是不開倉，等資料解決 Crux 1 與 Crux 2。

## 論點支柱
（這是「未來若轉 LONG」的支柱，用來定義重訪條件）

| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 現金流能自我覆蓋 | Q3 OCF − capex − 股利 ≥ 0 | H1 FCF -0.97B，Q3 未公布 | 觀察中 |
| 盈餘品質與指引 | 維持 USD 11.50–12.50，調整後 EPS ≥ 共識 3.88–3.99 | Q2 GAAP 1.42 vs 調整後 2.55，差距 1.13；86 天 outage 影響未知 | 觀察中 |
| 資料中心直供制度 | FERC/PJM 不封殺 co-location | 11-16 期限、PJM large-load 裁定未出 | 觀察中 |
| 併購後槓桿可控 | 淨負債/EBITDA < 3.5x，利息保障 > 5x | 2.9x / 7.5x | 成立 |

四根支柱只有一根成立，其餘三根都要等財報與監管事件才能判定，這正是 REJECT 的核心原因。

## 論點失效條件
與 Stop 分開（目前無部位，故無 Stop；以下是「日後不再考慮做多」的論點紀律）。
- 若 Q3 財報 OCF 減 capex 後 FCF 為負（連續第三季），且管理層未給出 capex 高峰結束的季度 → 現金流支柱失效，撤銷做多重訪，轉 SHORT_OR_AVOID 評估。
- 若全年調整後 EPS 指引下修至 USD 11.50 以下，或 Q3 調整後 EPS 低於 3.70 → 盈餘支柱失效。
- 若 FERC 在 11-16 前後裁定 co-location 負載須全額承擔輸電費用、或 PJM large-load 裁定禁止 behind-the-meter 直供 → 制度支柱失效。
- 若 Q3 淨負債/TTM EBITDA 升破 3.5x 或利息保障跌破 5x → 槓桿支柱失效。

## 重訪條件（什麼會改變 REJECT）
- Q3 FCF 轉正 **且** 維持或上調 USD 11.50–12.50 指引 **且** 財報後收盤站穩 MA200（$279.67）→ 重新跑 trade card，LONG、conviction MEDIUM、Small（起始 ≤2% NAV），停損回到 $247.20 下方。
- 財報後若跌破 $247.20 並收在 $240.51 之下 → 評估 SHORT，不急於搶反彈。

## Monitoring trigger
若 11-06 VST 財報導致 CEG 在自身財報前單日跌幅超過 1.5×ATR（約 $17）並跌破 $247.20，代表同業重定價先於基本面，重訪時以 $240.51 為新結構參考，不以舊區間判讀。

## Catalyst calendar
- 2026-11-06 — VST Q3 財報（同業情緒傳導）
- 2026-11-09 — CEG Q3 2026 財報（預估，未經公司確認；另一來源列 11-06）
- 2026-11-16 — FERC co-location 合規期限；約略同期除息日
- 2026-12（日期未定）— PJM 2029/30 容量拍賣

FINAL DECISION COMPLETE
