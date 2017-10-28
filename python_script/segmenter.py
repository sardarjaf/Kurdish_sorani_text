import re
import glob
import os

# read files from a directory
# read retrieved files and read them
# traverse through the file line by line
# process each line and segment the sentences based on basic punctuation marks
# write the segments to a file
def readFiles(fileName):
    sentences = ''
    with open(fileName, 'r') as file:
        for line in file:
            if len(line) > 5: # if line has more than 5 characters
                sentences += line+'\n'
    return sentences

def segmentSentnces(sentence):
    segments = []
    for seg in re.split("[\.:؟]+", sentence):
        tokens = seg.split(' ')
        if len(tokens) >= 5 and len(tokens) <= 30:
            segments.append(seg)

    return segments

def writeSegmentToFile(segments, fileName):
    file = open(fileName, 'w')
    for segment in segments:
        print(segment)
        tokens = segment.split(' ')
        if len(tokens) >= 5 and len(tokens) <= 25:
            file.write(segment+'\n')

def traverseDir(readingDirName, writingDirName):
    count = 1
    allSent = []
    for file in glob.glob(os.path.join(readingDirName, '*.txt')):
        count += 1
        sentences = readFiles(file)
        lines = sentences.split('\n')
        for line in lines:
            if len(line.split(' ')) > 5:
                segments = segmentSentnces(line)
                for seg in segments:
                    allSent.append(seg)
        if count > 35: # reading up to 35 files
            break

    return allSent

def writeF(writingDirName):
    allSent = traverseDir(readingDirName, writingDirName)
    print(allSent, len(allSent))
    i = 0
    j = 15
    for count in range(1, 21):
        writeSegmentToFile(allSent[i:j], os.path.join(writingDirName, str(count) + '.txt'))
        temp = i
        i = j
        j = (j * 2) - temp



readingDirName = './data/kurdish-sentences/' #to be modifed to use dir path
writingDirName = './data/kurdish-sentences-segmented/' #to be modifed to use dir path
writeF(writingDirName)
