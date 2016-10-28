# 吴恩达 《机器学习》
## 第一章 线性回归

path <- "E:/python学习/吴恩达机器学习/machine-learning-ex1/ex1/ex1data1.txt"
data <- read.csv(path, header = F, col.names = c("Population", "Profit"))

library(ggplot2)
ggplot(data,aes(Population,Profit))+geom_point(colour="red")

# 考虑使用梯度下降法来进行回归

# 一个维度下的回归

costfunc1 <- function(data, alpha=0.01, theta = c(0,0),iteration = 500) {
  
   # 学习率设置为0, 初始值设置为c(2,1)
  n <- nrow(data)
  X <- cbind(rep(1,n), data[,1]) # 设计矩阵
  theta <- as.matrix(theta)
  
  df <- data.frame(theta0=rep(0,iteration+1),
                   theta1 = rep(0, iteration + 1),
                   cost = rep(0,iteration + 1))
  
  #function(theta=c(2,1)){
  lapply(1:(iteration+1), FUN = function(i){
    yhat <- X %*% theta   #拟合值
    cost <- (yhat - data[,2])^2/(2*n)
    df[i,] <<- c(theta[1], theta[2], cost)
    theta <<- theta - t(X) %*% (yhat-data[,2]) * alpha / n
  
  })
  
  return(df)
}

test <- costfunc1(data,alpha = 0.01, theta = c(0,0), iteration = 1000)
tail(test)
plot(test$cost[-1],col="red",type="l")

contour(x=test$theta0,y=test$theta1,z=test$cost)
