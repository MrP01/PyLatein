function fill_form(){
    var conjugation=$("#conjugation").val();
    var present_stem=$("#present_stem").val();
    var perfect_stem="";
    var vocal="";

    //vocal
    if(conjugation == "A") {vocal="a"}
    else if (conjugation == "E") {vocal="e"}
    else {vocal="i"}

    //perfect_stem
    if (conjugation == "A"){perfect_stem=present_stem+"av";}
    else if (conjugation == "E"){perfect_stem=present_stem+"u";}
    else if (conjugation == "I"){perfect_stem=present_stem+"iv";}
    else {perfect_stem=$("#perfect_stem").val();}

    //infinitive and imperatives
    if (conjugation == "K" || conjugation == "M"){
        $("#id_infinitive").val(present_stem+"ere");
        $("#id_imperativeSg").val(present_stem+"e!");
        $("#id_imperativePl").val(present_stem+"ite!");
    }
    else{
        $("#id_infinitive").val(present_stem+vocal+"re");
        $("#id_imperativeSg").val(present_stem+vocal+"!");
        $("#id_imperativePl").val(present_stem+vocal+"te!");
    }

    //present
    if (conjugation == "A" || conjugation == "K"){
        $("#id_presentSg1").val(present_stem+window.endings["StdE"].sg1);}
    else{$("#id_presentSg1").val(present_stem+vocal+window.endings["StdE"].sg1);}
    $("#id_presentSg2").val(present_stem+vocal+window.endings["StdE"].sg2);
    $("#id_presentSg3").val(present_stem+vocal+window.endings["StdE"].sg3);
    $("#id_presentPl1").val(present_stem+vocal+window.endings["StdE"].pl1);
    $("#id_presentPl2").val(present_stem+vocal+window.endings["StdE"].pl2);
    if (conjugation == "K"){
        $("#id_presentPl3").val(present_stem+"u"+window.endings["StdE"].pl3);}
    else if (conjugation == "I" || conjugation == "M"){
        $("#id_presentPl3").val(present_stem+vocal+"u"+window.endings["StdE"].pl3);}
    else{$("#id_presentPl3").val(present_stem+vocal+window.endings["StdE"].pl3);}

    //perfect
    $("#id_perfectSg1").val(perfect_stem+window.endings["PerfE"].sg1);
    $("#id_perfectSg2").val(perfect_stem+window.endings["PerfE"].sg2);
    $("#id_perfectSg3").val(perfect_stem+window.endings["PerfE"].sg3);
    $("#id_perfectPl1").val(perfect_stem+window.endings["PerfE"].pl1);
    $("#id_perfectPl2").val(perfect_stem+window.endings["PerfE"].pl2);
    $("#id_perfectPl3").val(perfect_stem+window.endings["PerfE"].pl3);

    //imperfect
    var impfVocal="e";
    if (conjugation == "A"){impfVocal="a";}
    $("#id_imperfectSg1").val(present_stem+impfVocal+"ba"+window.endings["ImpfE"].sg1);
    $("#id_imperfectSg2").val(present_stem+impfVocal+"ba"+window.endings["ImpfE"].sg2);
    $("#id_imperfectSg3").val(present_stem+impfVocal+"ba"+window.endings["ImpfE"].sg3);
    $("#id_imperfectPl1").val(present_stem+impfVocal+"ba"+window.endings["ImpfE"].pl1);
    $("#id_imperfectPl2").val(present_stem+impfVocal+"ba"+window.endings["ImpfE"].pl2);
    $("#id_imperfectPl3").val(present_stem+impfVocal+"ba"+window.endings["ImpfE"].pl3);

    //plusquamperfect
    $("#id_pluqperfectSg1").val(perfect_stem+window.endings["PlqpfE"].sg1);
    $("#id_pluqperfectSg2").val(perfect_stem+window.endings["PlqpfE"].sg2);
    $("#id_pluqperfectSg3").val(perfect_stem+window.endings["PlqpfE"].sg3);
    $("#id_pluqperfectPl1").val(perfect_stem+window.endings["PlqpfE"].pl1);
    $("#id_pluqperfectPl2").val(perfect_stem+window.endings["PlqpfE"].pl2);
    $("#id_pluqperfectPl3").val(perfect_stem+window.endings["PlqpfE"].pl3);

    //future
    if (conjugation == "A" || conjugation == "E"){
        $("#id_futureSg1").val(present_stem+vocal+"b"+window.endings["StdE"].sg1);
        $("#id_futureSg2").val(present_stem+vocal+"bi"+window.endings["StdE"].sg2);
        $("#id_futureSg3").val(present_stem+vocal+"bi"+window.endings["StdE"].sg3);
        $("#id_futurePl1").val(present_stem+vocal+"bi"+window.endings["StdE"].pl1);
        $("#id_futurePl2").val(present_stem+vocal+"bi"+window.endings["StdE"].pl2);
        $("#id_futurePl3").val(present_stem+vocal+"bu"+window.endings["StdE"].pl3);
    }
    else if (conjugation == "K") {
        $("#id_futureSg1").val(present_stem+"a"+window.endings["ImpfE"].sg1);
        $("#id_futureSg2").val(present_stem+"e"+window.endings["ImpfE"].sg2);
        $("#id_futureSg3").val(present_stem+"e"+window.endings["ImpfE"].sg3);
        $("#id_futurePl1").val(present_stem+"e"+window.endings["ImpfE"].pl1);
        $("#id_futurePl2").val(present_stem+"e"+window.endings["ImpfE"].pl2);
        $("#id_futurePl3").val(present_stem+"e"+window.endings["ImpfE"].pl3);
    }
    else{
        $("#id_futureSg1").val(present_stem+vocal+"a"+window.endings["ImpfE"].sg1);
        $("#id_futureSg2").val(present_stem+vocal+"e"+window.endings["ImpfE"].sg2);
        $("#id_futureSg3").val(present_stem+vocal+"e"+window.endings["ImpfE"].sg3);
        $("#id_futurePl1").val(present_stem+vocal+"e"+window.endings["ImpfE"].pl1);
        $("#id_futurePl2").val(present_stem+vocal+"e"+window.endings["ImpfE"].pl2);
        $("#id_futurePl3").val(present_stem+vocal+"e"+window.endings["ImpfE"].pl3);
    }

    //future II
    $("#id_future2Sg1").val(perfect_stem+window.endings["Fut2E"].sg1);
    $("#id_future2Sg2").val(perfect_stem+window.endings["Fut2E"].sg2);
    $("#id_future2Sg3").val(perfect_stem+window.endings["Fut2E"].sg3);
    $("#id_future2Pl1").val(perfect_stem+window.endings["Fut2E"].pl1);
    $("#id_future2Pl2").val(perfect_stem+window.endings["Fut2E"].pl2);
    $("#id_future2Pl3").val(perfect_stem+window.endings["Fut2E"].pl3);
}
