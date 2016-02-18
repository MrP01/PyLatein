var persons=["sg1", "sg2", "sg3", "pl1", "pl2", "pl3"];

var endings={
    "std": {"sg1":"o", "sg2":"s", "sg3":"t",
            "pl1":"mus", "pl2":"tis", "pl3":"nt"},
    "perf": {"sg1":"i", "sg2":"isti", "sg3":"it",
            "pl1":"imus", "pl2":"istis", "pl3":"erunt"},
    "impf": {"sg1":"m", "sg2":"s", "sg3":"t",
            "pl1":"mus", "pl2":"tis", "pl3":"nt"},
    "plqpf": {"sg1":"eram", "sg2":"eras", "sg3":"erat",
            "pl1":"eramus", "pl2":"eratis", "pl3":"erant"},
    "fut2": {"sg1":"ero", "sg2":"eris", "sg3":"erit",
            "pl1":"erimus", "pl2":"eritis", "pl3":"erint"}
};

function assignEndings(result, prefix, stem, vocal, ends){
    for (var p=0; p < persons.length; p++){
        result[prefix+persons[p]]=stem+vocal+ends[persons[p]];}
    return result;
}

function conjugate(present_stem, perfect_stem, conjugation){
    var result={};

    //vocal
    var vocal="";
    if(conjugation == "A"){vocal="a"}
    else if (conjugation == "E"){vocal="e"}
    else{vocal="i"}

    //perfect_stem
    if (perfect_stem == "__auto__"){
        if (conjugation == "A"){
            perfect_stem=present_stem+"av";}
        else if (conjugation == "E"){
            perfect_stem=present_stem+"u";}
        else if (conjugation == "I"){
            perfect_stem=present_stem+"iv";}
    }

    //infinitive and imperatives
    if (conjugation == "C" || conjugation == "M"){
        result.infinitive=present_stem+"ere";
        result.imperative_sg=present_stem+"e!";
        result.imperative_pl=present_stem+"ite!";
    }
    else{
        result.infinitive=present_stem+vocal+"re";
        result.imperative_sg=present_stem+vocal+"!";
        result.imperative_pl=present_stem+vocal+"te!";
    }

    //present
    assignEndings(result, "present_", present_stem, vocal, endings.std);
    if (conjugation == "A" || conjugation == "C"){
        result.present_sg1=present_stem+endings.std.sg1;}
    else{result.present_sg1=present_stem+vocal+endings.std.sg1;}
    if (conjugation == "C"){
        result.present_pl3=present_stem+"u"+endings.std.pl3;}
    else if (conjugation == "I" || conjugation == "M"){
        result.present_pl3=present_stem+vocal+"u"+endings.std.pl3;}
    else{result.present_pl3=present_stem+vocal+endings.std.pl3;}

    //perfect
    assignEndings(result, "perfect_", perfect_stem, "", endings.perf);

    //imperfect
    var impfVocal="e";
    if (conjugation == "A"){impfVocal="a";}
    else if (conjugation == "I" || conjugation == "M"){impfVocal="ie";}
    assignEndings(result, "imperfect_", present_stem, impfVocal+"ba", endings.impf);

    //plusquamperfect
    assignEndings(result, "pluqperfect_", perfect_stem, "", endings.plqpf);

    //future
    if (conjugation == "A" || conjugation == "E"){
        assignEndings(result, "future_", present_stem, vocal+"bi", endings.std);
        result.future_sg1=present_stem+vocal+"b"+endings.std.sg1;
        result.future_pl3=present_stem+vocal+"bu"+endings.std.pl3;
    }
    else if (conjugation == "C") {
        assignEndings(result, "future_", present_stem, "e", endings.impf);
        result.future_sg1=present_stem+"a"+endings.impf.sg1;
    }
    else{
        assignEndings(result, "future_", present_stem, vocal+"e", endings.impf);
        result.future_sg1=present_stem+vocal+"a"+endings.impf.sg1;
    }

    //future II
    assignEndings(result, "future2_", perfect_stem, "", endings.fut2);

    return result;
}
