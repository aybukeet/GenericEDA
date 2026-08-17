"""
outlier.py

Outlier analysis module for GenericEDA.

Features
--------
- Detect outliers using IQR
- Detect outliers using Z-Score
- Generate summary report
"""

import pandas as pd
import numpy as np
from scipy.stats import zscore


# ==========================================================
# IQR METHOD
# ==========================================================

def _iqr_outliers(series, multiplier=1.5):
    """
    Detect outliers using the IQR method.

    Parameters
    ----------
    series : pandas.Series
        Input numeric series.

    multiplier : float
        IQR multiplier used to calculate the bounds.

    Returns
    -------
    tuple
        outlier_count,
        outlier_percentage,
        lower_bound,
        upper_bound
    """

    clean_series = pd.to_numeric(
        series,
        errors="coerce"
    ).replace(
        [np.inf, -np.inf],
        np.nan
    ).dropna()

    if clean_series.empty:
        return 0, 0.0, np.nan, np.nan

    q1 = clean_series.quantile(0.25)
    q3 = clean_series.quantile(0.75)

    iqr = q3 - q1

    lower = q1 - multiplier * iqr
    upper = q3 + multiplier * iqr

    mask = (
        (clean_series < lower)
        | (clean_series > upper)
    )

    count = mask.sum()

    percent = (
        count / len(clean_series)
    ) * 100

    return (
        int(count),
        round(percent, 2),
        lower,
        upper
    )


# ==========================================================
# Z-SCORE METHOD
# ==========================================================

def _zscore_outliers(series, threshold=3):
    """
    Detect outliers using Z-Score.

    Parameters
    ----------
    series : pandas.Series
        Input numeric series.

    threshold : float
        Z-Score threshold.

    Returns
    -------
    tuple
        outlier_count,
        outlier_percentage,
        threshold
    """

    clean_series = pd.to_numeric(
        series,
        errors="coerce"
    ).replace(
        [np.inf, -np.inf],
        np.nan
    ).dropna()

    if clean_series.empty:
        return 0, 0.0, threshold

    if clean_series.std(ddof=0) == 0:
        return 0, 0.0, threshold

    z_scores = np.abs(
        zscore(clean_series)
    )

    count = (
        z_scores > threshold
    ).sum()

    percent = (
        count / len(clean_series)
    ) * 100

    return (
        int(count),
        round(percent, 2),
        threshold
    )


# ==========================================================
# REPORT GENERATION
# ==========================================================

def _generate_report(
    df,
    method="iqr",
    threshold=3,
    iqr_multiplier=1.5
):
    """
    Generate an outlier analysis report.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.

    method : str
        "iqr" or "zscore".

    threshold : int or float
        Z-Score threshold.

    iqr_multiplier : int or float
        IQR multiplier.

    Returns
    -------
    pandas.DataFrame
        Outlier report.
    """

    numeric_df = df.select_dtypes(
        include=np.number
    )

    # ------------------------------------------------------
    # Remove ID columns
    # ------------------------------------------------------

    numeric_df = numeric_df[
        [
            column
            for column in numeric_df.columns
            if "id" not in str(column).lower()
        ]
    ]

    # ------------------------------------------------------
    # Keep only continuous numeric columns
    # ------------------------------------------------------

    numeric_df = numeric_df[
        [
            column
            for column in numeric_df.columns
            if numeric_df[column].nunique(
                dropna=True
            ) > 10
        ]
    ]

    report = []

    # ------------------------------------------------------
    # Analyze each numeric column
    # ------------------------------------------------------

    for column in numeric_df.columns:

        if method.lower() == "iqr":

            count, percent, lower, upper = _iqr_outliers(
                numeric_df[column],
                multiplier=iqr_multiplier
            )

            report.append({
                "Column": column,
                "Method": "IQR",
                "Outlier Count": count,
                "Outlier %": percent,
                "Lower Bound": round(lower, 3),
                "Upper Bound": round(upper, 3)
            })

        elif method.lower() == "zscore":

            count, percent, limit = _zscore_outliers(
                numeric_df[column],
                threshold
            )

            report.append({
                "Column": column,
                "Method": "Z-Score",
                "Outlier Count": count,
                "Outlier %": percent,
                "Threshold": limit
            })

    report = pd.DataFrame(report)

    if report.empty:
        return report

    report = report.sort_values(
        by="Outlier Count",
        ascending=False
    ).reset_index(drop=True)

    return report


# ==========================================================
# MAIN FUNCTION
# ==========================================================

def detect_outliers(
    df,
    method="iqr",
    threshold=3,
    iqr_multiplier=1.5
):
    """
    Detect outliers in a dataset.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataset.

    method : str
        "iqr" or "zscore".

    threshold : int or float
        Threshold for Z-Score.

    iqr_multiplier : int or float
        Multiplier for IQR method.

    Returns
    -------
    pandas.DataFrame
        Outlier report.
    """

    method = method.lower()

    if method not in ["iqr", "zscore"]:
        raise ValueError(
            "Method must be either 'iqr' or 'zscore'."
        )

    if iqr_multiplier <= 0:
        raise ValueError(
            "IQR multiplier must be greater than 0."
        )

    report = _generate_report(
        df,
        method=method,
        threshold=threshold,
        iqr_multiplier=iqr_multiplier
    )

    return report