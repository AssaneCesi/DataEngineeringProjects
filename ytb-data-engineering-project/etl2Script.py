import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1736521543080 = glueContext.create_dynamic_frame.from_catalog(database="db_youtube_cleaned", table_name="cleaned_statistic_reference_data", transformation_ctx="AWSGlueDataCatalog_node1736521543080")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1736521548305 = glueContext.create_dynamic_frame.from_catalog(database="db_youtube_cleaned", table_name="raw_statistics", transformation_ctx="AWSGlueDataCatalog_node1736521548305")

# Script generated for node Join
Join_node1736521599382 = Join.apply(frame1=AWSGlueDataCatalog_node1736521548305, frame2=AWSGlueDataCatalog_node1736521543080, keys1=["category_id"], keys2=["id"], transformation_ctx="Join_node1736521599382")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=Join_node1736521599382, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1736521487902", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1736522430506 = glueContext.getSink(path="s3://de-on-youtube-analytics-eu-north-1-dev", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=["region", "category_id"], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1736522430506")
AmazonS3_node1736522430506.setCatalogInfo(catalogDatabase="db_ytb_analytics",catalogTableName="final_analytics")
AmazonS3_node1736522430506.setFormat("glueparquet", compression="snappy")
AmazonS3_node1736522430506.writeFrame(Join_node1736521599382)
job.commit()