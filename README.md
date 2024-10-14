# ConflictMinerals_SECsearch
Use this tool to investigate corporations' use of conflict minerals and what, if any, responsibility measures are being applied by searching SEC Specialized Disclosures.

This tool was built in support of transparency and worker power. Learn more about the use case: [Chip Workers 4 Responsible Mining](https://www.cw4rm.org/). 
- [CW4RM Presentation at CIRCUIT BREAKERS CONFERENCE 2024](https://static1.squarespace.com/static/668ae83b4af380120c2767a0/t/670b5472352d6c38efc24cc2/1728795766212/241012+Circuit+Breakers+Conflict+Mineral+Workshop+%28External%29+V1.pdf)


Working jointly with a member of the semiconductor industry, this tool was built as a wrapper for the SEC's [EDGAR Full Text Search API](https://sec-api.io/docs/full-text-search-api). By running the workflow, you will receive a csv with the minerals and responsibility partners listed in a corporation's Specialized Disclosure. 

This tool supports efforts by member organizations to eliminate human rights abuses and
environmental damage associated with upstream actors in the semiconductor supply
chain, by first answering the following questions: 

* Does my company use conflict minerals in our products? 
* What is my company doing to ensure equitable treatment for mining communities? 


## Quick Start

> [!IMPORTANT]
> Before you start, you will need to obtain your own SEC API key. You can do that here: [https://sec-api.io/signup/free](https://sec-api.io/signup/free)

* Fork the repo
* Add your SEC API Key as a repo secret. Be sure to name it "KEY"
  * [Github's Guide for this](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)
* Update the file `company_names.py` to include the companies you want to search for
  * **be sure to format as an array of strings, e.g `["Company A", "Company B", "Company C"]`**
* Run as Github Action
  * On the menu bar click "Actions" 
    ![screenshot showing the menu bar, with the actions button circled](images/ss_1.PNG)
  * Click on the workflow name `py`
    ![screenshot showing workflowname](images/ss_2.PNG)
  * Then, click "Run workflow" button (look to the right in the workflow table for the button)
    ![screenshot showing run workflow button](images/ss_3.PNG)
* Navigate back to the main repo to find the output file (`output.csv`)
  ![screenshot showing repo with output file circled](images/ss_4.PNG)
* Click on the output file, and then download
  ![screenshot showing file download button](images/ss_5.PNG)

## Helpful links 

* [Chip Workers 4 Responsible Mining](https://www.cw4rm.org/)
* This repo relies on the Securities and Exchange Commission's [EDGAR Database Full Text Search API](https://sec-api.io/docs/full-text-search-api)
* What is a Specialized Disclosure? [Thomas Reuters Practical Law](https://content.next.westlaw.com/practical-law/document/Icf49605def0a11e28578f7ccc38dcbee/Form-SD?viewType=FullText&transitionType=Default&contextData=(sc.Default))
* Who is filing Specialized Disclosures? [Ropes & Gray](https://www.ropesgray.com/en/insights/viewpoints/102ik3y/conflict-minerals-rule-filing-statistics-released-how-does-your-company-stack)
* Specilized Disclosure Form from the SEC - [Template](https://www.sec.gov/files/formsd.pdf)


## Forthcoming

In the near future, there will be an option to use this workflow straight from a web interface. 

Benefits of this option:
* this tool will be accesible to a wider population
* a user would not need their own api key

Here's what this could like: 

![wireframe showing web browser view of webpage that includes about section, search bar, and tips](images/shortterm_wireframe.png)
