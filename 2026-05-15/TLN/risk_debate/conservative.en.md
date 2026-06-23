# Conservative risk view — TLN

## Where trader is too aggressive
- **Stop too tight given vol.** ATR14 $18.44 and 20d annualized vol 59% means a 3% ($10.88) stop from $352.88 to $342 is barely 0.6 ATR — well inside daily noise. Probability of intraday whipsaw stop-out before 5/18 PJM headline is high. A vol-adjusted 1.5x ATR stop would sit ~$325, but that conflicts with the $343/$310 support architecture — meaning the stop level is *structurally* right but *statistically* fragile. Sizing must compensate.
- **Sizing not vol-adjusted to risk-of-ruin.** 1.5% NAV at $352.88 entry with ATR $18.44 implies the position will see ±$18/day swings on ~85% of NAV-position-value; in a 59%-vol single name, Medium is the upper bound, not the natural choice.
- **Catalyst risk underweighted.** 5/18 PJM refile is a binary 3-day-out headline. Adding the second tranche *on* a constructive read is correct, but a 60% first tranche pre-catalyst is overcommitted — should be 40/60 not 60/40.
- **Sector co-move blind spot.** Beta 1.67, plus cohort-wide nuclear sell-off on 5/07 despite strong VST print, shows TLN trades as a basket. Stop at $342 can be hit purely by VST/CEG/SMR cohort drawdown, not TLN-specific news.
- **Leverage tail underpriced.** Net debt $6.12B, ND/normalized-EBITDA ~10x, equity $1.09B (P/B 14.8x). Any FY26 guide trim doesn't compress P/E linearly — it re-prices the equity stub. Forward P/E 10.3x implies $34 EPS; a 20% guide cut on leveraged equity is a 40-50% drawdown, not 20%.

## Tail scenarios
- **Scenario A (25%) — 5/18 PJM language ambiguously hits front-of-meter PPAs**: gap to $320, stop $342 skipped on open. $ loss = (352.88−320)×shares ≈ 9.3% of position × 1.5% NAV = **~0.14% NAV** if stop honored at $320, but slippage realistic to $315 → ~0.16% NAV.
- **Scenario B (15%) — Sector co-move with VST earnings miss / Oklo miss week of 5/18**: TLN -8% on cohort beta despite no TLN news → $325, stop $342 hit cleanly. $ loss = (352.88−342)×shares = **~0.046% NAV** (clean stop).
- **Scenario C (10%) — Hyperscaler capex pause headline (AMZN/MSFT)**: -15% gap to $300, stop skipped. $ loss = (352.88−300)/352.88 = 15% × 1.5% NAV = **~0.22% NAV**.
- **Scenario D (5%) — Susquehanna outage slip / transmission reconfig delay**: -12% to $310, $ loss ~**0.18% NAV**.
- **Aggregate left-tail (~10% combined gap-through)**: expected $ loss ~0.18% NAV, but psychological/sequencing damage if it stacks with other longs.

## Recommended adjustments
- **Size**: Medium 1.5% → **Small-Medium 1.0% NAV** (rationale: 59% vol, 10x leverage, binary 5/18 in 3 days; preserve dry powder for confirmation add).
- **Stop**: $342 unchanged structurally, but **honor it as daily-close not intraday** to avoid wick whipsaw; emergency hard exit $335 intraday only.
- **Entry**: split **40% now / 40% on 5/18 confirmation / 20% on MA200 $372 reclaim** (not 60/40).
- **Consider**: pair with **partial CEG or VST short** (~25% of TLN $) to neutralize cohort beta through 5/18; or buy June $330 puts (~1.5% premium) as cheap binary insurance.

## Position-level $ risk
If stop hits at $342 from $352.88 entry on 1.0% NAV size: $ loss = (352.88−342)/352.88 × 1.0% = **0.031% NAV**. Acceptable — well inside the 0.05%/1%-sized rule of thumb. On the proposed 1.5% size: 0.046% NAV — still acceptable on a clean stop, but the gap-risk distribution above (Scenarios A/C/D) carries a fatter tail of 0.14–0.22% NAV, which on a Medium book is meaningful when stacked with correlated nuclear/AI-power exposure.

## What I'd push for
Cut size to 1.0% NAV, restructure tranches to 40/40/20 with the first 40% only on a pullback to $348 or lower (don't chase $352.88), defer the second tranche to *after* 5/18 close not into it, and overlay either a CEG short pair or a $330 June put as binary insurance through the PJM headline. The trade thesis is sound; the sequencing is too eager and the cohort beta is unhedged. The same R:R is achievable at lower notional with a survivable left tail.

CONSERVATIVE VIEW COMPLETE
