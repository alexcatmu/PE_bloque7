merge <- read.delim("./merge_data.txt", sep ="\n", header = FALSE, dec =".")
quick <- read.delim("./quick_data.txt", sep ="\n", header = FALSE, dec =".")

data<-data.frame(merge,quick)
boxplot(data, names=c("Merge","Quick"))