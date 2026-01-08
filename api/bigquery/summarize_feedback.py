from google.cloud import bigquery
from vertexai.preview.generative_models import GenerativeModel
import vertexai

PROJECT_ID = "gcp-codebase-exercise"
DATASET = "gcp_bigquery_exercise"
SOURCE_TABLE = "imdb_ratings"
TARGET_TABLE = "imdb_ratings_summary"
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)
bq_client = bigquery.Client(project=PROJECT_ID)

model = GenerativeModel("gemini-2.5-flash")

query = f"""
SELECT *
FROM `{PROJECT_ID}.{DATASET}.{SOURCE_TABLE}`
LIMIT 10
"""

rows = bq_client.query(query).result()

summaries = []

for row in rows:
    prompt = f"Summarize the movie rating in one short sentence:\n{row.title} {row.averageRating} {row.numVotes}"

    response = model.generate_content(prompt)

    summaries.append(
        {
            "titleId": row.titleId,
            "title": row.title,
            "averageRating": row.averageRating,
            "numVotes": row.numVotes,
            "summary": response.text,
        }
    )

table_id = f"{PROJECT_ID}.{DATASET}.{TARGET_TABLE}"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("titleId", "STRING"),
        bigquery.SchemaField("title", "STRING"),
        bigquery.SchemaField("averageRating", "FLOAT"),
        bigquery.SchemaField("numVotes", "INTEGER"),
        bigquery.SchemaField("summary", "STRING"),
    ],
    write_disposition="WRITE_TRUNCATE",
)

bq_client.load_table_from_json(summaries, table_id, job_config=job_config).result()

print("✅ Summaries written to BigQuery (LIMIT 10, cost-controlled)")
