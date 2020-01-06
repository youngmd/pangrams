# Pangrams

### Reads in a list of words and finds the highest possible score


## Puzzle

See https://fivethirtyeight.com/features/can-you-solve-the-vexing-vexillology/

The rules specify that 

* each word must have 4 letters
* must not contain 's'
* must contain the central letter
* must not contain any extra letters
* must form at least one pangram

## Method

The final rule lets us generate a list of candidate sets by finding all words that contain *exactly* 7 unique letters.  

Using these candidate sets we then evaluate each word in the dictionary for compliance with the rules and add it to the candidate set word list.

I set a threshold of 500 to identify "large sets" for further evaluation, which turned out to be 34 unique sets of letters.  

Each of these sets was then run through the full scoring routine having each candidate letter take the central position.  The highest total that also included at least one pangram was chosen as the winner for that set, and the highest total among all sets was selected.  The answer is given below.

## Solution

* Winning Set: AEGINRT
* Central Letter: R
* Total Score: 4036
* Number of Pangrams: 50
* Total Number of Words: 537

### Word Set:

['aerate', 'aerating', 'aerie', 'aerier', 'agar', 'ager', 'agger', 'aggregate', 'aggregating', 'aginner', 'agrarian', 'agree', 'agreeing', 'agria', 'aigret', 'aigrette', 'airer', 'airier', 'airing', 'airn', 'airt', 'airting', 'anear', 'anearing', 'anergia', 'angaria', 'anger', 'angering', 'angrier', 'anteater', 'antiair', 'antiar', 'antiarin', 'antra', 'antre', 'area', 'areae', 'arena', 'arenite', 'arete', 'argent', 'argentine', 'argentite', 'arginine', 'aria', 'arietta', 'ariette', 'arraign', 'arraigning', 'arrange', 'arranger', 'arranging', 'arrant', 'arrear', 'arrearage', 'artier', 'atria', 'attainer', 'attar', 'attire', 'attiring', 'attrite', 'eager', 'eagerer', 'eagre', 'earing', 'earn', 'earner', 'earning', 'earring', 'eater', 'eerie', 'eerier', 'eger', 'eggar', 'egger', 'egret', 'engager', 'engineer', 'engineering', 'engirt', 'engrain', 'engraining', 'enrage', 'enraging', 'enter', 'entera', 'enterer', 'entering', 'entertain', 'entertainer', 'entertaining', 'entire', 'entrain', 'entrainer', 'entraining', 'entrant', 'entreat', 'entreating', 'entree', 'ergate', 'erne', 'errant', 'errata', 'erring', 'etagere', 'eterne', 'gager', 'gagger', 'gainer', 'gaiter', 'ganger', 'gangrene', 'gangrening', 'garage', 'garaging', 'garget', 'garner', 'garnering', 'garnet', 'garni', 'garnierite', 'garret', 'garring', 'garter', 'gartering', 'gear', 'gearing', 'genera', 'generate', 'generating', 'genre', 'gerent', 'getter', 'gettering', 'ginger', 'gingering', 'ginner', 'ginnier', 'girn', 'girning', 'girt', 'girting', 'gittern', 'gnar', 'gnarr', 'gnarring', 'gnattier', 'grain', 'grainer', 'grainier', 'graining', 'gran', 'grana', 'grange', 'granger', 'granita', 'granite', 'grannie', 'grant', 'grantee', 'granter', 'granting', 'grat', 'grate', 'grater', 'gratin', 'gratine', 'gratinee', 'gratineeing', 'grating', 'great', 'greaten', 'greatening', 'greater', 'gree', 'greegree', 'greeing', 'green', 'greener', 'greengage', 'greenie', 'greenier', 'greening', 'greet', 'greeter', 'greeting', 'gregarine', 'greige', 'grig', 'grigri', 'grin', 'grinner', 'grinning', 'grit', 'grittier', 'gritting', 'igniter', 'inaner', 'inerrant', 'inert', 'inertia', 'inertiae', 'ingrain', 'ingraining', 'ingrate', 'ingratiate', 'ingratiating', 'inner', 'integer', 'integrate', 'integrating', 'intenerate', 'intenerating', 'inter', 'interage', 'intergang', 'intern', 'interne', 'internee', 'interning', 'interregna', 'interring', 'intertie', 'intrant', 'intreat', 'intreating', 'intrigant', 'irate', 'irater', 'iring', 'irrigate', 'irrigating', 'irritant', 'irritate', 'irritating', 'iterant', 'iterate', 'iterating', 'itinerant', 'itinerate', 'itinerating', 'nagger', 'naggier', 'naira', 'narine', 'narrate', 'narrater', 'narrating', 'natter', 'nattering', 'nattier', 'near', 'nearer', 'nearing', 'neater', 'negater', 'netter', 'nettier', 'nigger', 'niter', 'niterie', 'nitrate', 'nitrating', 'nitre', 'nitrite', 'nittier', 'raga', 'rage', 'ragee', 'raggee', 'ragging', 'ragi', 'raging', 'ragtag', 'raia', 'rain', 'rainier', 'raining', 'ranee', 'rang', 'range', 'ranger', 'rangier', 'ranging', 'rani', 'rant', 'ranter', 'ranting', 'rare', 'rarer', 'raring', 'ratan', 'ratatat', 'rate', 'rater', 'ratine', 'rating', 'ratite', 'rattan', 'ratteen', 'ratten', 'rattener', 'rattening', 'ratter', 'rattier', 'ratting', 'reagent', 'reaggregate', 'reaggregating', 'reagin', 'rear', 'rearer', 'rearing', 'rearrange', 'rearranging', 'reata', 'reattain', 'reattaining', 'reearn', 'reearning', 'reengage', 'reengaging', 'reengineer', 'reengineering', 'reenter', 'reentering', 'reentrant', 'regain', 'regainer', 'regaining', 'regatta', 'regear', 'regearing', 'regenerate', 'regenerating', 'regent', 'reggae', 'regina', 'reginae', 'regna', 'regnant', 'regrant', 'regranting', 'regrate', 'regrating', 'regreen', 'regreening', 'regreet', 'regreeting', 'regret', 'regretter', 'regretting', 'reign', 'reigning', 'reignite', 'reigniting', 'rein', 'reining', 'reinitiate', 'reinitiating', 'reintegrate', 'reintegrating', 'reinter', 'reinterring', 'reiterate', 'reiterating', 'renege', 'reneger', 'reneging', 'renig', 'renigging', 'renin', 'renitent', 'rennet', 'rennin', 'rent', 'rente', 'renter', 'rentier', 'renting', 'reran', 'rerig', 'rerigging', 'retag', 'retagging', 'retain', 'retainer', 'retaining', 'retarget', 'retargeting', 'rete', 'retear', 'retearing', 'retene', 'retia', 'retiarii', 'retie', 'retina', 'retinae', 'retine', 'retinene', 'retinite', 'retint', 'retinting', 'retirant', 'retire', 'retiree', 'retirer', 'retiring', 'retrain', 'retraining', 'retreat', 'retreatant', 'retreater', 'retreating', 'retting', 'riant', 'riata', 'rigger', 'rigging', 'ring', 'ringent', 'ringer', 'ringgit', 'ringing', 'rinning', 'rite', 'ritter', 'tagger', 'tagrag', 'tanager', 'tangerine', 'tangier', 'tanner', 'tantara', 'tantra', 'tare', 'targe', 'target', 'targeting', 'taring', 'tarn', 'tarre', 'tarrier', 'tarring', 'tart', 'tartan', 'tartana', 'tartar', 'tarter', 'tarting', 'tartrate', 'tatar', 'tater', 'tatter', 'tattering', 'tattier', 'tear', 'tearer', 'tearier', 'tearing', 'teenager', 'teener', 'teenier', 'teeter', 'teetering', 'tenner', 'tenter', 'tentering', 'tentier', 'terai', 'terete', 'terga', 'tergite', 'tern', 'ternate', 'terne', 'terra', 'terrae', 'terrain', 'terrane', 'terraria', 'terreen', 'terrene', 'terret', 'terrier', 'terrine', 'territ', 'tertian', 'tetra', 'tetter', 'tiara', 'tier', 'tiering', 'tiger', 'tinier', 'tinner', 'tinnier', 'tinter', 'tire', 'tiring', 'titer', 'titrant', 'titrate', 'titrating', 'titre', 'titter', 'titterer', 'tittering', 'tragi', 'train', 'trainee', 'trainer', 'training', 'trait', 'treat', 'treater', 'treating', 'tree', 'treeing', 'treen', 'tret', 'triage', 'triaging', 'triene', 'triennia', 'trier', 'trig', 'trigger', 'triggering', 'trigging', 'trine', 'trining', 'trinitarian', 'trite', 'triter']

