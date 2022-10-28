# snowflake-udf-performance-testing

Performance testing for Snowflake UDFs includes:

- normal UDFs vs vecotrized
- Batch size for vectorized udfs
- Warehouse size
- Affects of dataset size
- compairison to local execution

See `snowpark_testing.ipynb` for all of the code execution  

UDFs saved as `.py` files to make them easier to review

The `env_setup.txt` file has some commands to help set up the conda environment to run snowpark.

`.csv` files save some query results

See results in blog here: https://www.prestonblackburn.com/projects/UDFPerformance
