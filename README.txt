#######
getHomologSequences.py
#######

Given the Ensembl ID of a gene, the script retrieves the cDNA sequence of all known ortologues in the database.
Results are output in FastA format.

Example usage:
	python getHomologSequences.py -g ENSMUSG00000027168 -o homologSeq.fa