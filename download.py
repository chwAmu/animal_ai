from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os,time,sys

#API
key='xxxx'
secret='yyy'
wait_time=1

#save path
animalname=sys.argv[1]#
savedir='./'+animalname

flickr=FlickrAPI(key,secret,format='parsed-json')
result=flickr.photos.search(
		text=animalname,
		per_page=400,
		media='photos',
		sort='relevance',
		safe_search=1,
		extras='url_q,licence'
	)

photos=result['photos']

print('photos is donwloading..')
for i,photo in enumerate(photos['photo']):
	url_q=photo['url_q']
	file_path=savedir+'/'+photo['id']+'.jpg'
	if os.path.exists(file_path):continue
	urlretrieve(url_q,file_path)
	time.sleep(wait_time)
	
print('Finished:)!')