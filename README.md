[README(1).md](https://github.com/user-attachments/files/32581581/README.1.md)
# Index Integrity — Deflation, Substitution Bias & Goodhart

## Objective

Build and validate tools that preserve the meaning of economic indexes and product metrics, from base-year wage deflation to inflation-rate comparisons and engagement monitoring.

## Methodology

- Diagnosed four errors in a nominal-wage deflation pipeline: base-year selection, date alignment, missing observations, and an output-unit error that mislabeled values scaled to the CPI's 1982–84 reference as 2020 dollars.
- Corrected the pipeline to use the average CPI in the chosen base year, match wage and CPI observations by month, and return only nonmissing values. Packaged the tested `deflate_series()` function in `deflation_utils.py` for reuse.
- Aligned unadjusted CPI-U (`CPIAUCNS`) with unadjusted Chained CPI-U (`SUUR0000SA0`), rebased both to December 1999 = 100, and compared their compounded average annual inflation rates.
- Simulated an engagement intervention and monitored DAU/MAU alongside time per session. Compared correlations before and after the intervention and built an interactive monitor with a start-date selector, CPI-U series toggle, and rolling-correlation window.

## Key Findings

- CPI-U increased at **2.61% per year**, versus **2.35% per year** for C-CPI-U: an **upper-level substitution gap of 0.27 percentage points per year** after rounding. The **0.50 index points per year** difference in index levels is a different unit and cannot be interpreted as an inflation-rate gap.
- The correlation between DAU/MAU and time per session shifted from **+0.93** during organic growth to **−0.96** during the simulated gaming phase. DAU/MAU continued to rise while session duration fell, signaling that increased activity did not necessarily mean better engagement.
- The monitor makes the CPI comparison period and rolling-window sensitivity explicit. A negative rolling correlation is an investigation trigger, not proof of causation; teams should examine notification changes, retention, and meaningful user actions before attributing the decline to gaming.

*The latest C-CPI-U observations may be preliminary and subject to revision. The seasonally adjusted CPI-U toggle is useful for sensitivity checks; the unadjusted series provides the like-for-like comparison with C-CPI-U.*
