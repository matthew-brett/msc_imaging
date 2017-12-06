# R script to repeat GLM intro analysis
psychopathy <- c(11.416,   4.514,  12.204,  14.835, 8.416,   6.563,  17.343,
                13.02, 15.19 ,  11.902,  22.721,  22.324)
clammy = c(0.389,  0.2  ,  0.241,  0.463, 4.585,  1.097,  1.642,  4.972,
           7.957,  5.585,  5.527,  6.964)

simple_regression = lm(psychopathy ~ clammy)
print(summary(simple_regression))

university <- factor(c(rep('Berkeley', 4),
                       rep('Stanford', 4),
                       rep('MIT', 4)))

one_way_anova = lm(psychopathy ~ university)
print(summary(one_way_anova))
