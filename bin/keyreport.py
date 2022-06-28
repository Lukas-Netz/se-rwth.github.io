import bibtexparser
from os import listdir
from os.path import isfile, join

def getmdkeys(path):
    with open(path) as mbse:
        mbse_data = mbse.read()

    start = mbse_data.find('keys')
    end = mbse_data.find('---', start)

    all_keys = mbse_data[start+6:end]
    res = all_keys.replace('\n', '').replace(' ', '').strip('][').split(',')

    return res


def getbibkeys(path):
    with open(path) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    bibtexlist = bib_database.entries
    keylist = []

    for entry in bibtexlist:
        keylist.append(entry.get('key'))

    return (keylist)


def checkkeys(mdkeys, bibkeys):
    missing_keys = []
    for key in mdkeys:
         if (not (key in bibkeys)):
             missing_keys.append(key)
    return missing_keys


def main(filepath,bibpath):
    files = [f for f in listdir(filepath) if isfile(join(filepath, f))]
    bib_keys = getbibkeys(bibpath+'/all-software-engineering-rwth-references.bib')
    bib_keys_new = getbibkeys(bibpath+'/additional-bib-entries.bib')
    bib_keys.extend(bib_keys_new)
    with open("keyreport.md", "w") as text_file:
        for file in files:
            keys = getmdkeys(filepath+'/'+file)
            missing = checkkeys(keys, bib_keys)
            text_file.write('### Missing keys from '+file+':\n')
            for key in missing:
                text_file.write('* '+key+'\n')
            text_file.write('\n')

if __name__ == "__main__":
    main('_pages/research','assets/bibliography')
