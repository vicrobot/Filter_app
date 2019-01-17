library(mvtnorm)

<<<<<<< HEAD
rowvars <- colvars <- c(10,20,30,40,50)

all <- NULL
for(i in 1:length(colvars)){
  colvar <- colvars[i]
  for(j in 1:length(rowvars)){
    set.seed(303)  # Put seed here to show same data in each panel
    rowvar <- rowvars[j]
    # Simulate 50 points, corr=0.8
    sig <- matrix(c(rowvar, .8*sqrt(rowvar)*sqrt(colvar), .8*sqrt(rowvar)*sqrt(colvar), colvar), nrow=2)
    yy <- rmvnorm(50, mean=c(0,0), sig)
    dati <- data.frame(i=i, j=j, colvar=colvar, rowvar=rowvar, covar=.8*sqrt(rowvar)*sqrt(colvar), yy)
    all <- rbind(all, dati)
  }
}
names(all) <- c('i','j','colvar','rowvar','covar','x','y')
all <- transform(all, colvar=factor(colvar), rowvar=factor(rowvar))
library(latticeExtra)
useOuterStrips(xyplot(y~x|colvar*rowvar, all, cov=all$covar,
                      panel=function(x,y,subscripts, cov,...){
                        panel.xyplot(x,y,...)
                        print(cor(x,y))
                        ltext(14,-12, round(cov[subscripts][1],0))
                      }))
=======
    Use for cleaning the directory mess and make separate folders for pictures and videos.
![text](https://img.shields.io/badge/Experiment-blue.svg)
>>>>>>> d4f1b5586f1c508dfa21ca34a12d26a4ee6a1721
