from xml.dom import minidom
import argparse
import urllib2

##### Parsing command line arguments #####
#parser = argparse.ArgumentParser()
#parser.add_argument('-g', '--gene', action = 'store', dest = 'gene', help = 'Target gene query. Use Ensembl ID.')
#parser.add_argument('-o', '--output', action = 'store', dest = 'outfile', help = 'Output file.')
#args = parser.parse_args()

gene = 'ENSMUSG00000027168'
outfile = 'homologs.fa'

##### Get XML over Ensembl REST API
gene_api = 'http://rest.ensembl.org/homology/id/'+gene+'?content-type=text/xml;type=orthologues;aligned=0;sequence=cdna'
gene_xml = urllib2.urlopen(geneAPI).read()
xmldoc = minidom.parseString(data)

##### Parse XML and write FASTA
homologs = xmldoc.getElementsByTagName('target')
seq_dict = {}
f = open(outfile, 'w')
for i in range(0, len(homologs) - 1):
    seq_id = '>'str(homologs[i].attributes['species'].value+'_'+homologs[i].attributes['id'].value)
    sequence = str(homologs[i].attributes['seq'].value)
    f.write(seq_id)
    f.write(sequence)
f.close()
