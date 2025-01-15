# Setting Up Environment for BigQuery Script

This guide will help you set up your environment to run a Python script that interacts with Google BigQuery, specifically for accessing the `chrome-ux-report` dataset.

## 1. Set Up Google Cloud Account

### Create a Google Cloud Account
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Sign in with your Google account.

### Create a Project
1. Navigate to **IAM & Admin > Manage Resources**.
2. Click **Create Project** and give it a name (e.g., `measurements`).

---

## 2. Enable Required APIs

1. Open the [API Library](https://console.cloud.google.com/apis/library).
2. Search for and enable the following APIs:
   - **BigQuery API**

---

## 3. Install Required Tools

### Install Python
Ensure that Python 3.x is installed on your system.

### Install Google Cloud CLI
Download and install the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install).

### Install Required Python Libraries
Open a terminal and install the `google-cloud-bigquery` library:
pip install google-cloud-bigquery

---

## 4. Authenticate and Set Up gcloud

### Authenticate
Open a terminal and authenticate with your Google account:
gcloud auth application-default login
This will open a browser for you to log in.
After logging in, the credentials will be saved locally.

### Set the Active Project
Set your active Google Cloud project:
gcloud config set project <YOUR_PROJECT_ID>
Replace <YOUR_PROJECT_ID> with your actual project ID (e.g., measurements-220513).
For more details on authentication, refer to the [Google Cloud Authentication Setup Guide](https://cloud.google.com/docs/authentication/set-up-adc-local-dev-environment).

---

## 5. Test Access to BigQuery
Ensure you can see the chrome-ux-report dataset: [chrome-ux-report Dataset](https://console.cloud.google.com/bigquery?p=chrome-ux-report&d=all&page=dataset).

---

## 6. Run the Script
Save and run the Python script python list_country_datasets.py

