# Neutral risk view — VRT

## Points of agreement (both sides)
- 雙方都認為 trade_proposal 目前「維持現有規模、被動等待 $275.12 停損觸發」的作法對 85.49% 年化波動、財報前 14 天的環境而言太被動——單一硬停損在財報跳空情境下保護效力有限，這點論據充分（ATR14 $20.81，$275.12 距現價僅 1.37×ATR）。
- 雙方都認同 7/22 GEV 財報是有效的免費領先指標，應被納入決策而非僅作觀察。
- 雙方都認同分批 / 分層機制優於單一觸發點（不論是分批停損或分批建倉）。

## Aggressive overreach
- Where：主張財報前即以現股或選擇權建立試探倉位（含 $310/$360 call spread）。
- Why：investment_plan.md 明確判定為 NEUTRAL、MEDIUM conviction，核心矛盾（估值定錨 $6.35 vs $8.87）尚未收斂，這不是「該下小注」的訊號收斂情境，而是雙方論點都站得住腳的真實不確定性。選擇權雖將損失鎖定在權利金，但把「連四季超預期」當作第五次同樣會超預期的依據是代表性偏誤（recency bias），trailing P/E 76.86x 已隱含極高預期，超預期後仍可能因指引措辭保守而下跌（即「利多出盡」），凸性論點並不能消除方向判斷本身的錯誤機率。

## Conservative overreach
- Where：要求既有部位「財報前一週內主動減碼至少 1/3」為唯一可接受做法，並將 54% 跌幅的極端熊市估值錨（$139.70）當作常規尾部情境權重納入部位規模計算。
- Why：$139.70 是保守指引 EPS $6.35 隱含的下限情境，機率遠低於 base case，用它來說「vol-adjusted sizing 低估風險 2-6 倍」誇大了帳面停損與尾部風險的落差；且 trade_proposal 本就已排除新倉，conservative 的「至少 1/3」是武斷的固定比例，未附帶漸進邏輯，不如其自己提出的分批停損機制精細。

## Balanced adjustment proposal
- Size：不建新倉。既有部位不強制固定減碼比例，改用分批停損自然降低曝險；若同時持有 GEV/ETN 等同題材曝險，應合併計算風險桶位（採納 conservative）。
- Stop：分批停損——跌破 $290 先減 1/3，跌破 $275.12 全數出清（採納 conservative，較單一硬停損更貼合跳空風險）。
- Entry：財報後轉 LONG 需站上 MA20 $316.61 且連續 2 日收盤確認 + 量能放大（採納 conservative，理由是估值分歧未收斂前，單日站上易被雙巴）。
- Hedge：若想保留財報上行參與，可用 <0.5% NAV 的小額衛星倉位（如 aggressive 提議的 $310/$360 call spread）投機下注，但明確定位為投機資金而非核心部位邏輯的替代（部分採納 aggressive，僅限已知最大損失且規模極小）。
- Time horizon：數週，7/29 財報為關鍵決策節點。

## Net $ risk if stop hits
以 aggressive 提議的 1.5% NAV 衛星倉位為例（NAV $100,000 → 名目部位 $1,500），分批停損下加權平均損失約 -7.75%（優於單一停損 -9.36%）＝ $116（NAV 的 0.12%）。

## Net $ upside at T1 / T2
T1（base case $388.67，+28%）＝ $420（NAV 的 0.42%）；T2（bull case $500，+64.7%）＝ $970（NAV 的 0.97%）。

NEUTRAL VIEW COMPLETE
