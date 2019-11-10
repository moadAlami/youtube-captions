# youtube-captions

Looks for a list of words in a YouTube Video

## Principle

This Python script takes a YouTube video url as input, it then checks if that video has english captions available; if it is the case, it then prompts the user to input a list of words and checks if they are in the video. When a match is found, the script will output the timestamp and the sentence containing that word.

Technically, youtube-captions can also look for sentences, but this can be difficul because most sentences in a video are split based on the timestamp.

## False positives

In some videos, if a word that's being searched matches with the person speaking, it can result in a false positive. For example, If we're looking for the word "Jimmy" --> "Jimmy: THIS IS ELLEN".

## Dependencies

youtube-captions uses [pytube](https://github.com/moadAlami/ROI-Auto/blob/master/README.md), [pandas](https://pandas.pydata.org/) and [numpy](https://www.numpy.org/).
