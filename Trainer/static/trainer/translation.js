function TranslationTrainer(inputId, promptId, vocs){
    AbstractTrainer.call(this, inputId, promptId, vocs);
}

TranslationTrainer.prototype=Object.create(AbstractTrainer.prototype);
TranslationTrainer.constructor=AbstractTrainer;

TranslationTrainer.prototype.getPrompt = function(voc){
    if (voc.model == "Vokabel.noun"){
        return voc.fields.sg1+", "+voc.fields.sg2+" ["+voc.fields.genus+"] "+voc.fields.declination;
    }
    else if (voc.model == "Vokabel.verb"){
        return voc.fields.present_sg1+", "+voc.fields.present_sg2+", "+voc.fields.infinitive+", "+voc.fields.perfect_sg1+" "+voc.fields.conjugation;
    }
    else if (voc.model == "Vokabel.adjective"){
        return voc.fields.pos_sg1m+"/"+voc.fields.pos_sg1f+"/"+voc.fields.pos_sg1n+", "+voc.fields.pos_sg2m+" "+voc.fields.declination;
    }
};

TranslationTrainer.prototype.getSolution = function(voc){
    return voc.fields.translation;
};

TranslationTrainer.prototype.isCorrect = function(val, voc){
    var correct=false;
    val=val.toLowerCase();
    voc.fields.translation.split(",").forEach(function(trans){
        trans=$.trim(trans).toLowerCase();
        if (trans == val){
            correct=true;
        }
    });
    return correct;
};

TranslationTrainer.prototype.gameover = function(){
    alert("Congratulations!");
};
