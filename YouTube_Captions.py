# coding:utf-8

print('Loading necessary modules...\n')
import re
import pandas as pd
import numpy as np
from pytube import YouTube as YT

url = input('Please enter the YouTube video link:\n\t $ ')
while not url == '':
    print('\nGetting video informations...\n')
    yt = YT(url)

    title = yt.title.replace('/', '-')
    title = yt.title.replace('\\', '-')
    title = yt.title.replace('|', '-')


    print("Getting english captions for '{}'...\n".format(title))
    captions = yt.captions.get_by_language_code('en')

    if captions is not None:

        print('Converting captions to SRT...\n')
        captions_srt = (captions.generate_srt_captions())

        with open(r'{}.txt'.format(title), 'w') as file:
            file.write(re.sub(r'<.+?>', '',captions_srt))

        word_list = list()
        with open(r'{}.txt'.format(title), 'r') as file:
            for line in file:
                if not line.isspace():
                    word_list.append(line) 

        search_list=input('Enter the words you want to look for separated by an underscore "_" (no spaces between words):\n\n\t $ ').split('_')

        columns = ['Index', 'Time Stamp', 'Sentence']

        df = pd.DataFrame(np.array(word_list).reshape(int(len(word_list)/3),3), columns=columns)
        df.drop(columns=['Index'], inplace=True)

        for column in columns[1:]:
            df[column] = df[column].str[:-2]
            
        matches = list()
        for inedx, row in df.iterrows():
            if re.compile('|'.join(search_list), re.IGNORECASE).search(row[1]):
                print('Match found on {}: "{}""'.format(row[0], row[1]))
                matches.append(1)   
        if len(matches) == 0:
            print('\nNo matches were found for {}'.format(search_list))
        
        input('\nClick enter to move to search a new video')

    else:
        print('Captions are not available for this video!')
        input('\nClick enter to move to search a new video')

    url = input('\nPlease enter the YouTube video link (Press \'Enter\' to quit):\n\t $ ')
