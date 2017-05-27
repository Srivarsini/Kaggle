library(plyr)
library("NbClust")

dataBank <- read.csv('C:/Users/Sriva/Desktop/Kaggle/SberbankHousing/mergedData.csv')
for (col_name in names(dataBank))
{
  if (!is.numeric(dataBank[,col_name]))
  {
    dataBank[,col_name] <- as.numeric(dataBank[,col_name])
  }
}
features <- dataBank[,-391]

res.nb <- NbClust(features, distance = "euclidean",
                  min.nc = 2, max.nc = 10, 
                  method = "complete", index ="all") 
res.nb # print the results

