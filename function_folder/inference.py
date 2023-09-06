# Avoid zero divisions errors
from __future__ import division

'''---------------------------------------------------'''

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import sem
import math

'''--------------------------------------------------- POPULATION''' 

### Population functions ###

def pop_parameters(dataset):
    statistics = {}

    for i in dataset.columns:
        size = np.size(dataset[i])
        datatype = dataset[i].dtypes
        unique_values = dataset[i].unique().size
        mean = np.mean(dataset[i])
        stdv = np.std(dataset[i])
        min = dataset[i].min()
        per25 = dataset[i].quantile(0.25)
        median = dataset[i].quantile(0.50)
        per75 = dataset[i].quantile(0.75)
        max = dataset[i].max()
        IQRs = dataset[i].quantile(0.75) - dataset[i].quantile(0.25)
        lower_bound = (dataset[i].quantile(0.25)) - 1.5*(dataset[i].quantile(0.75) - dataset[i].quantile(0.25))
        upper_bound = (dataset[i].quantile(0.75)) + 1.5*(dataset[i].quantile(0.75) - dataset[i].quantile(0.25))

        statistics[i] = (size,datatype,unique_values,mean,stdv,min,per25,median,per75,max,IQRs,lower_bound,upper_bound)
    results = pd.DataFrame.from_dict(statistics,orient='index',columns=['size','datatype','unique_values','mean','stdv','min','per25',
                                                                        'median','per75','max','IQRs','lower_bound','upper_bound'])
    results['lower_bound'] = np.where((results['lower_bound']<0) & (results['min']>=0),0,results['lower_bound'])
    return round(results,2)


'''Saving results to a dictionary'''

def pop_parameters_dict(dataset):
    statistics = {}

    for i in dataset.columns:
        size = np.size(dataset[i])
        datatype = dataset[i].dtypes
        unique_values = dataset[i].unique().size
        mean = np.mean(dataset[i])
        stdv = np.std(dataset[i])
        min = dataset[i].min()
        per25 = dataset[i].quantile(0.25)
        median = dataset[i].quantile(0.50)
        per75 = dataset[i].quantile(0.75)
        max = dataset[i].max()
        IQRs = dataset[i].quantile(0.75) - dataset[i].quantile(0.25)
        lower_bound = (dataset[i].quantile(0.25)) - 1.5*(dataset[i].quantile(0.75) - dataset[i].quantile(0.25))
        upper_bound = (dataset[i].quantile(0.75)) + 1.5*(dataset[i].quantile(0.75) - dataset[i].quantile(0.25))

        statistics[i] = (size,datatype,unique_values,mean,stdv,min,per25,median,per75,max,IQRs,lower_bound,upper_bound)
    results = pd.DataFrame.from_dict(statistics,orient='index',columns=['size','datatype','unique_values','mean','stdv','min','per25',
                                                                        'median','per75','max','IQRs','lower_bound','upper_bound'])
    results['lower_bound'] = np.where((results['lower_bound']<0) & (results['min']>=0),0,results['lower_bound'])
    results =  round(results,2)
    results = results.to_dict('index')
    return results


'''--------------------------------------------------- DISTRIBUTION ANALYSIS (MOMENTS)'''

# Calculate 4 moments of a distribution
def moment_summary(dataset):
    statistics = {}

    for i in dataset.columns:
        mean= np.mean(dataset[i])
        median = dataset[i].quantile(0.50)
        stdv = np.std(dataset[i])
        skewness = 3*(mean - median) / stdv
        mu4 = np.mean((dataset[i] - mean)**4)
        mu2 = np.mean((dataset[i] - mean)**2)
        kurtosis = mu4/(mu2**2)
        Excess_kurtosis = kurtosis - 3

        statistics[i] = (mean,median,stdv,skewness,kurtosis,Excess_kurtosis)
    results = pd.DataFrame.from_dict(statistics,orient='index',columns=['mean','median','stdv','skewness','kurtosis','Excess_kurtosis'])
    results = round(results,2)
    #Measuring Skewness
    results['is_skewed'] = results['skewness']
    results['is_skewed'] = np.where((results['skewness']> -0.5) & (results['skewness']<= 0.5), "almost symmetric", results['is_skewed'])
    results['is_skewed'] = np.where((results['skewness']<= -0.5) & (results['skewness']>= -1), "moderate negative skewness", results['is_skewed'])
    results['is_skewed'] = np.where((results['skewness']> 0.5) & (results['skewness']<= 1), "moderate positive skewness", results['is_skewed'])
    results['is_skewed'] = np.where((results['skewness']< -1) , "high negative skewness", results['is_skewed'])
    results['is_skewed'] = np.where((results['skewness']> 1) , "high positive skewness", results['is_skewed'])

    #Measuring Kurtosis
    results['is_kurtosis'] = results['kurtosis']
    results['is_kurtosis'] = np.where((results['kurtosis']== 3) & (results['Excess_kurtosis']== 0), "mesokurtic", results['is_kurtosis'])
    results['is_kurtosis'] = np.where((results['kurtosis']< 3) & (results['Excess_kurtosis']< 0), "platykurtic", results['is_kurtosis'])
    results['is_kurtosis'] = np.where((results['kurtosis']> 0.5) & (results['Excess_kurtosis']> 0), "leptokurtic", results['is_kurtosis'])

    #Kurtosis description
    results['description'] = results['is_kurtosis']
    results['description'] = np.where((results['is_kurtosis']== "mesokurtic") , "extreme events are close to zero", results['description'])
    results['description'] = np.where((results['is_kurtosis']=="platykurtic") , "few values in the tails, flatter peak", results['description'])
    results['description'] = np.where((results['is_kurtosis']=="leptokurtic") , "higher chances of extreme outliers", results['description'])

    return results

