'''
Test 2 vectors/ts if they come from the same distribution.

Tests employed:
- Kolmogorov-Smirnov test
- Anderson-Darling test

Example here tests:
- Continuous (normal vs. uniform)
- Discrete (Bernoulli vs. geometric)

'''

import numpy as np 
import matplotlib.pyplot as plt 
from scipy import stats


# Define sameple sizes:
n_train = 8000
n_test = 10000


# Create distributions (2 different distributions)
# We will want to reject null of "same distributions"
cont_train = stats.norm.rvs(size=n_train)
cont_test = stats.uniform.rvs(size=n_test)

p = 0.3		# discrete distributions reqire prob.
disc_train = stats.bernoulli.rvs(p, size=n_train)
disc_test = stats.geom.rvs(p, size=n_test)


# Plot for comparison
plt.hist(cont_train, bins=50)
plt.hist(cont_test, bins=50)
plt.show();

plt.hist(disc_train)
plt.hist(disc_test)
plt.show();


# Kolmogorov-Smirnov
# null: 2 independent samples are drawn from the same continuous distribution
# This test is SENSITIVE on two-sided/less/greater parameter!!!
ks_c = stats.ks_2samp(cont_train, cont_test, alternative="less")
print(ks_c, "\n")


# Anderson-Darling:
# null: k-samples are drawn from the same population without having to specify the distribution function of that population.
ad_c = stats.anderson_ksamp([cont_train, cont_test])
print(ad_c, "\n")

ad_d = stats.anderson_ksamp([disc_train, disc_test])
print(ad_d, "\n")



### USE ANDERSON-DARLING!!!


