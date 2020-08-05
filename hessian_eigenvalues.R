library(dplyr)
library(ggplot2)
library(paramtest)

calcEigenvalues <- function(i, x, y) {  # x is v1, y is v2
  H <- matrix(c((1200 * (x ^ 2)) - (400 * y) + 2, -400 * x, -400 * x, 200), 2, 2)  # Hessian
  e <- eigen(H)  # calculate eigenvectors and eigenvalues
  eigenvalues <- e$values
}

res <- grid_search(calcEigenvalues, params = list(x = seq(-10, 10, 0.5), y = seq(-10, 10, 0.5)), output = "data.frame")
df = res$results  # get eigenvalues at points

# Reject convexity at the following points as at least one eigenvalue is negative:
filter(df, X1 < 0 | X2 < 0) %>% ggplot(aes(x.test, y.test)) + geom_point() + labs(x = 'X Axis', y = 'Y Axis', title = 'Reject convexity at the following points as at least one eigenvalue is negative')
