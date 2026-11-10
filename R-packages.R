# Ejecutar una vez: Rscript R-packages.R
paquetes <- c("tidyverse", "rsample", "ranger", "gbm", "pROC",
              "knitr", "scales", "patchwork", "reticulate", "rmarkdown")
faltantes <- setdiff(paquetes, rownames(installed.packages()))
if (length(faltantes)) install.packages(faltantes, repos = "https://cloud.r-project.org")
cat("Dependencias de R listas.\n")
