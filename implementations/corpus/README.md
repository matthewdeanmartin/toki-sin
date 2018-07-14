corpus
------
A corpus is a body of texts. Field linguists gather them from living, speaking subjects.

canonical
---------
In conlang creation, we have texts that are canonical, i.e. they are correct by dint of the language creation authority, either the artist, committee or what have you.  We would expect a parser to parse eveything in the canonical corpus, or there is a mistake in the corpus.

community
---------
Humans write texts and these sometimes are wrong, sometimes are wrong but, hey it is a human activity and that is how people roll. Your parser needs to be able to cope with it, either by failing gracefully or by incorporating the rules implicit in community created speech. If enough people make an error, systematically enough, in natural languages that is the new rule.

format
------
Texts are ascii and end in .txt.  If you have meta data, put it in a .ini file of the same name. 

In languages used on the internet, it is inevitable that a corpus texts will be a mixture of:

- different encodings
- different languages
- html and other markup language
- white space and punctuation that is used in a surprising way, but had meaning to the writer, for example, larger blocks of white space used instead of periods to end sentences.

