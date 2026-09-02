# Statistics From Scratch

Implementation of core statistical functions (mean, variance, standard
deviation, Pearson correlation) using only Python loops — no NumPy —
built to deeply understand the underlying math before relying on libraries.

## Functions
- calculate_mean(data)
- calculate_variance(data, mean_value)
- calculate_std_deviation(var_value)
- calculate_pearson_correlation(x, y)

## Verification
Results were cross-checked against NumPy's built-in functions
(np.mean, np.var, np.std, np.corrcoef) using math.isclose() to
account for floating-point precision differences.

## Example output
Mean: 80.0
Variance: 50.0
Standard Deviation: 7.071
Correlation: 0.9999999999999998 (≈ 1.0, verified against NumPy)
