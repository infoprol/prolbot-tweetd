# prolbot-tweetd

first crack at building an automatic invite flow from twitter -> slack.  this is the twitter daemon part, which is going to be built on top of python-twitter [TODO add href, etc]

## with python3, setting up your project virtual env sandbox is virtually painless... (pun intended)


* yeah, so, with python3, where $DIR is the base dir of your local copy of this very repo(such that this README.md is at $DIR/README.md),


* TO CRANK UP (activate) YOUR PYTHON VENV FOR THIS PROJECT: 

```cd <DIR>
python3 -m venv <DIR>
source <DIR>/bin/activate
pip install -r requirements.txt
```

* NOTE that the last line there is calling the "shimmed/virt" pip, so go to town installing, removing py packages all willy-nilly without
fear of breaking the python installs your system requires. 






* TO DE-activate (crank-down) YOUR PYTHON VENV FOR THIS PROJECT:


```source <DIR>/bin/deactivate
```

(i think, again, RTFM for venv - really, just python3, since venv has been swallowed into standard python3 dist...)



* IF YOU COMMIT ANY CHANGES THAT IMPORT MODULES FROM PACKAGES YOU INSTALLED IN YOUR VENV -

make sure you update requirements.txt with
`pip freeze > requirements`
that overwrite/not-append is intentional, and assumes you've already run the "crank-up" instructions.