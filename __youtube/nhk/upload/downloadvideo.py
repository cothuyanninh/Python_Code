import os
def downloadVideo(link_m3u8, title):
	os.system("ffmpeg -protocol_whitelist file,http,https,tcp,tls,crypto -i %s -c copy %s.mp4"%(link_m3u8, title))

