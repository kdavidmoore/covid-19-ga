df <- read.csv("~/Projects/covid-19-ga/covid-19-ga.csv")

library(ggplot2)
library(lubridate)

df$date <- as.Date(as.character(df$date), format="%Y%m%d")

df <- df[df$date >= "2021-01-01",]

p <- ggplot(df, aes(x=date, y=positiveIncrease)) +
  geom_bar(stat="identity", fill="steelblue") +
  geom_text(aes(label=positiveIncrease), vjust=1.6, color="black", size=2.5) +
  labs(title="COVID-19 Daily New Cases in Georgia", x="Date", y="positiveIncrease") +
  geom_hline(yintercept=2000, color = "red") +
  theme_minimal()

p