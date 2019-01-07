import csv
def saveIntoCsv(_index,_file_name, _title, _comment, _tag, _link, _linkm3u8, flag):
	with open('./data/names.csv', 'a',encoding='utf8', newline='') as csvfile:
		fieldnames = ['index','file_name', 'title', 'comment', 'tag', 'link_source', 'link_m3u8']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		if flag == 0:
			writer.writeheader()
		writer.writerow({'index': _index,'file_name': _file_name, 'title': _title, 'comment': _comment, 'tag': _tag, 'link_source': _link, 'link_m3u8': _linkm3u8})