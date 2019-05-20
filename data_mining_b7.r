merge <- read.delim("./merge_data.txt", sep ="\n", header = FALSE, dec =".")
quick <- read.delim("./quick_data.txt", sep ="\n", header = FALSE, dec =".")
diff = (merge-quick)
diff_df <- data.frame(diff)
data<-data.frame(merge,quick)
boxplot(data, names=c("Merge","Quick"))
boxplot(diff, names=c("Merge"))

hist(merge$V1, main= "time")
hist(quick$V1, main= "time")
hist(diff_df$V1, main= "time")

qqnorm(merge$V1)
qqline(merge$V1)


qqnorm(quick$V1)
qqline(quick$V1)


qqnorm(diff_df$V1)
qqline(diff_df$V1)


