from xml.dom import minidom
import argparse
import urllib2

##### Parsing command line arguments #####
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--gene', action = 'store', dest = 'gene', help = 'Target gene query. Use Ensembl ID.')
parser.add_argument('-o', '--output', action = 'store', dest = 'outfile', help = 'Output file.')
args = parser.parse_args()

gene = args.gene
outfile = args.outfile

##### Get XML over Ensembl REST API
gene_api = 'http://rest.ensembl.org/homology/id/'+gene+'?content-type=text/xml;type=orthologues;aligned=0;sequence=cdna'
gene_xml = urllib2.urlopen(gene_api).read()
xmldoc = minidom.parseString(gene_xml)

##### Parse XML and write FASTA
homologs = xmldoc.getElementsByTagName('target')
f = open(outfile, 'w')
for i in range(0, len(homologs) - 1):
    seq_id = '>'+str(homologs[i].attributes['species'].value+'_'+homologs[i].attributes['id'].value)
    sequence = str(homologs[i].attributes['seq'].value)
    f.write(seq_id+'\n')
    f.write(sequence+'\n')
f.close()
