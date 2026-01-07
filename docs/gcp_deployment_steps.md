# GCP deployment steps
`$GOOGLE_PROJECT` makes reference to the project ID in GCP, the one we're working with

1. Create the GCP project and configure billing 

2. Go to IAM & Admin  
    2.1 Go to Service Accounts and create service account  
    2.2 Go to IAM and grant access to the new service account  
    2.3 Go to Service Accounts, three dots, manage keys and add key (download JSON file)  

3. Go to github repository and add secrets  
    3.1 Go to settings -> Secrets and variables -> actions  
    3.2 Click "New repository secret" and paste the contents of the JSON, I called the secret `GOOGLE_APPLICATION_CREDENTIALS`  
    3.3 Click again "New respository secret" and paste the GCP project ID, I called the secret `GOOGLE_PROJECT`

4. Install Google Cloud CLI (skip step if already installed)  
    4.1 `curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz`  
    4.2 `tar -xf google-cloud-cli-linux-x86_64.tar.gz`  
    4.3 `./google-cloud-sdk/install.sh`  

5. Login and select project  
    5.1 `gcloud auth login`  
    5.2 `gcloud config set project <project_name>`  
    5.3 Can verify the config using `gcloud config list` or `gcloud config get-value project`  

6. Enable required GCP services (this will **fail** if the billing was not configured for the project)  
    6.1 `gcloud services enable \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  cloudbuild.googleapis.com`  

7. Create Artifact Registry repository (it's ok if repository already exists, it just confirms the repo that's gonna be used)  
    7.1 `gcloud artifacts repositories create api-repo \
  --repository-format=docker \
  --location=us-central1 \
  --description="Docker images for Cloud Run"`  
  7.2 Can validate existing repositories using `gcloud artifacts repositories list`

8. Authenticate Docker to Artifact Registry  
    8.1 `gcloud auth configure-docker us-central1-docker.pkg.dev`

9. Setup dockerfile for project (skip this step if docker file is already created and working)

10. Build the docker image  
    10.1 `docker build \
  -t us-central1-docker.pkg.dev/$GOOGLE_PROJECT/api-repo/api .`

11. Authenticate Docker with Artifact Registry (skip if already authenticated)  
    11.1 `gcloud auth configure-docker us-central1-docker.pkg.dev`  

12. Push the image to Artifact Registry  
    12.1 `docker push us-central1-docker.pkg.dev/$GOOGLE_PROJECT/api-repo/api`  
    12.2 Can verify if the image exists using `gcloud artifacts docker images list \
  us-central1-docker.pkg.dev/$GOOGLE_PROJECT/api-repo`

13. Deploy the image to Cloud Run
  13.1 `gcloud run deploy api \
  --image us-central1-docker.pkg.dev/$GOOGLE_PROJECT/api-repo/api \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated`  
  13.2 Can validate if the service works either entering in the URL in browser or making a curl

