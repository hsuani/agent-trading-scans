# Conservative risk view — NEE

## Where trader is too aggressive

1. **PRICE_DATA_UNAVAILABLE 使規模計算完全失效**：交易提案提出 Small（0.5% NAV）初始倉，但 ATR14 不可得，無從驗證停損距離是否符合 vol-adjusted 標準。不知真實波動率的情況下，任何規模設定均屬盲目下注，無可追溯根據。

2. **FOMC 9月升息 77% 概率被低估**：投資計畫將升息列為「下行觸發」，卻仍維持 Long 方向。公用事業股對利率的敏感性是非線性的——NEE 的 P/E 溢價（18–22x vs. 行業 14–17x）本質上是債券替代品估值，77% 升息概率等同於高概率倍數壓縮事件，而非邊緣尾部風險。每升息 25 bp，若 20% 債務屬浮動或短期再融資，年利息支出增加約 $4.8 億。

3. **Dominion 合併風險被低估**：全股票交易（0.8:1 換股）已令股價公告後下跌 4.6%。合併需同時通過 FERC、NRC、Virginia、North Carolina、South Carolina 五個機構。Virginia Governor Spanberger 已公開宣布介入——州長正式介入的交易，歷史上有顯著比例最終改變條款或延遲逾 24 個月。倉位計畫未對「交易失敗」情境定義額外減倉機制。

4. **內部人賣出被歸類為「中性」過於寬鬆**：過去三個月 $3.2M 賣出、$0 買入。高層管理人員在信息最充分的位置選擇賣出而非買入，這是明確的偏空警示，不應輕描淡寫為中性。

## Tail scenarios

- **情境 A（概率 25%）：Fed 9 月升息 50 bp 超預期** → P/E 壓縮至行業均值 14x，以 EPS $4.02 計算，隱含目標價約 $56；相較 $89 參考價，下行約 37%。$損失 = 待價格恢復後確認。

- **情境 B（概率 20%）：Dominion 合併遭 Virginia 實質阻止或條款重談** → 合併溢價消失、管理層公信力受損，估計股價測試 $82–$85；若與情境 A 疊加，下行幅度可達 40–45%。

- **情境 C（概率 15%）：IRA 稅務抵免遭聯邦削減** → NEER 部門估值模型高度依賴 IRA 補貼，削減直接壓縮 EV/EBITDA 倍數；NEER 約佔整體業務 40%，估值衝擊達 15–20%。

## Recommended adjustments

- **Size**：Small（0.5% NAV）→ **0% NAV**。理由：PRICE_DATA_UNAVAILABLE 下無法計算 vol-adjusted 規模；FOMC 升息概率 77%、Dominion 監管審查兩項近期催化劑均為負面且具明確時間表。
- **Stop**：待價格恢復後確認（建議設於參考低點以下 2 ATR，具體點位需實際報價支撐）。
- **Entry**：等待 2026-09-18 FOMC 確認暫停升息後，方可考慮建立初始 0.5% NAV 試探倉；不在當前不確定性窗口搶進。
- **Consider**：若強制持有任何倉位，以 XLU 指數 Put 或 TLT Put 部分對沖利率敏感性風險。

## Position-level $ risk

若停損觸發：$ loss = (entry − stop) × shares = **待價格恢復後確認**。

PRICE_DATA_UNAVAILABLE 狀態下 ATR14、年化波動率、合適停損距離均無法計算，損失金額占 NAV 百分比無從評估。**這本身即構成不應建倉的充分理由**——無可量化風險，即無可執行的倉位。

## What I'd push for

當前存在三重疊加障礙，缺一不可解決：其一，PRICE_DATA_UNAVAILABLE 使停損與規模計算均不可執行，建倉等同於盲飛；其二，Fed 9 月升息 77% 概率是具體日期（2026-09-18）的高概率倍數壓縮事件，NEE 的 P/E 溢價是最直接受害者，WACC 若突破 ROIC 下緣（7%），高溢價估值面臨系統性重訂價；其三，Dominion 全股票交易已啟動稀釋，Virginia Governor 公開介入令交易失敗或條款惡化概率不可忽視，內部人 $3.2M 純賣出強化這一判斷。結論：**維持 0% NAV，直至（1）價格數據恢復以供 vol-adjusted 規模計算，且（2）2026-09-18 FOMC 確認暫停升息**。兩項條件均達成後，以 0.5% NAV 試探性建倉，停損設於進場價以下 2 ATR，後續視 Dominion 監管明朗化決定是否加碼至 1.5% NAV。任何在確認前搶跑的行為，其風險/報酬比在當前信息缺口下均不可量化，不符合審慎風控標準。

CONSERVATIVE VIEW COMPLETE
