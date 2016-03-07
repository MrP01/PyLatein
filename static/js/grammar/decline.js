var cases=["sg1", "sg2", "sg3", "sg4", "sg5", "sg6",
        "pl1", "pl2", "pl3", "pl4", "pl5", "pl6"];

var declinations={
    "O":{"sg1":"us", "sg2":"i", "sg3":"o", "sg4":"um", "sg6":"o",
        "pl1":"i", "pl2":"orum", "pl3":"is", "pl4":"os", "pl6":"is"
    },
    "A":{"sg1":"a", "sg2":"ae", "sg3":"ae", "sg4":"am", "sg6":"a",
        "pl1":"ae", "pl2":"arum", "pl3":"is", "pl4":"as", "pl6":"is"
    },
    "C":{"sg1": null, "sg2":"is", "sg3":"i", "sg4":"em", "sg6":"e",
        "pl1":"es", "pl2":"um", "pl3":"ibus", "pl4":"es", "pl6":"ibus"
    },
    "M":{"sg1": null, "sg2":"is", "sg3":"i", "sg4":"em", "sg6":"e",
        "pl1":"es", "pl2":"ium", "pl3":"ibus", "pl4":"es", "pl6":"ibus"
    },
    "I":{"sg1": null, "sg2":"is", "sg3":"i", "sg4":"im", "sg6":"i",
        "pl1":"es", "pl2":"ium", "pl3":"ibus", "pl4":"es", "pl6":"ibus"
    },
    "E":{"sg1":"es", "sg2":"ei", "sg3":"ei", "sg4":"em", "sg6":"e",
        "pl1":"es", "pl2":"erum", "pl3":"ebus", "pl4":"es", "pl6":"ebus"
    },
    "U":{"sg1":"us", "sg2":"us", "sg3":"ui", "sg4":"um", "sg6":"u",
        "pl1":"us", "pl2":"uum", "pl3":"ibus", "pl4":"us", "pl6":"ibus"
    }
};

adjective_declinations=["AO", "M"];

function decline(sg1, stem, genus, declination, plonly){
    var result={};

    var dec=declinations[declination];
    for (var i = 0; i < cases.length; i++){
        result[cases[i]]=stem+dec[cases[i]]}

    if (sg1 == "__auto__"){
        if (declination == "O" && genus == "n"){
            result.sg1=stem+"um";}
    }
    else{
        result.sg1=sg1;
    }

    if (genus == "n"){
        result.sg4=result.sg1;
        if (["O", "C"].indexOf(declination) > -1){
            result.pl1=stem+"a";}
        else if (declination == "I"){
            result.pl1=stem+"ia"}
        result.pl4=result.pl1;
    }

    result.sg5=result.sg1+"!";
    result.pl5=result.pl1+"!";
    if (genus == "m" && declination == "O" && result.sg1.slice(-2) == "us"){  //Vocative on '-us'
        result.sg5=stem+"e!";}

    if (plonly){
        for (i = 0; i <= 6; i++){
            result["sg"+i]="-"}
    }

    return result;
}

function decline_adjective(sg1m, sg1f, sg1n, stem, adj_declination){
    var result={};
    if (adj_declination == "AO"){
        result.m=decline("__auto__", stem, "m", "O");
        result.f=decline("__auto__", stem, "f", "A");
        result.n=decline("__auto__", stem, "n", "O");
    }
    else if (adj_declination == "M"){
        result.m=decline(sg1m, stem, "m", "I");
        result.m.sg4=stem+"em";
        result.f=decline(sg1f, stem, "f", "I");
        result.f.sg4=stem+"em";
        result.n=decline(sg1n, stem, "n", "I");
    }
    return result;
}

function comparative(stem){
    var result={};
    var newstem=stem+"ior";
    result.m=decline(newstem, newstem, "m", "C");
    result.f=decline(newstem, newstem, "f", "C");
    result.n=decline(stem+"ius", newstem, "n", "C");
    return result;
}

function superlative(stem, auto){
    var result={};
    if (auto){
        stem=stem+"issim";
    }
    result.m=decline("__auto__", stem, "m", "O");
    result.f=decline("__auto__", stem, "f", "A");
    result.n=decline("__auto__", stem, "n", "O");
    return result;
}

//function recognize(sg2){
//    //returns all possible declinations of a noun
//    var result=[];
//    for (var declination in declinations){
//        if (declinations.hasOwnProperty(declination)){
//            var x=declinations[declination].sg2;
//            if (x == sg2.slice(-x.length)){
//                result.push(declination);
//            }
//        }
//    }
//    return result;
//}
