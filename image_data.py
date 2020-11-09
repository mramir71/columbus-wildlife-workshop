import urllib.request

class Save():
    def __init__(self):
        return
    def url_to_jpg(self, i, url, file_path):
        '''
            Args:
                -- i: number of image
                -- url: a URL address of a given image
                -- file_path: where to save the final image
        '''

        filename = 'image-{}.jpg'.format(i)
        full_path = '{}{}'.format(file_path, filename)
        urllib.request.urlretrieve(url, full_path)

        print('{} saved.'.format(filename))
        return 
    
    #method to get url links from json list
    def get_urls(self, json_data):
        urls = []
        for doc in json_data:
            for item in doc:
                if item['url_l'] != "":
                    urls.append(item['url_l'])
        return urls
    
    def download_images(self, file_path, json_data):
        #get all urls from json docs
        urls = self.get_urls(json_data)
        
        # Save Images to the Directory by iterating through urls
        i=0
        for url in urls:
            i += 1
            self.url_to_jpg(i, url, file_path)
            
        print('done downloading images!')
        
        return urls
    
    def download_metadata(self, json_data):
        out_file = open("image_metadata.json", "w")  
        for dict_item in json_data:
            json.dump(dict_item, out_file, indent = 6)  
        out_file.close()  
        