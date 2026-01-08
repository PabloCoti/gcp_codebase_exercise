# BigQuery usage steps

I'll follow the steps based on the knowledge I have about Power BI since they're tools that have a similar process but work differently.

1. Create dataset  
    1.1. Go to the GCP console -> BigQuery  
    1.2. Go to the three dots in the project and select "Create dataset"  
    1.3. Set the dataset id  
    1.4. Set the location, in this case I used `us-central1`  

2. Create table  
    2.1. Select "Create table"  
    2.2. Source: upload (in mi case since I want to work with an existing dataset I [downloaded from kaggle](https://www.kaggle.com/datasets/umitka/imdb-ratings?resource=download))  
    2.3. Schema: Auto-detect (best option in majority of times)  

3. Query Data, in the case of BigQuery the queries are done with SQL syntax, this makes the usage easier in my opinion.

4. Save views and measures

5. The workflow of BigQuery kind of ends there since in comparison with Power BI the visuals are done with an external tool, also we can do more with this like train a personalized model with vertex (gemini) based on our data and also do visuals with looker studio.

--- 

# Steps to comunicate vertex with my BigQuery dataset

Followed architecture

```
BigQuery (text data)
   ↓
Python app (Cloud Shell / local)
   ↓
Vertex AI (Gemini)
   ↓
BigQuery (summaries table)
```

1. Enable APIs (skip this step if APIs are already enabled)  
    1.1. `gcloud services enable \
  bigquery.googleapis.com \
  aiplatform.googleapis.com`  

2. Install libraries to handle bigquery in our api  
    2.1. `pip install google-cloud-bigquery google-cloud-aiplatform`

3. Create the script to comunicate with the AI model

4. Run the script 

5. Check if the analysis table was created in the dataset

6. Query the results of the created table