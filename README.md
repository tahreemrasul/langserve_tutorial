# How to deploy LangChain apps using LangServe

You can read in detail in this [medium article]()

## Clone Repository

```shell
   git clone git@github.com:tahreemrasul/langserve_tutorial.git
   cd ./langserve_tutorial
```

## Installation & Setup

Install the LangChain CLI using

```shell
pip install -U langchain-cli
```

Set Up a Conda Environment (Recommended)
* If you don't have Conda, install it first.
* Create a new Conda environment:
```shell
   conda create -n summarization_bot python=3.8
```

* Activate the environment:
```shell
   conda activate summarization_bot
```

Install Dependencies
* Install the required packages using the `requirements.txt` file:
```shell
   pip install -r requirements.txt
```

Set Up Your OpenAI API Key
* Create a .env file in the root directory of the project.
* Add your OpenAI API key to the `.env` file:
```shell
   OPENAI_API_KEY='Your-OpenAI-API-Key-Here'
```

## Launch LangServe

Run the application locally by navigating into main directory and:
```shell
langchain serve
```

## Running in Docker

This project folder includes a Dockerfile that allows you to easily build and host your LangServe app.

### Building the Image

To build the image, you simply:

```shell
docker build . -t my-langserve-app
```

If you tag your image with something other than `my-langserve-app`,
note it for use in the next step.

### Running the Image Locally

To run the image, you'll need to include any environment variables
necessary for your application.

In the below example, we inject the `OPENAI_API_KEY` environment
variable with the value set in my local environment
(`$OPENAI_API_KEY`)

We also expose port 8080 with the `-p 8080:8080` option.

```shell
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -p 8080:8080 my-langserve-app
```

## Running in GCP Cloud Run
Cloud Run in GCP is a managed compute platform that lets you run containers directly on top of Google's 
scalable infrastructure. You can run on GCP using either the source code or through the Dockerfile. For running with 
source code, use:
```shell
gcloud run deploy SERVICE --source . --port 8080 --project PROJECT_ID --allow-unauthenticated --region REGION 
--set-env-vars=OPENAI_API_KEY=$(OPENAI_API_KEY)
```

