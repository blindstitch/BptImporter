#!/usr/bin/env python3

import pandas
import re

def sanitize(string):
    string = string.lower()
    string = re.sub(r' ','_',string)
    string = re.sub(r'[^a-zA-Z_]','',string)
    return string


class BptImporter():
    playName = ''
    dirtyData = ''
    headers = []
    cleanedData = pandas.DataFrame()

    def __init__(self, name):
        self.playName = name

    def importData(self, path):
        self.dirtyData = open(path,'r').read()
        self.dirtyData = self.dirtyData.split('\n')
        self.dirtyData = self.dirtyData[4:] # Top four lines are junk
        self.dirtyData = [line.split('\t') for line in self.dirtyData]
        self.headers = self.dirtyData[1]
        self.dirtyData = [line for line in self.dirtyData if len(line[0]) > 0]
        self.dirtyData = [line for line in self.dirtyData if line != self.headers]
        self.dirtyData = [line for line in self.dirtyData if line[0] != 'None']

    def processData(self):
        sectionHeads = [idx for idx, x in enumerate(self.dirtyData) if len(x) == 1]
        for idx in range(len(sectionHeads)):
            if len(self.dirtyData[sectionHeads[idx] + 1]) == 1:
                pass
            else:
                groupTicketClass = sanitize(self.dirtyData[sectionHeads[idx]][0])
                groupStart = sectionHeads[idx] + 1
                if idx != (len(sectionHeads) - 1):
                    groupEnd = sectionHeads[idx+1] - 1
                else: # End of data
                    groupEnd = len(self.dirtyData) - 1

                df = pandas.DataFrame(self.dirtyData[groupStart:groupEnd], columns=self.headers)
                df['ticket_purchase_type'] = groupTicketClass
                self.cleanedData = pandas.concat((self.cleanedData,df), ignore_index=True)

    def getData(self):
        return self.cleanedData
