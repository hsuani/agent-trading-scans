# Neutral risk view — AXTI

## Points of agreement (both sides)
- 技術停損 $36.56（距現價 $38.88 僅約 6%）相對 ATR14 $6.89（17.7%）確實過窄，雙方都同意應改用 ATR 尺度停損。
- 現價 $38.88 處於死亡交叉（MA20 $54.59、MA50 $64.00、MA200 $65.44 之上），MOFCOM 11-10／11-27 二元事件未解，此為真正的風險核心，雙方都未否認這點。
- 雙方都不支持現在滿倉直接建立方向性部位——aggressive 僅提升到 Medium（2% NAV）而非 Large，conservative 則主張維持 0 或更低；兩者的落點其實比表面分歧更接近。

## Aggressive overreach
- Where：把 Size 從觀察倉直接拉到 Medium（2% NAV），且主張「現在小部位進場，不等確認」。
- Why：investment_plan 的 crux 不是「過度等待確認」的行為偏誤，而是未解的二元政策事件（11-10／11-27）本身無法被 ATR 停損保護——binary 新聞日常見跳空，停損極可能被跳空穿透而非依序成交。R:R 計算（risk $6.89 vs. 到 $50.57 的 $11.69，R:R≈1.70）只採多頭情境，未對稱納入 conservative 提出的「跌破 $36.56 續跌至 $30 附近」情境（Scenario A），屬選擇性引用，低估尾部風險。同時提議現股加碼 call spread，等於對同一催化事件重複曝險，並非真正分散風險。

## Conservative overreach
- Where：主張觀察倉上限由 Small（0.5% NAV）進一步砍到 0.25% NAV 或直接空手，且要求兩觸發條件同時且量化確認才進場。
- Why：這會使 1–3 週的觀察期內即便 MOFCOM 結果明朗、價格放量收復關鍵區，也可能因「量化門檻」未定義而持續延後進場，重蹈 aggressive 批評的「等到全部確認、股價已貴」的問題；conservative 自身也沒有為此設定明確的量化標準，只是把決策門檻推得更高，並非真正解決。Tail scenario 的 40%／25%／15% 機率屬主觀賦值，文件中並無依據，精確度有被高估之嫌。

## Balanced adjustment proposal
- Size：維持 trade_proposal 原定上限 Small（0.5% NAV），不採 aggressive 的 Medium（2% NAV），亦不須砍到 conservative 的 0.25% 或空手；此倉位僅用於承接 11-10 結果明朗後的初始反應，非全倉方向性賭注。
- Stop：採 ATR 尺度，入場價 $38.88 − 1×ATR14 $6.89 ≈ $31.99（取代過窄的 $36.56），與雙方共識一致。
- Entry：不要求提前搶跑，但也不要求「放量收復 MA20 $54.59 + 10-Q OCF 轉正」雙重確認全部到齊；改為單一明確觸發——MOFCOM 公告結果後、股價收盤站回 $50.57 支撐轉壓力區下緣即可用 Small 倉位試單，10-Q 現金流作為加碼（而非初始進場）的條件。
- Hedge：初始曝險優先採用 aggressive 提出的 $40/$55 call spread（12 月到期，涵蓋兩個 MOFCOM 公告日），以權利金封頂下行風險，取代現股承擔跳空缺口；待事件結果明朗後再視情況轉為現股並套用 ATR 停損。
- Time horizon：1–3 週觀察 MOFCOM 與 10-Q 揭露，論點本體仍屬季度級別，須待 2027-02 Q4 財報驗證。

## Net $ risk if stop hits
以 Small（0.5% NAV）、ATR 停損 $31.99 計，每股風險 $6.89（17.7%）。每 $100,000 NAV 約承擔 $88.5 風險（= 0.0885% of NAV）；若改用 call spread 承接，下行風險封頂於權利金成本，低於上述現股數字。

## Net $ upside at T1 / T2
T1（$50.57 支撐轉壓力區下緣）：每股獲利 $11.69（30.1%），每 $100,000 NAV 約 $150.5（0.1505% of NAV）。
T2（MA20 $54.59）：每股獲利 $15.71（40.4%），每 $100,000 NAV 約 $202（0.202% of NAV）。
對應 R:R 分別約 1.70 與 2.28，與 investment_plan 設定的 long 門檔 1.5 相符，支持小倉位、ATR 停損、事件確認後進場的折衷方案。

NEUTRAL VIEW COMPLETE