'''--------------------------------------------------- COUNTING OUTLIERS'''

def outlier_summary(dataset,dictionary,lower,upper):
    outli = {}
    for i in dataset.columns:
        n = np.size(dataset[i])
        lower_b = round(dictionary[i][lower],3)
        outliers_lower_n = dataset[i][dataset[i] < dictionary[i][lower]].count()
        outliers_lower_perc = (dataset[i][dataset[i] < dictionary[i][lower]].count()) / np.size(dataset[i])
        upper_b = round(dictionary[i][upper],3)
        outliers_upper_n = dataset[i][dataset[i] > dictionary[i][upper]].count()
        outliers_upper_perc = (dataset[i][dataset[i] > dictionary[i][upper]].count()) / np.size(dataset[i])
        total_outliers = outliers_lower_n + outliers_upper_n
        total_outliers_perc = outliers_lower_perc + outliers_upper_perc

        outli[i] = (n,lower_b,outliers_lower_n,outliers_lower_perc,upper_b,outliers_upper_n,outliers_upper_perc,total_outliers,total_outliers_perc)
    results = pd.DataFrame.from_dict(outli,orient='index',columns=['n','lower_b','outliers_lower_n','outliers_lower_perc','upper_b','outliers_upper_n',
                                                                   'outliers_upper_perc','total_outliers','total_outliers_perc'])
    return round(results,2)


'''--------------------------------------------------- COUNTING MISSING VALUES'''

def missing_summary(dataset):
    missing = {}
    for i in dataset.columns:
        n = np.size(dataset[i])
        missing_values = dataset[i].isnull().sum()
        missing_perc = dataset[i].isnull().mean()
        missing[i] = (n,missing_values,missing_perc)
    results = pd.DataFrame.from_dict(missing,orient='index',columns=['n','missing_values','missing_perc'])
    results = results.sort_values(by='missing_perc',ascending=False)
    results = results[results['missing_values']>0]

    return round(results,4)


'''--------------------------------------------------- SAMPLING'''

# Generating a simple random sample:
def data_sample(df,size,repl):
    samples = df.sample(size,replace = repl)
    return pd.DataFrame(samples)


def sample_parameters(dataset):
    statistics = {}
# Include standard error calculation
    for i in dataset.columns:
        size = np.size(dataset[i])
        datatype = dataset[i].dtypes
        unique_values = dataset[i].unique().size
        mean = np.mean(dataset[i])
        stdv = np.std(dataset[i])
        se = np.std(dataset[i],ddof=1)/np.sqrt(np.size(dataset[i]))
        min = dataset[i].min()
        per25 = dataset[i].quantile(0.25)
        median = dataset[i].quantile(0.50)
        per75 = dataset[i].quantile(0.75)
        max = dataset[i].max()
        IQRs = dataset[i].quantile(0.75) - dataset[i].quantile(0.25)
        lower_bound = (dataset[i].quantile(0.25)) - 1.5*(dataset[i].quantile(0.75) - dataset[i].quantile(0.25))
        upper_bound = (dataset[i].quantile(0.75)) + 1.5*(dataset[i].quantile(0.75) - dataset[i].quantile(0.25))

        statistics[i] = (size,datatype,unique_values,mean,stdv,se,min,per25,median,per75,max,IQRs,lower_bound,upper_bound)
    results = pd.DataFrame.from_dict(statistics,orient='index',columns=['size','datatype','unique_values','mean','stdv','se','min','per25',
                                                                        'median','per75','max','IQRs','lower_bound','upper_bound'])
    results['lower_bound'] = np.where((results['lower_bound']<0) & (results['min']>=0),0,results['lower_bound'])
    return round(results,2)


# Saving sample results in a dictionary

def sample_parameters_dict(dataset):
    statistics = {}
