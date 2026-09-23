"""Deflation utilities for ECON 5200 labs."""

import pandas as pd


def deflate_series(nominal, cpi, base_year=2020):
    """Convert a nominal time series to real (constant-dollar) values.

    Parameters
    ----------
    nominal : pd.Series
        Nominal values indexed by date.
    cpi : pd.Series
        CPI values indexed by date, at the SAME frequency and with the SAME
        seasonal adjustment as `nominal`.
    base_year : int
        Year whose dollars to express values in. The base is that year's
        average CPI.

    Returns
    -------
    pd.Series
        Real values in base_year dollars, on the dates both inputs share,
        with no missing values.

    Raises
    ------
    ValueError
        If base_year is not present in the CPI index, or if the two series
        share no dates.
    """
    if not (cpi.index.year == base_year).any():
        raise ValueError(f"Base year {base_year} not found in CPI data.")

    # YOUR CODE HERE — the body of your deflate_series_fixed from Part 1
    base = cpi.loc[cpi.index.year == base_year]
    if len(base) == 0:
      raise ValueError(f"base_year {base_year} not present in the CPI Index")

    date = nominal.index.intersection(cpi.index)
    nominal = nominal.loc[date]
    cpi = cpi.loc[date]

    real = (nominal / cpi) * base.mean()

    return real.dropna()

# YOUR CODE HERE — paste profile_dataframe() from Lab 1 Part 3

def profile_dataframe(data, unit_col="name", time_col="date"):
    """Return a dict describing the structure and completeness of `data`."""
    profile = {}
    profile["shape"] = data.shape

    # 1. How many units, and how many periods?                    [Step 0c]
    profile["n_units"]   = data[unit_col].nunique()
    profile["n_periods"] = data[time_col].nunique()

    # The taxonomy follows from those two counts. Read this; it is the
    # whole point of the chapter.
    if profile["n_units"] > 1 and profile["n_periods"] > 1:
        profile["structure"] = "panel"
    elif profile["n_periods"] > 1:
        profile["structure"] = "time series"
    else:
        profile["structure"] = "cross-sectional"

    # 2. Count the periods each unit actually appears in.         [Step 0c]
    periods_per_unit = data.groupby(unit_col)[time_col].nunique()

    # 3. Keep only the units that appear in every period, and say whether
    #    that is all of them.                                     [Step 0c]
    complete = periods_per_unit[periods_per_unit == profile["n_periods"]]
    profile["complete_units"] = len(complete)
    profile["balanced"] = len(complete) == profile["n_units"]

    # 4. The share of each column that is missing, as a percentage.
    #    One entry per column, built with the loop.               [Step 0d]
    missing = {}
    for col in data.columns:
        missing[col] = data[col].isna().mean() * 100
    profile["missing"] = missing

    return profile