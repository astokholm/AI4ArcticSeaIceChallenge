import requests
from time import sleep
from tqdm import tqdm
import logging
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#looks like the individual files are within this range (actually every 3, weirdly)
file_id_range= list(range(37832145, 37835670, 1))

#set to your filepath, including trailing '\\' (very important)
filepath = 'C:\\Users\\Ultimate Gaming Comp\\Documents\\Ice_Data_2\\'

#loops over inidividual file ids on their server
for file_id in tqdm(file_id_range):
    url = 'https://data.dtu.dk/ndownloader/files/{}'.format(file_id)
    r = requests.get(url, allow_redirects=True)

    #if its a usable file, save it to filepath
    if 'Content-Disposition' in r.headers:

        filename= r.headers['Content-Disposition'].split('=')[1]

        open(filepath + filename, 'wb').write(r.content)

        logging.info("Successfully accessed and saved {} to {}". format(filename, filepath))

    #sleep means you dont spam the server and potentially get banned
    sleep(1)


