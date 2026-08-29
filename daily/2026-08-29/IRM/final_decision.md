FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — IRM as of 2026-08-29

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
REJECT

> 倉位判定：IRM 不在 `held_tickers.txt` 內，屬**新倉決策**。REJECT 指「本輪不建倉、資金配置 0%」，非賣出訊號（無部位可賣），故第一行為 HOLD（不動作）。
> **PRICE_DATA_UNAVAILABLE** — yfinance 代理封鎖（403），無即時報價，不提供 entry / stop / target 數值。

## 決策參數（無部位）
| Field | Value |
|---|---|
| Direction | 不建倉（新資金 0%） |
| Entry zone | PRICE_DATA_UNAVAILABLE |
| Stop | PRICE_DATA_UNAVAILABLE |
| Target 1 / 2 | PRICE_DATA_UNAVAILABLE |
| Size | 0% NAV（觀察名單） |
| Horizon | 3–6 個月，2026-10-29 Q3 財報為決策節點 |
| Conviction | M（方向信念 ~60%，但「現在進場」信念僅 ~30%） |
| R:R to T1 | 0.3（+10.7% vs. −34%）— 低於 Long 門檻 1.5 |

## Dealbreaker（明講）
不是基本面看空，而是**進場條件不成立**：(1) 30 天 +26%、YTD +45% 後，共識目標僅剩 +10.7% 上行，而 P/AFFO 由 21x 壓縮至 14x 的下行達 −34%，R:R 約 0.3:1；(2) 無即時報價，Stop 與部位風險無法量化，任何「先建 1/3 倉」都是無錨下單。兩者疊加，等待的機會成本遠低於錯誤定價的成本。

## Risk debate adjudication
- **Aggressive 最強論點**：以分析師共識當上行天花板確實壓低了分子；若 AFFO 續增 17% 且倍數向 22–24x 擴張，上行可達 +30–35%，R:R 會翻轉。這點成立，但**發生在 Q3 驗證之後**，不是現在。
- **Conservative 最強論點**：MA200 + 「基本面惡化確認」的雙重停損等於吃完整段下行才出場，紀律形同虛設；PRICE_DATA_UNAVAILABLE 下無法算 $ risk。
- **Net**：我採 **neutral** 為主。理由：Conservative 把資料中斷升格為基本面否定、把 Mark Kidd 賣股當結論性反向證據，權重過重；Aggressive 用 EQIX 平價（28–30x）當常態目標，IRM 歷史從未到過該區間。Neutral 的分割最準確——**論文成立，但時機不成立**，故配置歸零而非否定標的。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| DC 租賃動能 | YoY >30% | Q2 +39%，YTD 110 MW 已超全年 100 MW 目標 | 成立 |
| ALM 第三引擎 | 年營收近 $1B | Q2 YoY +88%，跨境併購擴張中 | 成立 |
| 估值有擴張空間 | P/AFFO 21x → 24x+ | 漲幅已吸納利多，上行僅剩 +10.7% | 觀察中 |
| Matterhorn 融資不稀釋 | 負 FCF 下維持槓桿與信評 | 淨槓桿 5.5–6.5x、2027–2030 capex $10–15 億/年 | 觀察中 |

## 論點失效條件
- 若 Q3 2026 單季 DC 新簽租賃 <20 MW，或連續兩季 DC 營收 YoY <30% → DC 動能支柱失效 → **永久移出觀察名單**。
- 若 Moody's / S&P 下調至 BBB– 以下，或公告 Matterhorn capex 超原計劃 20% 以上 → 融資支柱失效 → **移出觀察名單**。
- 若 30 年期公債殖利率突破 5.5% 且維持逾 20 個交易日 → 估值支柱失效 → **移出觀察名單**。
- 若 Mark Kidd 在非 RSU 到期視窗出現大額公開市場賣出 → 加重反向權重 → **建倉門檻上調**。

## Monitoring trigger
下列**兩項同時**滿足才重啟建倉評估（首批 0.75% NAV，Stop 設於 MA50 有效跌破 + 量能 >20 日均量 150%）：
1. 報價恢復且股價回調至 MA50 附近並有量能支撐；
2. Q3 財報 DC 租賃 ≥30 MW（排除孟買 51 MW 一次性效應）。

## Catalyst calendar
- 2026-10-29（預計）— Q3 2026 財報：DC 租賃 MW、AFFO per share、全年指引
- 持續 — Project Matterhorn 超大規模客戶長約公告
- 持續 — 高管 Form 4（Mark Kidd 是否轉買入）
- 持續 — FOMC 決議與 30 年期公債殖利率 5.5% 關鍵位

FINAL DECISION COMPLETE
