# https://cloud.google.com/functions/docs/deploying/filesystem?hl=ja
gcloud functions deploy checkEmotion --entry-point checkEmotion --runtime python37 --trigger-http --region asia-northeast1