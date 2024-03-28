########################################################
#Cloudperceptor                                  #
########################################################

Make sure to have the correct services enabled in your GCP project which include below

api-gateway
cloudfunctions
storage

To deploy this serverless function API, use below command

gcloud functions deploy car-bot-fallback-api     --gen2     --runtime=python312     --region=us-central1     --source=.     --entry-point=handle_post_request     --trigger-http     --allow-unauthenticated