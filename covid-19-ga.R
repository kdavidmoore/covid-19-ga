df <- read.csv("~/Projects/covid-19-ga/covid-19-ga-data.csv")

library(ggplot2)
library(lubridate)

df$date <- as.Date(as.character(df$date), format="%Y%m%d")

p <- ggplot(df, aes(x=df$date, y=df$newCases)) +
  geom_bar(stat="identity", fill="steelblue") +
  geom_text(aes(label=df$newCases), vjust=1.6, color="white", size=3.5) +
  labs(title="Daily New COVID-19 Cases in Georgia", x="Date", y="Daily New Cases") +
  theme_minimal()

p