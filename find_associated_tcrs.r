library(DBI)
## another library?

## change these parameters based on your database
con <- dbConnect(RPostgres::Postgres(), dbname = "database name", host = "localhost", port = "5432", user = "username", password = "password")

t <- dbReadTable(con, "hip_uniq_counts")

dbDisconnect(con)

n_positive <- 289
n_negative <- 352

row_to_cont_table <- function(row) {
  pp <- row$positive
  pn <- row$total - pp
  ap <- n_positive - pp
  an <- n_negative - pn
  matrix(c(pp,pn,ap,an), nrow=2)
}

is <- NULL

for (i in 1:nrow(t)) {
  row <- t[i,]
  ct <- row_to_cont_table(row)
  p <- fisher.test(ct, alternative = "greater")$p.value ## one-tailed
  if (p < 1e-4) {
    print(row)
    print(ct)
    print(p)
    is <- c(is, i)
  }
}

write.csv(t[is,c("amino_acid", "j_family", "j_gene", "j_allele", "v_family", "v_gene", "v_allele")], quote = FALSE, row.names = FALSE, file = "cmv_associated_tcrs.csv")
