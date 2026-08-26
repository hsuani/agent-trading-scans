# Sector report — semi as of 2026-08-17

##覆蓋範圍說明
9 檔中 6 檔完成完整 Phase 1-4 流程：MRVL（既有持倉，強制走完整流程）、AMD、ASML、MU、NVDA、TSM。3 檔為 Phase-1-only stub（未達 ≥3/5 正面信號門檻，未進入 Phase 2-4）：ARM（2/4）、AVGO（2/4）、CBRS（1/4）。本輪 6 檔完整流程中，**全部**因 market.md 連續 `PRICE_DATA_UNAVAILABLE` 而無技術面驗證，故除 MRVL（沿用既有持倉敘述性參考價）外，其餘 5 檔皆無 Entry/Stop/Target 數字。

## Ranking table
| Rank | Ticker | Verdict | Conviction | R:R | Size | Horizon | Trigger |
|------|--------|---------|------------|-----|------|---------|---------|
| 1 | ASML | BUY | M | N/A（無報價） | 0.75% NAV 起始倉，硬上限 2% | 3-9 個月 | MATCH 法案表決／商務部調查升級 |
| 2 | MRVL | HOLD（既有倉減碼至 80-85%） | M | 1.2 | Medium | 週度至季度 | 8/27 財報資料中心占比 <76% 或毛利率 <60% |
| 3 | TSM | HOLD（本輪不建倉） | M | N/A | 待恢復後 1/3 目標倉 | 數週至數季 | 9 月營收 YoY <35% 即證偽 |
| 4 | MU | HOLD（0% 曝險） | M（方向）/L（可執行） | N/A | 0%，恢復後 1/4 倉 | 數週至數季 | 反算 Forward P/E >60x 則下修門檻 |
| 5 | NVDA | HOLD（既有倉續抱，新資金 0） | M（長線）/L（短線） | N/A | 0% 新資金 | 1-2 週 | 連兩期資料未恢復即主動降至核心規模 |
| 6 | AMD | HOLD（不建新倉） | L | N/A | 0%（可選 call spread 0.3% NAV） | 數週至 1-2 季 | Forward P/E 反算 >90x 則減至半倉 |
| — | AVGO | Phase-1 stub（AVOID） | — | — | — | — | VMware CVE-2026-59310 客戶流失數據 |
| — | ARM | Phase-1 stub（AVOID） | — | — | — | — | Goldman 下修後續、監管調查結果 |
| — | CBRS | Phase-1 stub（AVOID） | — | — | — | — | 盈利轉正路徑、P/S 回落至 <20x |

## 共識首選
**ASML**。是本輪唯一 BUY，MODIFY 裁決核准 0.75% NAV 起始倉。論點結構性且非仰賴財報前後的短期波動：backlog >€40B、能見度 12-18 個月，且 TSMC capex 上修至 $640 億、SK Hynix $80 億協議為近期多來源交叉驗證的硬催化劑。主要風險 MATCH 法案為單一二元事件，已設定明確重評觸發，不依賴技術止損。

## Contrarian pick
**AVGO**（Phase-1 stub，未進 Phase 2-4，非本輪可執行部位，僅列為觀察名單的不對稱標的）。基本面（營收 YoY +44%、AI 營收 +143%、毛利率 65-67%）與估值（Forward P/E 25-30x，PEG 0.6-0.7）雙雙 PASS，遠優於 ASML/TSM/MU 等目前敘事性溢價更高的同業，僅因 VMware CVE-2026-59310 資安事件（361+ 企業受害）拖累新聞面與情緒面判定為 FAIL 而暫不進場。若客戶流失數據未如headline 般惡化，此為全板塊估值最便宜、基本面最乾淨的名字，一旦情緒面轉正即可能是補漲最快者。

## Pairs trade idea
Long ASML / 對沖 MRVL 減碼部位。ASML 論點時間軸長（3-9 個月，backlog 驅動，不依賴單一財報），MRVL 則同時面對 8/26（NVDA）與 8/27（自身）雙財報周的短期二元事件風險，final decision 已裁定強制減碼至 80-85%。以 ASML 新倉承接方向性曝險、同時執行 MRVL 減碼，是用板塊內兩種截然不同的催化劑時間軸互相分散單一事件曝險，而非傳統意義上的 long/short 對沖（本輪板塊無 SELL 標的）。

## Sector-wide observations
- **共同催化劑**：2026-08-26 NVDA Q3 FY2027 財報是本輪跨 NVDA、AMD、MU、TSM、MRVL 五檔共同引用的最大單一事件，Q4 指引是否破 $100B、毛利率是否守 75% 為板塊 beta 錨點。
- **共同風險**：market.md 資料源（yfinance 代理）於 6 檔完整流程與 3 檔 stub 中**全數**回報 `PRICE_DATA_UNAVAILABLE`，代表本輪整個板塊無一檔具備獨立驗證之技術止損。此為基礎設施風險，非個股訊號，優先於任何個股催化劑。
- **擁擠交易**：AI capex 多頭敘事高度一致（TSM 18 買 0 賣、MU 41 買 0 賣分析師共識），共識方向本身已隱含擁擠風險；MATCH 法案（ASML）與 RISC-V 侵蝕/反壟斷調查（ARM）屬市場尚未充分定價的板塊尾部風險。
- **相關性群組**：NVDA-MU-MRVL-TSM-AMD 同屬 AI GPU/HBM/晶圓供應鏈，且共同錨定 8/26 NVDA 財報，短期相關性高，勿在此群組內疊加曝險視為分散。ASML 屬半導體設備上游，催化劑（MATCH 法案、SEMI 展望）與此群組獨立性較高，是本板塊內少數的真分散標的。

## Action sequencing
1. **MRVL** 先執行 — 減碼至 80-85% 為強制風控指令，時效性最高（8/26-27 雙財報周迫近）。
2. **ASML** 次之 — 0.75% NAV 起始倉為本輪唯一新資金部署，待數據源恢復後補完整 Setup 再考慮加碼至 2%。
3. 其餘 HOLD（NVDA、AMD、MU、TSM）暫不動作，僅設定各自 monitoring trigger 待財報／營收數據驗證。
4. AVGO/ARM/CBRS 維持觀察名單，無操作。

## Sector risk budget
本輪唯一核准的新增曝險為 ASML 0.75-2% NAV；既有 NVDA/AMD/MU/TSM 部位不變、MRVL 部位下修至 80-85%。鑑於 AI capex 群組相關性高且技術止損全數缺位，建議板塊總曝險（新增+既有）上限暫控在 **8% NAV**，並優先待 market.md 報價恢復後重建各檔獨立止損，再評估是否放寬。

SECTOR REPORT COMPLETE
