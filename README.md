# Bioinformatics
Simple python script for Bioinformatics. I made python code to generate dictionary for transcript ID: A to I mutation site both for hg38 and hg19 database.

## contents
- transcript_to_editing_hg38.pickle: transcript to A->I site location dictionary with HG38 database
- transcript_to_editing.pickle transcript to A->I site location dictionary with HG19 database
- intervals_to_transcript.pickle: interval tree data for transcript ID in HG19 database
- Human_AG_all_hg19.txt A to I mutation site downloaded from RADAR
- conversion script:
  - find_editting_site.py : generate HG19 based transcript to A to I database
  - find_editting_site_hg38.py: generate HG38 based transcript to A to I database
