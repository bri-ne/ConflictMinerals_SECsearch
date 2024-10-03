# ConflictMinerals_SECsearch
Use this tool to investigate corporations' use of conflict minerals by searching SEC Specialized Disclosures 

## Quick Start

* Fork the repo
* Update the file `company_names.py` to include the companies you want to search for
  * **be sure to format as an array of strings, e.g `["Company A", "Company B", "Company C"]`**
* Run as Github Action
  * On the menu bar click "Actions" 
    * ![screenshot showing the menu bar, with the actions button circled](.images/ss_1.PNG)
  * Click on the workflow name `py`
    * ![screenshot showing workflowname](.images/ss_2.PNG)
  * Then, click "Run workflow" button (look to the right in the workflow table for the button)
    * ![screenshot showing run workflow button](.images/ss_3.PNG)
* Navigate back to the main repo to find the output file (`output.csv`)
  * ![screenshot showing repo with output file circled](.images/ss_4.PNG)
  * click it, and then download
    * ![screenshot showing file download button](.images/ss_5.PNG)

## Helpful links 

* This repo relies on the Securities and Exchange Commission's [EDGAR Database Full Text Search API](https://sec-api.io/docs/full-text-search-api)
