import math
import numpy as np

scores = [70, 75, 80, 85, 90]
hours = [1, 2, 3, 4, 5]
exam_scores = [50, 60, 70, 80, 90]

def calculate_mean(data):
    if not data:
        print("Mean: 0")
        return 0
    
    avg = sum(data)/len(data)
    print("Mean: ", avg)
    return avg

def calculate_variance(data, mean_value):
    if not data:
        print("Variance: 0")
        return 0
    
    data_squared = [(x - mean_value)**2 for x in data]
    result_variance = sum(data_squared)/len(data)
    print("Variance: ", result_variance)
    return result_variance

def calculate_std_deviation(var_value):
    result_std_deviation = math.sqrt(var_value)
    print("Standard Deviation: ", result_std_deviation)
    return result_std_deviation

result_mean_scores = calculate_mean(scores)
result_variance_scores = calculate_variance(scores, result_mean_scores)
result_std_deviation_scores = calculate_std_deviation(result_variance_scores)

result_mean_hours = calculate_mean(hours)
result_variance_hours = calculate_variance(hours, result_mean_hours)
result_std_deviation_hours = calculate_std_deviation(result_variance_hours)

def calculate_pearson_correlation(scores, hours):
    mean_scores = calculate_mean(scores)
    mean_hours = calculate_mean(hours)
    covariance_terms = [(s - mean_scores)*(h - mean_hours) for s,h in zip(scores, hours)]
    x_squared = [(s - mean_scores)**2 for s in scores]
    y_squared = [(h - mean_hours)**2 for h in hours]
    sum_x_squared = sum(x_squared)/len(covariance_terms)
    sum_y_squared = sum(y_squared)/len(covariance_terms)
    sum_xy = sum(covariance_terms)/len(covariance_terms)
    correlation = sum_xy/((math.sqrt(sum_x_squared))*(math.sqrt(sum_y_squared)))
    return correlation


a = calculate_pearson_correlation(scores, hours)
print("Correlation: ",a)

np_correlation = np.corrcoef(scores, hours)
print(np_correlation)
print(math.isclose(a, np_correlation[0][1]))
