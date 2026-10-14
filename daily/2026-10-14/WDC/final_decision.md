FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — WDC as of 2026-10-14

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

WDC 不在 held_tickers.txt, 屬新倉評估 (框架 A)。Trader 的「財報前 0% 新倉」核准; 修改的是 investment_plan 裡「財報確認後直接加到半倉至標準部位」的後續計畫, 以及 risk debate 中沒人察覺的 R:R 缺陷: 以 $410 進場、$365 停損、T1 $431.56 計算, R:R 只有 0.48, 根本過不了 LONG ≥1.5 的門檻。下方交易卡為**條件式**, 10-22 財報 trigger 未兌現前不啟動。Aggressive 提議的 call spread 不採納: 無可驗證的選擇權報價, 無法定義實際 R:R。

## Final trade card (條件式, 財報後才啟動)
| Field | Value |
|---|---|
| Direction | LONG |
| Entry zone | $405.00 – $412.00 (財報後收盤站上 MA200 $407.95 且量能放大, 隔日分批) |
| Stop | $383.00 (收盤確認; 跌回財報前價位代表跳空失敗) |
| Target 1 | $451.52 (MA50) |
| Target 2 | $480.00 |
| Size | Small (約 1.0% NAV, 相當於 3/8 標準倉; 收復 MA20 $431.56 後可加至半倉) |
| Horizon | 事件窗口至 10-28 FOMC; 轉 LONG 後 1–3 季 |
| Conviction | M |
| R:R to T1 | 1.7 (以 $409 中點計) |

## Risk debate adjudication
- Aggressive's strongest point: 等「收回 MA200 確認」等於付 7–13% 的確認費, 基本面硬數據 (normalized 淨利 +79%、FCF 35.1 億、淨現金轉正) 確實偏向多方。
- Conservative's strongest point: 盤中低點 $358.26 當停損不穩健; 從 0% 一步跳到半倉是用單一二元事件決定大額曝險; EPS 基準 (33.09 vs 20.52) 未釐清前「估值便宜」不可作為加碼理由。
- Net: I weight **neutral** more here because beta 2.17、ATR 6.8% 的標的在財報前持現股, 跳空會直接貫穿停損 (gap-through), aggressive 的「停損不收緊」在此情境下不提供保護; 但 conservative 要求對試單再做 STX/SOXX 對沖是雙重防禦, 成本不成比例。Neutral 的分批與收盤確認架構最合理, 我只修正它的停損與 T1 使 R:R 達標。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 營運現金創造能力 | FCF margin >20%, 去槓桿持續 | FCF 35.1 億、margin 27.2%、債務 47.1→10.5 億、淨現金轉正 | 成立 |
| HDD 定價週期未過高峰 | 非 GAAP 毛利率守住 55–56%, FY27 Q2 指引續升 | 最新季 54.1%, 等待 10-22 驗證 | 觀察中 |
| 盈餘品質 | 65 億出售業務收益有合理對應 (SNDK 以債換股處分) | 10-Q 尚未核實, 季度現金減少 16.6 億 | 觀察中 |
| 技術結構反轉 | 放量收回 MA200 $407.95 | 股價 $380.71 低於 MA20/50/200, MACD 柱狀體連三日擴大為負 | 已失效 (故現在不進場) |

## 論點失效條件
必須可證偽, 且與 Stop 分開 (Stop 是價格紀律, 這裡是論點紀律)。
- 若 10-22 非 GAAP 毛利率 < 55%, 或 FY27 Q2 營收指引中點低於 Q1 實際值, 定價週期支柱失效 → 條件卡作廢, 維持空手, 不得以「跌深」為由進場。
- 若管理層在電話會議承認 hyperscaler 訂單遞延或取消, 或 STX 財報表示近線 HDD ASP 環比下滑 → 同上, 條件卡作廢。
- 若 10-Q 顯示 65 億收益無對應的 SNDK 持股處分或債務減少, 而季度現金減少無法解釋 → 盈餘品質支柱失效, 即使已依條件卡進場, 全數出場不等 Stop。
- 若已進場後, 連續兩季 HDD 營收 YoY < 15% → 週期論點失效, 出場。

## Monitoring trigger
If STX 財報 (10-22 前後) 先行揭示 HDD 定價轉弱, 或 WDC 財報前收盤跌破 $358.26, 條件卡直接作廢, 不再等 10-22。If 財報前無新訊息下股價站回 MA20 $431.56, 重新評估是否以較小規模 (1/4 倉) 提前進場, 停損改 $383。

## Catalyst calendar
- 2026-10-22 (收盤後) — WD FY27 Q1 財報與電話會議: 營收 $4.1B 中點、毛利率 55–56%、FY27 Q2 指引、SNDK 殘餘持股會計處理。
- 2026-10-22 前後 (日期未確認) — Seagate (STX) 財報: 同業 HDD 需求與 ASP 驗證。
- 2026-10-28 — FOMC 利率決議: beta 2.17 放大效應, 鷹派意外為下行風險。
- 財報後 10-Q 申報 — 核實 65 億收益與現金流對應。

FINAL DECISION COMPLETE
