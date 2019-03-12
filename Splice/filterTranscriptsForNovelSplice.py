# -*- coding: utf-8 -*-

####Splice filtering
####Nicole Lama
####RNA_Seq_In_Cloud
####2019/03/11

################# STEPS #######################################################
## input: gtf files

## filtering steps:
#i. remove known txs A
#ii. remove intronless tx
#iii. keep only internal exons (remove begining and terminal exons)
#iv. Filter retained introns

## output: tsv (chr,exon_start,exon_stop,strand)
import os,sys,csv
from glob import glob
import numpy as np
import pandas as pd



#define important variables and arrays/dictionaries

gtf = []
#rejectTx = [] ## store rejected transcripts with less than 2 introns
exonTxH = {}


#################### FUNCTIONS ###############################################
def examineInternalExons(data):
    return data

def writeOutFile(tsvOut):
    with open(tsvOut, "w+", newline = '') as tOut:
            tOut.write("chromosome\exon_start\exon_end\tstrand_+/-\n")
            for row in tsvOut:
                row=row.split()
                tOut.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(chrm,exS,exE,strd))
            tsvOut.close()


########################## INIT ###############################################

with open("sample.500.gtf",'r') as g:
    for row in g:
        tx = row.split("\t")
        if row.split(" ")[0] == "#": #filter out header and gaps
            continue
#        if tx[2] == "transcript":
#            exonCount = 0
            pass
        if any("reference_id" in attr for attr in tx[8].split(";")): #filter known tx
            continue
        if tx[2] == "exon":
            if not any("1" in exNum for exNum in tx[8].split(";")[2]): #filter for less than 2 introns and remove first exon
                exonKey = "{0},{1},{2},{3}".format(tx[0],tx[3],tx[4],tx[6])
                tx_id=tx[8].split(";")[1].split(" ")[2]
                if exonKey in exonTxH.keys():
                    exonTxH[exonKey].append(tx_id)
                else:
                    exonTxH[exonKey] = []
                    exonTxH[exonKey].append(tx_id)
                examineInternalExons(row)

            #rejectTx.append(row) 







