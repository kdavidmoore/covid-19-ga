df <- read.csv("~/Projects/covid-19-ga/covid-19-nc-data-python.csv")

library(ggplot2)
library(lubridate)

df$date <- as.Date(as.character(df$date), format="%Y%m%d")

df <- df[df$date >= "2020-05-01" & df$date <= "2020-12-01",]

p <- ggplot(df, aes(x=df$date, y=df$positiveIncrease)) +
  geom_bar(stat="identity", fill="steelblue") +
  geom_text(aes(label=df$positiveIncrease), vjust=1.6, color="white", size=2.5) +
  labs(title="Daily New COVID-19 Cases in NC", x="Date", y="Daily New Cases") +
  theme_minimal()

p