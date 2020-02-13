# TrNER
Turkish Name Entitiy Recognition with PolyGlot
1-Install Package
pip install polyglot
pip install pyicu
!pip install -U pycld2
!pip install Morfessor

2-Import Package
import polyglot
from polyglot.text import Text

3-%%bash
polyglot download embeddings2.tr ner2.tr

4-Insert dataset in .txt file

5-Print most common Name Entity
