# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC ## This Notebook is used to read data from ADLS using access key

# COMMAND ----------

lst = [1,2,3,4,5,6]
even = []
for i in lst:
    if i%2 == 0:
        even.append(i)
print(even)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from Customer_df where city ='Pune';
