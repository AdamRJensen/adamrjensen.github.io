# Author: Chris Holdgraf
# https://chrisholdgraf.com/blog/2022/orcid-auto-update/

import pandas as pd
import requests
from pathlib import Path
from rich import progress

# My ORCID
orcid_id = "0000-0002-5554-9856"
ORCID_RECORD_API = "https://pub.orcid.org/v3.0/"

# Download all of my ORCID records
print("Retrieving ORCID entries from API...")
response = requests.get(url=requests.utils.requote_uri(ORCID_RECORD_API + orcid_id),
                        headers={'Accept': 'application/json'})
response.raise_for_status()
orcid_record = response.json()
# Retrieve authors last name from orcid record (avoids hard-coding later)
orcid_id_last_name = orcid_record['person']['name']['family-name']['value'].lower()

###
# Resolve my DOIs from ORCID as references
# Shamelessly copied from:
# https://gist.github.com/brews/8d3b3ede15d120a86a6bd6fc43859c5e
import requests
import json


def fetchmeta(doi, fmt='reference', **kwargs):
    """Fetch metadata for a given DOI.

    Parameters
    ----------
    doi : str
    fmt : str, optional
        Desired metadata format. Can be 'dict' or 'bibtex'.
        Default is 'dict'.
    **kwargs :
        Additional keyword arguments are passed to `json.loads()` if `fmt`
        is 'dict' and you're a big JSON nerd.

    Returns
    -------
    out : str or dict or None
        `None` is returned if the server gives unhappy response. Usually
        this means the DOI is bad.

    Examples
    --------
    >>> fetchmeta('10.1016/j.dendro.2018.02.005')
    >>> fetchmeta('10.1016/j.dendro.2018.02.005', 'bibtex')

    References
    ----------
    https://www.doi.org/hb.html
    """
    # Parse args and setup the server response we want.
    accept_type = 'application/'
    if fmt == 'dict':
        accept_type += 'citeproc+json'
    elif fmt == 'bibtex':
        accept_type += 'x-bibtex'
    elif fmt == "reference":
        accept_type = "text/x-bibliography; style=apa"
    else:
        raise ValueError(f"Unrecognized `fmt`: {fmt}")

    # Request data from server.
    url = "https://dx.doi.org/" + str(doi)
    header = {'accept': accept_type}
    r = requests.get(url, headers=header)

    # Format metadata if server response is good.
    out = None
    if r.status_code == 200:
        if fmt == 'dict':
            out = json.loads(r.text, **kwargs)
        else:
            out = r.text
    return out


# %%
# Extract metadata for each entry
dois = []

df = []
for iwork in progress.track(orcid_record["activities-summary"]["works"]["group"], "Fetching reference data..."):
    isummary = iwork["work-summary"][0]

    # Extract the DOI
    for ii in isummary["external-ids"]["external-id"]:
        if ii["external-id-type"] == "doi":
            doi = ii["external-id-value"]
            break

    if doi not in dois:
        dois.append(doi)    

        meta = fetchmeta(doi, fmt="dict")
        if meta['type'] not in ['thesis']:
            doi_url = meta["URL"]
            title = meta["title"]
            # references_count = meta["references-count"]
            year = meta["issued"]["date-parts"][0][0]
            url = meta["URL"]
    
            # Create authors list with links to their ORCIDs
            authors = meta["author"]
            autht = []
            authors_parsed = []
            for author in authors:
                if author not in authors_parsed:
                    authors_parsed.append(author)
                    # Modified to also show middle name initials correctly
                    name = f"{author['family']}, {' '.join([s[0]+'.' for s in author['given'].split()])[:-1]}."
                    # Bold name of author of interst and always link to orcid
                    if orcid_id_last_name in author["family"].lower():
                        autht.append(f"[**{name}**]({ORCID_RECORD_API + orcid_id})")
                    elif "ORCID" in author:
                        autht.append(f"[{name}]({author['ORCID']})")
                    else:
                        autht.append(name)
            autht = ", ".join(autht)
    
            journal = meta.get('container-title', None)
            # if meta['type'] == 'journal-article':
            #     journal = meta['container-title-short']
            # else:
            #     journal = meta["publisher"]
    
            # if 'assessing' in title.lower():
            #     raise ValueError
    
            url_doi = url.split("//", 1)[-1]
            reference = f"{autht} ({year}). **{title}**. {journal}. doi:&nbsp;[{doi}]({url})" # non-breaking space between doi text and number
            df.append({"year": year, "reference": reference})
df = pd.DataFrame(df)

# Convert into a markdown string
md = []
for year, items in df.groupby("year", sort=False):
    md.append(f"## {year}")
    for _, item in items.iterrows():
        md.append(item["reference"])
        md.append("")
    md.append("")
mds = "\n".join(md)

# This will only work if this is run as a script
path_out = Path(__file__).parent.parent / "_static/publications.txt"
path_out.write_text(mds, encoding='utf-8')
print(f"Finished updating ORCID entries at: {path_out}")
