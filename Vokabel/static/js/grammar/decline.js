var cases=["sg1", "sg2", "sg3", "sg4", "sg5", "sg6",
        "pl1", "pl2", "pl3", "pl4", "pl5", "pl6"];

var declinations={
    "1O":{"sg1":"us", "sg2":"i", "sg3":"o", "sg4":"um", "sg5":null, "sg6":"o",
        "pl1":"i", "pl2":"orum", "pl3":"is", "pl4":"os", "pl5":null, "pl6":"is"
    },
    "1A":{"sg1":"a", "sg2":"ae", "sg3":"ae", "sg4":"am", "sg5":null, "sg6":"a",
        "pl1":"ae", "pl2":"arum", "pl3":"is", "pl4":"as", "pl5":null, "pl6":"is"
    },
    "3K":{"sg1": null, "sg2": "is", "sg3": "i", "sg4": "em", "sg5": null, "sg6": "e",
        "pl1": "es", "pl2": "um", "pl3": "ibus", "pl4": "es", "pl5": null, "pl6": "ibus"
    },
    "3M":{"sg1": null, "sg2": "is", "sg3": "i", "sg4": "em", "sg5": null, "sg6": "e",
        "pl1": "es", "pl2": "ium", "pl3": "ibus", "pl4": "es", "pl5": null, "pl6": "ibus"
    },
    "3I":{"sg1": null, "sg2": "is", "sg3": "i", "sg4": "im", "sg5": null, "sg6": "i",
        "pl1": "es", "pl2": "ium", "pl3": "ibus", "pl4": "es", "pl5": null, "pl6": "ibus"
    },
    "5E":{"sg1": "es", "sg2": "ei", "sg3": "ei", "sg4": "em", "sg5": null, "sg6": "e",
        "pl1": "es", "pl2": "erum", "pl3": "ebus", "pl4": "es", "pl5": null, "pl6": "ebus"
    },
    "5U":{"sg1": "us", "sg2": "us", "sg3": "ui", "sg4": "um", "sg5": null, "sg6": "u",
        "pl1": "us", "pl2": "uum", "pl3": "ibus", "pl4": "us", "pl5": null, "pl6": "ibus"
    }
};

function decline(sg1, stem, genus, declination){
    var dec=declinations[declination];
    var result={};
    for (var i = 0; i < cases.length; i++){
        result[cases[i]]=stem+dec[cases[i]]
    }
    if (["3K", "3M", "3I"].indexOf(declination) > -1){
        result.sg1=sg1;
    }
    else if (declination == "1O" && genus == "n"){
        result.sg1=stem+"um";
    }
    if (genus == "n"){
        result.sg4=result.sg1;
        if (["1O", "3K"].indexOf(declination) > -1){
            result.pl1=stem+"a";
        }
        else if (declination == "3I"){
            result.pl1=stem+"ia"
        }
        result.pl4=result.pl1;
    }
    result.sg5=result.sg1+"!";
    result.pl5=result.pl1+"!";
    if (genus == "m" && declination == "1O" && result.sg1.slice(-2) == "us"){  //Vocative on '-us'
        result.sg5=stem+"e!";
    }
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

//function comparative(stem)
