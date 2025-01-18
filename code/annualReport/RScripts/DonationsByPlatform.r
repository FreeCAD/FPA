# donations per platform
# input is in common data csv

library(tidyverse)
library(ggplot2)
library(plyr)

dfDon <- read.csv("/home/alg/Documents/FreeCAD/FPA/gnucash/2024/2024AnnualReport/work/inputForR2023Dons.csv")
#dfDon <- read.csv("/home/alg/Documents/FreeCAD/FPA/gnucash/2024/2024AnnualReport/work/inputForR2024Dons.csv")

platformCounts <- count(dfDon, "platform")
platformSums <- aggregate(dfDon$value, by=list(Category=dfDon$platform), FUN=sum)
colnames(platformSums)[1] <- "Platform"

ggplot(platformSums, aes(x=Platform, y=x, fill = Platform)) + 
   geom_bar(stat = "identity") +
   labs(title="2023 Where did donations come from?",
       x ="Platform", y = "2023 Total (EUR)") +
   theme_minimal()
# labs(title="2024 Where do donations come from?",
#      x ="Platform", y = "2024 Total (EUR)") +
#   theme_minimal()
