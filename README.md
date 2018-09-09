## Getenberg

Classic books analysis on [Pride and Prejudice](http://www.gutenberg.org/ebooks/1342).

### The problem solved

1.  Count the number of words.
2.  Count the number of unique words.
3.  Get 20 most frequent words.
4.  Get top frequent meaningful words.
5.  Get 20 less frequent words.
6.  Get the frequency of a certain word.
7.  Get the chapter number given a famous quote.
8.  Generate a twenty-word sentence using random words appeared in the book.
9.  Get all the sentence given a prefix.
10. Given part of a famous quote, return the whole sentence.

### Sample output

The output below is generate by running `python main.py`.

-----------2a-----------

125900

-----------2b-----------

6528

-----------2c-----------

[['the', 4507], ['to', 4243], ['of', 3728], ['and', 3658], ['her', 2225], ['i', 2070], ['a', 2012], ['in', 1937], ['was', 1848], ['she', 1710], ['that', 1594], ['it', 1550], ['not', 1450], ['you', 1428], ['he', 1339], ['his', 1271], ['be', 1260], ['as', 1191], ['had', 1176], ['with', 1100]]

-----------2d-----------

[['i', 2070], ['not', 1450], ['mr', 786], ['s', 661], ['elizabeth', 635], ['darcy', 418], ['mrs', 343], ['am', 324], ['bennet', 323], ['bingley', 306], ['jane', 295], ['miss', 283], ['should', 250], ['herself', 227], ['though', 226], ['never', 220], ['sister', 218], ['soon', 216], ['might', 200], ['wickham', 194]]

-----------2e-----------

[['wiser', 1], ['withdrawing', 1], ['wisher', 1], ['wives', 1], ['withstood', 1], ['wits', 1], ['woe', 1], ['worthlessness', 1], ['wretchedly', 1], ['witnessing', 1], ['witty', 1], ['womanly', 1], ['witticisms', 1], ['zip', 1], ['yawning', 1], ['yawned', 1], ['york', 1], ['yards', 1], ['writes', 1], ['youths', 1]]

-----------3a-----------

[1, 0, 7, 5, 1, 6, 5, 14, 7, 4, 3, 3, 0, 1, 2, 3, 2, 15, 0, 0, 10, 0, 5, 9, 8, 7, 2, 3, 7, 1, 2, 2, 2, 4, 15, 5, 0, 2, 3, 8, 5, 4, 6, 7, 4, 4, 8, 3, 7, 3, 11, 8, 12, 5, 12, 5, 3, 6, 1, 3, 6]

-----------4a-----------

1

-----------5a-----------

the deficiency of society can spare from seeing you pay to introduce yourself into it wholly engrossed by bringing me

-----------6a-----------
I do not know a place in the country that is equal to netherfield.

I do not know the particulars, but i know very well that mr.

I do not know whether i ever before mentioned to you my feelings on this subject; but i will not leave the country without confiding them, and i trust you will not esteem them unreasonable.

I do not know anybody who seems more to enjoy the power of doing what he likes than mr.

I do not know who is good enough for him.

I do not know of any other designs that he had formed; but he was in such a hurry to be gone, and his spirits so greatly discomposed, that i had difficulty in finding out even so much as this.

I do not like to boast of my own child, but to be sure, jane--one does not often see anybody better looking.

I do not trust my own partiality.

I do not believe she often sees such at home.

I do not remember her name among the ladies at court.

I do not mean, however, to assert that we can be justified in devoting too much of our time to music, for there are certainly other things to be attended to.

I do not at all comprehend her reason for wishing to be intimate with me; but if the same circumstances were to happen again, i am sure i should be deceived again.

I do not think it is very pretty; but i thought i might as well buy it as not.

I do not deserve it.

-----------7a-----------

it is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. - Chapter 1

### Todo

- Enhance language processing and analysis power
