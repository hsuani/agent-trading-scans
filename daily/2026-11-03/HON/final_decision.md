FINAL TRANSACTION PROPOSAL: **HOLD**

# Final decision — HON as of 2026-11-03

## FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY

## 判定框架
HON 不在 `held_tickers.txt` 內, 屬新倉, 走 A 框架: 問題是「該不該進」。結論: 現價 $224.15 不進, 新倉維持 0% NAV。交易員的方向正確, 但原提案保留「放量站上 MA200 即轉多」與「回檔至支撐轉多」兩條路徑, 我只保留後者, 並把條件單規格鎖定為一張卡。理由: 從 $231 追突破、停損仍在 $217 附近, 到 T1 $244 的 R:R 不足 1.0, 不符合進場紀律; 回檔買進才有價格優勢。

## Final trade card (條件單, 未觸發前不持倉)
| Field | Value |
|---|---|
| Direction | LONG (僅於回檔觸發時成立) |
| Entry zone | $216.00 – $218.00 (須當日收盤守住 $216.13) |
| Stop | $211.50 (收盤基準, MA50 $211.80 下方) |
| Target 1 | $230.73 (MA200) |
| Target 2 | $244.00 (分析師目標價區間下緣) |
| Size | Small (1% NAV) |
| Horizon | 數週至 2027-01-28 Q4 財報 |
| Conviction | L |
| R:R to T1 | 2.5 (以 $217 進場計) |

## Risk debate adjudication
- Aggressive's strongest point: 方向性證據 (Q3 beat、兩度上修指引、去槓桿兌現) 品質高於估值論點, 等到放量站上 MA200 才進場等於把最佳風酬比等掉。這點我接受, 所以直接刪除追突破路徑, 而不是降低其門檻。
- Conservative's strongest point: 11/05 Quantinuum 消息有跳空風險, $215.54 的檢視線可能根本無法成交; 在 R:R 無優勢時承擔 Medium 曝險是風險與信心不對稱。這點決定了 Small 規模與不在催化劑前建倉。
- Net: I weight neutral more here because 兩端各有一半正確: 激進方未反駁「現價落在合理區間上段」的估值前提, 保守方 1×ATR 停損在 MEDIUM 信心下會被正常波動洗出。中性方「維持 0%、觸發後 1–1.2% NAV、停損約 1.35×ATR」最貼近我的判斷, 我再把停損下移至 MA50 下方以換取 R:R 2.5。

## 論點支柱
| 支柱 | 當初的預期 | 現況 | 判定 |
|---|---|---|---|
| 指引動能 | FY26 指引持續上修, organic 成長 ≥5% | Q3 organic +7%, 10/22 二度上修 (8-K 佐證) | 成立 |
| 分拆後估值 | 現價落在 2027 forward EPS 9.85 × 20–22x ($197–217) 區間內 | 現價 $224 高於區間上緣, forward P/E 22.7–26.6x, PEG 3.04 | 觀察中 (故只在回檔買) |
| 現金轉換 | FY26 FCF 兌現約 2.1B 指引, 轉換率 ≥75% | 9M FCF 0.37B 口徑混雜, Q4 才是首個乾淨季度 | 觀察中 |
| 技術結構 | 站回 MA200, 死亡交叉翻正 | 在 MA20/MA50 之上但低於 MA200 $230.73, 11/02 量僅 0.14x | 觀察中 |

## 論點失效條件
與 Stop 分開: Stop 是價格紀律, 以下是論點紀律, 任一觸發即不等 Stop 動作。
- 若 2027-01-28 Q4 財報公布 FY26 FCF 低於 1.9B (較指引 2.1B 短少逾 10%), 現金轉換支柱失效 → 出場; 未觸發則撤銷條件單。
- 若 FY27 organic 成長指引低於 4%, 或 FY26 指引在 Q4 前遭下修, 指引動能支柱失效 → 出場。
- 若 Q4 Process Automation & Technology 分部利潤率再較 Q3 下滑逾 100bp, 估值支柱轉為失效 → 減碼一半。
- 若條件單觸發前任一日收盤低於 $215.54, 技術結構支柱失效 → 撤銷條件單, 不接刀。

## Monitoring trigger
If 11/05 Quantinuum 消息造成當日跌幅超過 1.5×ATR14 (約 $8) 或 12 月 FOMC 意外升息, 即使價格仍在 $216–218 區間內也暫停條件單, 重新評估後再決定是否恢復。

## Catalyst calendar
- 2026-11-05 — Quantinuum 相關消息/業績
- 2026-11-06 — 美國非農就業數據
- 2026-11-13 — HON 除息
- 2026-12 — FOMC 會議 (升息風險)
- 2027-01-28 (預計) — HON Q4 財報, 驗證 FY26 FCF 與分拆後分部 EBITDA 口徑

FINAL DECISION COMPLETE
