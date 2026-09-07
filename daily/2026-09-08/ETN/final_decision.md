FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — ETN as of 2026-09-08

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

> 部位判定：ETN **不在** `held_tickers.txt` 內 → 新倉框架。問題是「該不該進」，答案是**現價不進股票**，但核准一筆有條件、定額保費的 call spread 作為催化劑曝險。

## 決策結果與信心度
- **決策結果**：HOLD（股票不建倉；有條件小額 options）
- **信心度**：**72% conviction**（對「現價不建股票倉」這個結論的信心；對 options 有條件執行的信心僅 55%）

## Final trade card
| Field | Value |
|---|---|
| Direction | LONG（僅限 defined-risk call spread；股票 NO ENTRY） |
| Entry zone | 股票 **N/A**（條件性 $390–$405，需觸發條件全數成立）；Options $440/$475 call spread，到期 2026-10-16 |
| Stop | Options 無 stop（保費即最大虧損 ≤$2,400）；條件性股票倉 **$370**，收盤破 $385 先減 50% |
| Target 1 | $475（共識目標 $474.65） |
| Target 2 | $530 |
| Size | 股票 **0% NAV**；Options 保費 **≤0.24% NAV**（3 contracts，每 spread ≤$8） |
| Horizon | Options 至 2026-10-16；股票入場後 1–3 個月 |
| Conviction | M |
| R:R to T1 | 股票 @$430 **1.1x（不合格）**；Options **3.4x（合格）** |

## Risk debate adjudication
- **Aggressive 最強論點**：call spread 的下行嚴格鎖定在保費，結構上比 0.5% NAV 股票倉更保守，卻能吃到 Q3 業績二元事件 45% 機率的牛市情境。放棄整個 options 視窗確實是主動放棄 alpha。
- **Conservative 最強論點**：39 位分析師 0 賣出評級 + trailing P/E 31.8x = 容錯率近乎為零；任何小幅不達標會引發連鎖降評與非線性壓縮。Heath Monesmith $826 萬套現是全場質量最高的反向信號。
- **Net**：我採 **neutral** 為主。理由是 PRICE_DATA_UNAVAILABLE 這件事本身就是裁決依據——aggressive 的「搶在 IV 抬升前入場」前提無法驗證，用未確認的保費估算下注等於把模型風險疊加在市場風險上；但 conservative 把定額保費結構與持股 gap-down 敞口一刀切也不成立。3 contracts、報價確認為前提，是唯一站得住的中間解。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 資料中心/電網結構性需求 | 訂單 YoY 高成長、多年能見度 | 2026 訂單 +240% YoY，FERC 206 條與 DOE 傳輸研究提供政策尾風 | 成立 |
| Grid-to-chip 稀缺定位 | Boyd 液冷 + NVIDIA Beam Rubin DSX 端到端 | 定位屬實，但協同效應與液冷毛利率尚未披露 | 觀察中 |
| 估值安全邊際 | 有折價或合理倍數 | $430 / FY26E EPS $13.50 = P/E 31.8x，PEG 1.7–2.0，上行僅 +10.4% | **已失效** |
| 內部人與機構信號一致 | 管理層與分析師同向 | Electrical Americas 總裁 8/11 套現 $826 萬，管理層淨賣出 | **已失效** |

四根支柱中兩根已失效，且失效的兩根正是決定「現在進場划不划算」的那兩根 —— 這是股票 NO ENTRY 的直接依據。

## 論點失效條件（與 Stop 分離）
- 若 Q3 2026 **Electrical Americas 毛利率跌破 26%** → 成長支柱失效，取消所有條件性入場，options 到期不續。
- 若管理層**下調** FY2026 有機成長或 EPS 指引（低於 $13.40）→ 出場，不等價格。
- 若 Meta / Google / Amazon 任一於 Q3 財報公佈 **2027 資料中心 capex 削減 ≥20%** → 熊市基本情境啟動，直接放棄本標的至下一季。
- 若再有電力部門高管或 CEO/CFO **單筆逾 $500 萬**賣出 → 內部人支柱二次確認失效，永久移出候選名單本季。
- 若 Boyd 首年整合一次性費用超管理層預估 **30%** → 護城河支柱失效。

## 關鍵催化劑
- **2026-09 中下旬** — Q3 2026 業績（唯一近期高質量催化劑）
- **2026-10-16** — call spread 到期日
- **2026 Q4** — Boyd Thermal 液冷毛利率首次正式披露
- **2026 Q4** — Meta / Google / Amazon Q3 財報中 2027 capex 指引
- **2026 Q4–2027 Q1** — Beam Rubin DSX 大型客戶合約（目標 2–3 件）

## 風險因子
- P/E 31.8x 無估值緩衝，加權期望值為負（-$5 至 -$15）
- 業績跳空 gap-down 可越過 $370，實際損失遠超理論停損
- 0 賣出評級 = 連鎖降評的系統性脆弱性
- +240% 訂單基數必然造成 2027 增速懸崖，市場可能提前定價
- PRICE_DATA_UNAVAILABLE：所有水位與 ATR 均為估算，倉控缺乏客觀錨點

## Phase 1 評分表
| Signal | 判定 |
|---|---|
| 趨勢 / 動能（52 週 +23.4%） | ✅ |
| 估值（P/E 31.8x、PEG 1.7–2.0） | ❌ |
| 基本面成長（有機 +14%、指引連續上調） | ✅ |
| 內部人 / 資金流（總裁套現 $826 萬、管理層淨賣出） | ❌ |
| R:R 至 T1（1.1x < 1.5x 門檻） | ❌ |

**2/5 通過 → 不足以支持股票新倉。**

## 執行建議
1. **本週股票零操作。** 不試探、不建底倉。
2. **Options 僅在 2026-09-09 收盤前同時滿足下列全部條件才執行**：(a) 取得 ETN 實時報價；(b) IV percentile < 50%；(c) 每 spread 保費 ≤$8。三者缺一 → 本週不動作，整個 options 方案作廢，不延後、不放寬。
3. **2026-09-15 起（業績前 72 小時）為「業績前禁止操作區」**，任何形式新倉一律禁止。
4. **業績後才是真正的決策點**：需同時見到有機成長 >15.5%、調整後 EPS >$3.56、管理層上調指引，且股價收盤站穩 $415 以上，方以 0.5% NAV 起始建股票倉並同步買入 Q4 $400 put 對沖。
5. **回落路徑**：若無基本面惡化而自然回落至 $390–$405，可直接依條件性參數建倉（R:R 3.2x）。

## Monitoring trigger
若 ETN 在無明顯消息下**跌破 $400**（機構出逃訊號），或 Q3 業績日期正式公告落在 09-15 之前，於 stop 觸發前重新評估整份決策。

FINAL DECISION COMPLETE

FINAL TRANSACTION PROPOSAL COMPLETE
