df <- read.csv("~/Projects/covid-19-ga/covid-19-ga.csv")

library(ggplot2)
library(lubridate)

df$date <- as.Date(as.character(df$date), format="%Y%m%d")

df <- df[df$date >= "2020-08-01",]

p <- ggplot(df, aes(x=date, y=hospitalized)) +
  geom_bar(stat="identity", fill="steelblue") +
  geom_text(aes(label=hospitalized), vjust=1.6, color="white", size=2.5) +
  labs(title="COVID-19 Daily hospitalized in Georgia", x="Date", y="hospitalized") +
  # geom_hline(yintercept=2000, color = "red") +
  scale_y_continuous(trans = 'log10') +
  annotation_logticks(sides="l")
  theme_minimal()

p