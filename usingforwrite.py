import json

with open("dchapter1.json", 'r') as file:
    dchapter1 = json.load(file)

dchapter1["Dialog1"] = "Kdyz ses vzbudil, vsude kolem bylo vlhko, kameni, prasno, kaslajici lidi, jsi  absolutne zmateny, trpis bolesti hlavy. Netusis, kde jsi, vlastne ani netusis, kdo jsi. Pri pokusu se zvednout, abys alespon trochu nabul dojmu, ze si porad panem situace si zjistil, ze ti krvacela urcite hlava, coz by vysvetlovalo ztratu pameti. Co se me stalo? Proc mam diru v hlave? Sakra co tu vubec delam... rikas si.Pri prvnim rozhlidnuti se, vidis obrovskou jeskyni osvetlenou loucemi ustici do dalsich chodeb, kdy v jeskyne konci mrizemi, za kterymi stoji straz, coz v tobe vubec neprobouzi dobre pocity a nadeji dostat se odsud. Jeskyne je opravdu rozlehla, muzes videt cast lidi co kuta skalu, cast lidi co spi, cast lidi, co si povida a pak nejake samotare."

with open("dchapter1.json", 'w') as file:
    json.dump(dchapter1, file)