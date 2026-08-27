# Final decision — QUBT as of 2026-07-21

FINAL TRANSACTION PROPOSAL: **HOLD**

## Verdict
MODIFY —方向性偏多成立，但在 SEC 10-Q 以原始文件核實現金前，**當前倉位為 0%**。交易員的「待觸發 0.25%」實質即零倉，我將其正式化為明確的 0% 觀察狀態，並鎖定條件式建倉路徑。

## Final trade card (if not REJECT)
| Field | Value |
|---|---|
| Direction | LONG（條件式，現金核實後啟動） |
| Entry zone | PRICE_DATA_UNAVAILABLE — 事件觸發：SEC 10-Q（EDGAR 原始文件）確認現金 ≥$1.0B → 次一交易日開盤後掛限價單，不追缺口 |
| Stop | 事件型：10-Q 或 Q2 財報揭露現金 <$200M → 立即清零；NHanced 整合失敗 / $72M 或有對價爭議公開化 → 即時退出 |
| Target 1 | 分析師共識 $18.33（隱含 +120%），觸發：現金確認 + opex/revenue 收斂 |
| Target 2 | 軋空加速情境（27–28% short interest 非線性）估算 +260% |
| Size | 現在 0%；10-Q 確認後 Small 0.25% NAV；Q2 財報再確認 opex/revenue 收斂後上限 0.5% NAV |
| Horizon | 4–6 週核心窗口（至 Q2 2026 財報，8 月）；論述確立可延伸 12–18 個月 |
| Conviction | L |
| R:R to T1 | 不可量化（PRICE_DATA_UNAVAILABLE）；方向性不對稱 +120% 對 −72%，確認後方成立 |

## Risk debate adjudication
- Aggressive's strongest point：不對稱性極大——若 $1.4B 屬實，EV 僅 $300–600M，0.25% NAV 最壞損失僅 ~0.18% NAV，機會成本論述有力。
- Conservative's strongest point：$1.4B（Yahoo/ChartMill 二手轉述）vs $80–120M（fundamentals.md 自承 DATA_UNAVAILABLE 推估）相差 10–17 倍，此裂縫決定整個論述生死，且等待成本為零。
- Net：我在此更重 **conservative**，並以 neutral 的表述紀律收尾。10–17 倍差距遠超正常誤差，非停損可管理的戰術風險，而是結構性二元事實；新聞轉述不等於 EDGAR 法定申報。激進方「先入場搶 alpha」與「10-Q 上傳後幾小時被重估」自相矛盾——若資訊已廣見於 Yahoo，時間優勢本就不存在。零成本可規避的尾部風險，不值得提前承擔。

## Monitoring trigger
若 SEC 10-Q 歸檔且現金經原始文件確認 <$200M（而非 $1.4B），空頭「強制稀釋論」重新主導，P/S 70–140x 面臨 −72% 至 −90% 重估——此為建倉前的一票否決,直接切換 AVOID,不待停損。反向:現金 ≥$1.0B 經 EDGAR 核實，即為建倉扳機。

## Catalyst calendar
- 2026 年 7 月（待定）— SEC 10-Q 歸檔：現金 $1.4B 核實或否定（入場先決條件）
- 2026 年 8 月 — Q2 2026 財報：現金、opex/revenue 比率、NHanced 初期貢獻
- 2026 年 Q3–Q4 — NeuraWave 首份非政府付費商業合約（估值重估觸媒）
- 2026 年 Q3–Q4 — NHanced TFLN 商用原型里程碑（$72M 或有對價路徑）
- 2026 年 7–8 月 — short interest 月度更新（監控是否突破 30%）

FINAL DECISION COMPLETE
