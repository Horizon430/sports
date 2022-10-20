data<-read.table(file="/Users/yunzehe/Desktop/MAST397/ass4.txt",header=TRUE)
data
future<-data.frame(Year=2023:2030)
Year<-data$year
Time<-data$time
model<-lm(Time~Year)
lm(Time~Year)


plot(Year,Time,main="Men's 100 metres world record progression since 1977",xlim=c(1960,2030))
points(Year, Time, col = "red")
abline(lm(Time~Year),col="blue")
par(new=TRUE)

plot(fitted(lm(Time~Year),col="black"),ann=FALSE,xaxt = "n",yaxt = 'n')
predict(data,point,interval="prediction",level=0.95)

predictvalue<-predict(data,point,interval="prediction",level=0.95)

predict(model,future,interval="prediction")



