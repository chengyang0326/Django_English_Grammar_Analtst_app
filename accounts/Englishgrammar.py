#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 14:54:39 2022

@author: cheng
"""

from parsimonious.grammar import Grammar


grammar = Grammar(r"""
                 
                  paragraph= (sentence space (sentence)*)/sentence
                  sentence =statement /question /command
                  statement = (subject space action space  object punctation)/(subject space action space proposition space  object punctation)/(subject space action punctation)
                  question = (verb space subject space action space  object punctation) / (Question_word space verb space subject space action space  object punctation)/(verb space subject space action punctation)/(Question_word space verb space subject space action punctation)
                  command = action space  object punctation
                  subject =   (article (adjective)* space noun)/(article noun)/(pron (adjective)* space noun)/(pron noun)/(pron)/((adjective)* space noun)/(noun)
                  object =  (article (adjective)* space noun)/(article noun)/(pron (adjective)* space noun)/(pron noun)/(pron)/((adjective)* space noun)/(noun)
                  action  =   ((adv)* space verb)/(verb space (adv) )/verb
                  noun='time'/ 'year'/  'people'/ ' way'/ 'day'/  'man'/ 'thing'/  'woman'/  'life'/ 'child'/  'world'/ 'school'/  'state'/  'family' /'student'/  'group'/ 'country'/  'problem'/ 'hand'/   'part'/ 'place'/  'case'/  'week'/  'company'/ 'system'/  'program'/  'question'/  'work'/  'government'/  'number'/  'night'/ 'point'/  'home'/  'water'/  'room' / 'mother'/ 'area'/ 'money' /'story'/ 'fact'/ 'month'/ 'lot'/ 'right'/ 'study'/ 'book'/ 'eye'/ 'job'/ ' word'/  'business'/   'issue'/ 'side'/ 'kind'/ 'head'/  'house'/ 'service'/ 'friend'/ 'father'/ 'power'/ 'hour'/ 'game'/ 'line'/ 'end'/ 'member'/ 'law'/ 'car'/  'city'/ 'community'/ 'name'/ ' president'/ 'team'/ 'minute'/ 'idea' /'kid'/  'body'/ 'information'/ 'back'/   'parent'/ 'face'/'others'/'level'/ 'office'/ 'door'/ 'health' /'person'/   'art' /'war'/ 'history'/ 'party'/'result'/'change'/ 'morning'/ 'reason'/ 'research'/ 'girl'/ 'guy'  / 'moment' /'air' / 'teacher' /'force'/ 'education'/'times'/ 'years'/   ' ways'/ 'days'/  'men'/ 'things'/  'women'/  'lives'/ 'children'/  'worlds'/ 'schools'/  'states'/  'families' /'students'/  'groups'/ 'countries'/  'problems'/ 'hands'/   'parts'/ 'places'/  'cases'/  'weeks'/  'companies'/ 'systems'/  'programs'/  'questions'/  'works'/  'governments'/  'numbers'/  'nights'/ 'points'/  'homes'/  'rooms' /  'moneys' /'stories'/ 'facts'/ 'months'/ 'lots'/ 'rights'/ 'studies'/ 'books'/ 'eyes'/ 'jobs'/ ' words'/     'issues'/ 'sides'/ 'kinds'/ 'heads'/  'houses'/ 'services'/ 'friends'/  'powers'/ 'hours'/ 'games'/ 'lines'/ 'ends'/ 'members'/ 'laws'/ 'cars'/  'cities'/ 'communities'/ 'names'/ ' presidents'/ 'teams'/ 'minutes'/ 'ideas' /'kids'/  'bodies'/ 'informations'/   'parents'/ 'faces'/'other'/ 'offices'/ 'doors' / 'arts' /'wars'/ 'histories'/ 'parties'/'results'/ 'mornings'/ 'reasons'/ 'girls'/ 'guys'  / 'moments' /'airs' / 'teachers' /'forces'



                  article= 'a'/'A'/'the'/'The'/'an'/'An'
                  proposition ='at'/'by'/'for'/'on'/'to'
                  pron= 'I'/'you'/'You'/'he'/'He'/'she'/'She'/'they'/'They'/ 'it'/'It'
                  verb ='are'/'is'/'am'/  'have'/'do'/'say'/  'go'/'can'/'get'/'would'/'make'/'know'/'will'/'think'/  'take'/  'see'/'come'/  'could'/'want'/'look'/'use'/'find'/  'give'/'tell'/'work'/'may'/  'should'/'call'/'try'/'ask'/'need'/'feel'/'become'/'leave'/'put'/'mean'/'keep'/'let'/'begin'/  'seem'/  'help'/'talk'/'turn'/'start'/'might'/'show'/'hear'/'play'/  'run'/'move'/'like'/'live'/'believe'/'hold'/'bring'/'happen'/'must'/'write'/'provide'/  'sit'/'stand'/'lose'/'pay'/'meet'/'include'/'continue'/'set'/'learn'/'change'/'lead'/'understand'/'watch'/'follow'/'stop'/'create'/'speak'/  'read'/'allow'/'add'/'spend'/'grow'/'open'/  'walk'/'win'/'offer'/  'remember'/'love'/'consider'/'appear'/'buy'/'wait'/  'serve'/'die'/'send'/'expect'/'build'/'stay'/'fall'/'cut'/'reach'/'were'/'was'/   'has'/'had'/'do'/'did'/'done'/'said'/'says'/  'goes'/'gone'/'going'/'can'/'could'/'get'/  'got'/'geting'/'would'/'make'/'made'/'making'/'known'/'knew'/'will'/'think'/'thinks'/'thinking'/'take'/'taking'/'takes'/'taken'/  'see'/'saw'/'seeing'/'come'/'coming'/'came'/  'could'/'want'/'wanted'/'wanting'/'look'/'looking'/'looked'/'use'/'using'/'used'/  'find'/'finding'/'found'/'give'/'gave'/'giving'/'tell'/'tells'/'told'/  'work'/'worked'/'working'/'may'/'might'/  'should'/'call'/'calling'/  'try'/'trying'/'ask'/'asking'/'asked'/'need'/'feel'/'become'/'leave'/'put'/'mean'/'keep'/'let'/'begin'/  'seem'/  'help'/'talk'/'turn'/'start'/'might'/'show'/'hear'/'play'/  'run'/'move'/'like'/'live'/'believe'/'hold'/'bring'/'happen'/'must'/'write'/'provide'/  'sit'/'stand'/'lose'/'pay'/'meet'/'include'/'continue'/'set'/'learn'/'change'/'lead'/'understand'/'watch'/'follow'/'stop'/'create'/'speak'/  'read'/'allow'/'add'/'spend'/'grow'/'open'/  'walk'/'win'/'offer'/  'remember'/'love'/'consider'/'appear'/'buy'/'wait'/  'serve'/'die'/'send'/'expect'/'build'/'stay'/'fall'/'cut'/'reach' /'Are'/'Is'/'Am'/  'Have'/'Do'/'Say'/  'Go'/'Can'/'Get'/'Would'/'Make'/'Know'/'Will'/'Think'/  'Take'/  'See'/'Come'/  'Could'/'Want'/'Look'/'Use'/'Find'/  'Give'/'Tell'/'Work'/'May'/  'Should'/'Call'/'Try'/'Ask'/'Need'/'Feel'/'Become'/'Leave'/'Put'/'Mean'/'Keep'/'Let'/'Begin'/  'Seem'/  'Help'/'Talk'/'Turn'/'Start'/'Might'/'Show'/'Hear'/'Play'/  'Run'/'Move'/'Like'/'Live'/'Believe'/'Hold'/'Bring'/'Happen'/'Must'/'Write'/'Provide'/  'Sit'/'Stand'/'Lose'/'Pay'/'Meet'/'Include'/'Continue'/'Set'/'Learn'/'Change'/'Lead'/'Understand'/'Watch'/'Follow'/'Stop'/'Sreate'/'Speak'/  'Read'/'Allow'/'Add'/'Apend'/'Grow'/'Open'/  'Walk'/'Win'/'Offer'/  'Remember'/'Love'/'Consider'/'Appear'/'Buy'/'Wait'/  'Serve'/'Die'/'Send'/'Expect'/'Build'/'Stay'/'Fall'/'Cut'/'Reach'/'Were'/'Was'/   'Has'/'Had'/'Do'/'Did'/'Done'/'Said'/'Says'/  'Goes'/'Gone'/'Going'/'Can'/'Could'/'Get'/  'Got'/'Geting'/'Would'/'Make'/'Made'/'Making'/'Known'/'Knew'/'Will'/'Think'/'Thinks'/'Thinking'/'Take'/'Taking'/'Takes'/'Taken'/  'See'/'Saw'/'Seeing'/'Come'/'Coming'/'Came'/  'Could'/'Want'/'Wanted'/'Wanting'/'Look'/'Looking'/'Looked'/'Use'/'Using'/'Used'/  'Find'/'Finding'/'Found'/'Give'/'Gave'/'Giving'/'Tell'/'Tells'/'Told'/  'Work'/'Worked'/'Working'/'May'/'Might'/  'Should'/'Call'/'Calling'/  'Try'/'Trying'/'Ask'/'Asking'/'Asked'/'Need'/'Feel'/'Become'/'Leave'/'Put'/'Mean'/'Keep'/'Let'/'Begin'/  'Seem'/  'Help'/'Talk'/'Turn'/'Start'/'Might'/'Show'/'Hear'/'Play'/  'Run'/'Move'/'Like'/'Live'/'Believe'/'Hold'/'Bring'/'Happen'/'Must'/'Write'/'Provide'/  'Sit'/'Stand'/'Lose'/'Pay'/'Meet'/'Include'/'Continue'/'Set'/'Learn'/'Change'/'Lead'/'Understand'/'Watch'/'Follow'/'Stop'/'Create'/'Speak'/  'Read'/'Allow'/'Add'/'Spend'/'Grow'/'Open'/  'Walk'/'Win'/'Offer'  


                  space = " "
                  adjective = 'able'/ 'bad'/ 'best'/ 'better'/ 'big'/ 'black'/ 'certain'/'clear'/ 'different'/ 'early'/ 'easy'/ 'economic'/ 'federal'/ 'free'/ 'full'/ 'good'/ 'great'/ 'hard'/ 'high'/ 'human'/ 'important'/ 'international'/ 'large'/ 'late'/ 'little'/ 'local'/ 'long'/ 'low'/ 'major'/ 'military'/ 'national'/ 'new'/ 'old'/ 'only'/ 'other'/ 'political'/ 'possible'/ 'public'/ 'real'/ 'recent'/ 'right'/ 'small'/ 'social'/ 'special'/ 'strong'/ 'sure'/ 'true'/ 'white'/ 'whole'/ 'young'/'Able'/ 'Bad'/ 'Best'/ 'Better'/ 'Big'/ 'Black'/ 'Certain'/'Clear'/ 'Different'/ 'Early'/ 'Easy'/ 'Economic'/ 'Federal'/ 'Free'/ 'Full'/ 'Good'/ 'Great'/ 'Hard'/ 'High'/ 'Human'/ 'Important'/ 'International'/ 'Large'/ 'Late'/ 'Little'/ 'Local'/ 'Long'/ 'Low'/ 'Major'/ 'Military'/ 'National'/ 'New'/ 'Old'/ 'Only'/ 'Other'/ 'Political'/ 'Possible'/ 'Public'/ 'Real'/ 'Recent'/ 'Right'/ 'Small'/ 'Social'/ 'Special'/ 'Strong'/ 'Sure'/ 'True'/ 'White'/ 'Whole'/ 'Young'




                  adv ='boldly'/ 'brightly'/ 'cheerfully'/ 'faithfully'/ 'fortunately'/ 'gleefully'/ 'gracefully'/ 'happily'/ 'honestly'/ 'innocently'/ 'kindly'/ 'perfectly'/ 'powerfully'/ 'safely'/ 'warmly'/'always'/ 'daily'/ 'eventually'/ 'finally'/ 'frequently'/ 'generally'/ 'hourly'/ 'later'/ 'never'/ 'nightly'/'Boldly'/ 'Brightly'/ 'Cheerfully'/ 'Faithfully'/ 'Fortunately'/ 'Gleefully'/ 'Gracefully'/ 'Happily'/ 'Honestly'/ 'Innocently'/ 'Kindly'/ 'Perfectly'/ 'Powerfully'/ 'Safely'/ 'Warmly'/'Always'/ 'Daily'/ 'Eventually'/ 'Finally'/ 'Frequently'/ 'Generally'/ 'Hourly'/ 'Later'/ 'Never'/ 'Nightly'



                  
                  Question_word= 'When'/'What'/'Where'/'How'/'Who'/'Why'/'Which'/'Whose'
                  
                  punctation= "."/"!"/"?"
                  
  
  

""")



sentence_counter=0
noun_counter=0
verb_counter=0
article_counter=0
proposition_counter=0
pronoun_counter=0
space_counter=0
adjective_counter=0
adverb_counter=0
Question_word_counter=0
punctation_counter=0








# print("sentence: ", x)
