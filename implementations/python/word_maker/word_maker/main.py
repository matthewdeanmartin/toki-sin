# coding=utf-8
"""

Spec:

By config, generate words.

- optionally, exclude cognates with English & other languages
- optionally, eliminate minimal pairs
- optionally, ensure some % of rhyming pairs (this interacts with minimal pairs, if you ban minimal pairs
 then you will only rhyme 2 syllable words)

This isn't a general purpose word generator, it is aimed at simple toki pona-like languages.

- Won't support IPA
- Won't support complex sandhi or tricky morphology rules

Should allow for:

- prohibitted starts, ends, syllablres
- onset -coda p

"""