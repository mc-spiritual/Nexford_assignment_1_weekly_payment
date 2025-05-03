# Load necessary library
library(dplyr)

# Step 1: Generate a data frame of 400 workers
set.seed(123)  # For reproducibility

num_workers <- 400
worker_ids <- 1:num_workers
names <- paste0("Employee_", worker_ids)
genders <- sample(c("Male", "Female"), num_workers, replace = TRUE)
salaries <- sample(5000:35000, num_workers, replace = TRUE)

workers <- data.frame(
  Worker_ID = worker_ids,
  Name = names,
  Gender = genders,
  Salary = salaries,
  stringsAsFactors = FALSE
)

# Step 2: Assign Employee Levels based on conditions
workers <- workers %>%
  mutate(
    Level = case_when(
      Salary > 10000 & Salary < 20000 ~ "A1",
      Salary > 7500 & Salary < 30000 & Gender == "Female" ~ "A5-F",
      TRUE ~ "B2"
    )
  )

# Step 3: Export to CSV
output_file <- "highridge_payment_slips_r.csv"
write.csv(workers, output_file, row.names = FALSE)

# Confirmation message
cat("Payroll slips successfully saved to", output_file, "\n")
