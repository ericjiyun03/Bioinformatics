# Bioinformatics
Python script for Bioinformatics code I made in Neoepiscope RNA editing project [see my forked neoepiscope github](https://github.com/ericjiyun03/neoepiscope). It generates dictionary for {transcript ID: A to I mutation site} both for hg38 and hg19 database.

## contents
- transcript_to_editing_hg38_new.pickle: transcript to A->I site location dictionary with HG38 database from (http://srv00.recas.ba.infn.it/atlas/claire.html)
- transcript_to_editing_hg38.pickle: transcript to A->I site location dictionary with HG38 database
- transcript_to_editing.pickle transcript to A->I site location dictionary with HG19 database
- intervals_to_transcript.pickle: interval tree data for transcript ID in HG19 database
- Human_AG_all_hg19.txt A to I mutation site downloaded from RADAR
- mapped: A to I mutation sites from HG38. Converted from Human_AG_all_hg19.txt using UCSC liftOver. 
- conversion script:
  - find_editting_site.py : generate HG19 based transcript to A to I database. It generate transcript_to_editing.pickle
  - find_editting_site_hg38.py: generate HG38 based transcript to A to I database. It generate transcript_to_editing_hg38.pickle
  - find_editting_site_hg38_new.py: generate HG38 based transcript to A to I database. It generate transcript_to_editing_hg38_new.pickle
  - those transcript to A to I database pickle file will be used in neoepiscope for RNA editting. See [my forked neoepiscope github](https://github.com/ericjiyun03/neoepiscope)
