# SPAM/HAM CLASSIFIER 

This classifier is written in Python and the web applciation is built using FLASK. 

The Enron Email Corpus is used for training the mode. It is one of the biggest email data sources in the world. It has 600,000 emails spread over 2.5 GB. 

Naive Bayes classifier is built on the train data after tokenizing the sentences and creating the word features. The accuracy on the test data turned out to be 98.92%.

Here are some of the most informative features derived from the model:

Most Informative Features
                    meds = True             spam : ham    =    299.0 : 1.0
                     xls = True              ham : spam   =    287.4 : 1.0
                     713 = True              ham : spam   =    271.1 : 1.0
                 stinson = True              ham : spam   =    268.4 : 1.0
                crenshaw = True              ham : spam   =    268.4 : 1.0
                     ect = True              ham : spam   =    226.2 : 1.0
                     eol = True              ham : spam   =    212.9 : 1.0
             medications = True             spam : ham    =    209.1 : 1.0
              scheduling = True              ham : spam   =    205.6 : 1.0
                  louise = True              ham : spam   =    200.5 : 1.0
                     hpl = True              ham : spam   =    194.4 : 1.0
                 parsing = True              ham : spam   =    192.7 : 1.0
                     oem = True             spam : ham    =    173.6 : 1.0
                    pill = True             spam : ham    =    166.4 : 1.0
                   daren = True              ham : spam   =    163.3 : 1.0
                    1933 = True             spam : ham    =    144.4 : 1.0
               schedules = True              ham : spam   =    136.9 : 1.0
                     sex = True             spam : ham    =    132.4 : 1.0
                   penis = True             spam : ham    =    125.1 : 1.0
                      um = True             spam : ham    =    124.4 : 1.0

