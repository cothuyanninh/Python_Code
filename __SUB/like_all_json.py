import httplib2
import os, time
import sys, random

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
	
CLIENT_SECRETS_FILE = "client_secrets.json"

MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0
To make this sample run you will need to populate the client_secrets.json file
found at: %s with information from the {{ Cloud Console }}
{{ https://cloud.google.com/console }} 
For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),CLIENT_SECRETS_FILE))
	
YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_authenticated_service(index, args):
	flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,scope=YOUTUBE_READ_WRITE_SCOPE,message=MISSING_CLIENT_SECRETS_MESSAGE)
	storage = Storage("%s.json" %index)
	credentials = storage.get()

	if credentials is None or credentials.invalid:
		credentials = run_flow(flow, storage, args)
	return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,http=credentials.authorize(httplib2.Http()))

def like_video(youtube, video_id):
	youtube.videos().rate(id=video_id, rating="like").execute()

if __name__ == "__main__":
	argparser.add_argument("--videoid", default="2LB-meHhMlA",help="ID of video to like.")
	args = argparser.parse_args()

	for i in range(1,13):
		youtube = get_authenticated_service(i, args)
		try:
			like_video(youtube, args.videoid)
		except (HttpError, e):
			print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
		else:
			print ("%s has been liked." % args.videoid)
		time.sleep(random.randint(10, 20))
		print("Liked video by json %d"%i)