# Include standard error calculation
    for i in dataset.columns:
        size = np.size(dataset[i])
        datatype = dataset[i].dtypes
        unique_values = dataset[i].unique().size
        mean = np.mean(dataset[i])
        stdv = np.std(dataset[i])
        se = np.std(dataset[i],ddof=1)/np.sqrt(np.size(dataset[i]))
        min = dataset[i].min()
        per25 = dataset[i].quantile(0.25)
        median = dataset[i].quantile(0.50)
        per75 = dataset[i].quantile(0.75)
        max = dataset[i].max()
        IQRs = dataset[i].quantile(0.75) - dataset[i].quantile(0.25)
        lower_bound = (dataset[i].quantile(0.25)) - 1.5*(dataset[i].quantile(0.75) - dataset[i].quantile(0.25))
        upper_bound = (dataset[i].quantile(0.75)) + 1.5*(dataset[i].quantile(0.75) - dataset[i].quantile(0.25))

        statistics[i] = (size,datatype,unique_values,mean,stdv,se,min,per25,median,per75,max,IQRs,lower_bound,upper_bound)
    results = pd.DataFrame.from_dict(statistics,orient='index',columns=['size','datatype','unique_values','mean','stdv','se','min','per25',
                                                                        'median','per75','max','IQRs','lower_bound','upper_bound'])
    results['lower_bound'] = np.where((results['lower_bound']<0) & (results['min']>=0),0,results['lower_bound'])
    results = round(results,4)
    results = results.to_dict('index')
    return results

'''--------------------------------------------------- SAMPLING DISTRIBUTION (INFERENCE 1)'''

def sampling_dist(dataset,size,repl,ranges):
    statistics = {}
    for i in dataset.columns:
        mean_list = []
        for n in range(ranges):
            means = dataset[i].sample(size,replace = repl).mean()
            mean_list.append(means)
        statistics[i] = mean_list
    return statistics


def sample_dist_parameters(dataset,t_value):
    statistics = {}
# Include standard error calculation
    for i in dataset.columns:
        mean = np.mean(dataset[i])
        se = np.std(dataset[i],ddof=1)
        size = np.size(dataset[i])
        median = dataset[i].quantile(0.50)
        upper_ci = mean + t_value * se
        lower_ci = mean - t_value * se
        
        statistics[i] = (mean,se,size,median,lower_ci,upper_ci)
    results = pd.DataFrame.from_dict(statistics,orient='index',columns=['mean','se','size','median','lower_ci','upper_ci'])
    return round(results,2)


def sample_dist_dict(dataset,t_value):
    statistics = {}
# Include standard error calculation
    for i in dataset.columns:
        mean = np.mean(dataset[i])
        se = np.std(dataset[i],ddof=1)
        size = np.size(dataset[i])
        median = dataset[i].quantile(0.50)
        upper_ci = mean + t_value * se
        lower_ci = mean - t_value * se
        
        statistics[i] = (mean,se,size,median,lower_ci,upper_ci)
    results = pd.DataFrame.from_dict(statistics,orient='index',columns=['mean','se','size','median','lower_ci','upper_ci'])
    results =  round(results,2)
    results = results.to_dict('index')
    return results


'''--------------------------------------------------- BOOTSTRAPPING (INFERENCE 2)'''

def bootstrap_samp(dataset,size,replicas):
    statistics= {}
    for i in dataset.columns:
        boot_means = []
        for n in range(replicas):
            bootsample= dataset[i].sample(size,replace=True)
            bootsample_mean = bootsample.mean()
            boot_means.append(bootsample_mean)
        statistics[i] = boot_means
    return statistics


'''--------------------------------------------------- PLOTTING'''

# 1) Histoplots (MULTIPLE COLUMNS)

def plot_hist_mult(data,var1,var2,bins):
    fig, axes = plt.subplots(var1,var2)

    for i, el in enumerate(list(data.columns.values)):
        a= data.hist(el,ax=axes.flatten()[i], bins=bins)

    fig.set_size_inches(18.5,14)
    plt.tight_layout()
    plt.show()


# 2) BOXPLOTS (MULTIPLE COLUMNS)

def plot_box_mult(data,var1,var2):
    fig, axes = plt.subplots(var1,var2)

    for i, el in enumerate(list(data.columns.values)):
        a= data.boxplot(el,ax=axes.flatten()[i], fontsize= 'large')

    fig.set_size_inches(18.5,14)
    plt.tight_layout()
    plt.show()


# 3) SAMPLE DISTRIBUTION HISTOGRAM (MULTIPLE COLUMNS)

def plot_sampledist_mult(data,var1,var2,bins,directory,lower_ci,upper_ci):
    fig, axes = plt.subplots(nrows=var1,ncols=var2,figsize=(18.5,14))
    axes = axes.ravel()
    cols = data.columns

    for col, ax in zip(cols,axes):
        data[col].plot(kind='hist', ax=ax, label=col, title=col, bins=bins)
        ax.axvline(x=directory[col][lower_ci],color = 'black', ls='--', label = 'Lower CI')
        ax.axvline(x=directory[col][upper_ci],color = 'black', ls='--', label = 'Upper CI')

    fig.tight_layout()
    plt.show()