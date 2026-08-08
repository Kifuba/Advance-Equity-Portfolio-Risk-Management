"""
missing_values.py

Utilities for detecting, analysing and validating missing values
in financial time series.

Phase 2 - Data Cleaning
Advance-Equity-Portfolio-Risk-Management
"""

import pandas as pd


def has_missing_values(prices: pd.DataFrame) -> bool:
    """
    Check whether the DataFrame contains missing values.

    Parameters
    ----------
    prices : pd.DataFrame
        Input DataFrame.

    Returns
    -------
    bool
        True if at least one missing value exists.
    """

    if not isinstance(prices, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if prices.empty:
        raise ValueError("Input DataFrame is empty.")

    return prices.isnull().values.any()


def get_missing_columns(prices: pd.DataFrame) -> list:
    """
    Return all columns containing missing values.
    """

    if not isinstance(prices, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if prices.empty:
        raise ValueError("Input DataFrame is empty.")

    return prices.columns[prices.isnull().any()].tolist()


def get_missing_count(prices: pd.DataFrame) -> pd.Series:
    """
    Count missing values for each column.
    """

    if not isinstance(prices, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if prices.empty:
        raise ValueError("Input DataFrame is empty.")

    return prices.isnull().sum()


def get_total_missing_values(prices: pd.DataFrame) -> int:
    """
    Count the total number of missing values.
    """

    if not isinstance(prices, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if prices.empty:
        raise ValueError("Input DataFrame is empty.")

    return int(prices.isnull().sum().sum())


def get_missing_dates(prices: pd.DataFrame) -> dict:
    """
    Return the dates where missing values occur
    for every affected column.
    """

    if not isinstance(prices, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if prices.empty:
        raise ValueError("Input DataFrame is empty.")

    missing_dates = {}

    for column in get_missing_columns(prices):

        dates = prices.index[prices[column].isnull()].tolist()

        missing_dates[column] = dates

    return missing_dates


def missing_percentage(prices: pd.DataFrame) -> pd.Series:
    """
    Calculate the percentage of missing values
    for each column.
    """

    if not isinstance(prices, pd.DataFrame):
        raise TypeError("Input must be a pandas.DataFrame.")

    if prices.empty:
        raise ValueError("Input DataFrame is empty.")

    return (prices.isnull().sum() / len(prices)) * 100


def find_missing_values(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Build a structured report describing all missing values.
    """

    if not isinstance(prices, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if prices.empty:
        raise ValueError("Input DataFrame is empty.")

    if not has_missing_values(prices):

        return pd.DataFrame(
            columns=[
                "Column",
                "Missing Count",
                "Missing Percentage",
                "Missing Dates",
            ]
        )

    counts = get_missing_count(prices)

    percentages = missing_percentage(prices)

    dates = get_missing_dates(prices)

    report = []

    for column in get_missing_columns(prices):

        report.append(
            {
                "Column": column,
                "Missing Count": counts[column],
                "Missing Percentage": percentages[column],
                "Missing Dates": dates[column],
            }
        )

    return pd.DataFrame(report)


def get_missing_summary(prices: pd.DataFrame) -> dict:
    """
    Return a global summary describing missing values.
    """

    if not isinstance(prices, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")

    if prices.empty:
        raise ValueError("Input DataFrame is empty.")

    total_rows = len(prices)

    total_columns = len(prices.columns)

    total_missing = get_total_missing_values(prices)

    total_cells = total_rows * total_columns

    summary = {
        "has_missing_values": has_missing_values(prices),
        "total_rows": total_rows,
        "total_columns": total_columns,
        "columns_with_missing": len(get_missing_columns(prices)),
        "total_missing_values": total_missing,
        "overall_missing_percentage": (
            total_missing / total_cells
        ) * 100,
    }

    return summary


def validate_missing_values(prices: pd.DataFrame) -> bool:
    """
    Validate that the DataFrame no longer contains
    missing values.
    """

    return not has_missing_values(prices)