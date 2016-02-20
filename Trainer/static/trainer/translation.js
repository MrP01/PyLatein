function TranslationTrainer(inputId, promptId, vocs){
    AbstractTrainer.call(this, inputId, promptId, vocs);
}

TranslationTrainer.prototype=Object.create(AbstractTrainer.prototype);
TranslationTrainer.constructor=AbstractTrainer;

TranslationTrainer.prototype.getPrompt = function(voc){
    if (voc.model == "Vokabel.noun"){
        return voc.fields.sg1;
    }
    else if (voc.model == "Vokabel.verb"){
        return voc.fields.infinitive;
    }
    else if (voc.model == "Vokabel.adjective"){
        return voc.fields.pos_sg1m;
    }
};

TranslationTrainer.prototype.getSolution = function(voc){
    return voc.fields.translation;
};

TranslationTrainer.prototype.isCorrect = function(val, voc){
    return (voc.fields.translation == val)
};

TranslationTrainer.prototype.gameover = function(){
    alert("Congratulations!");
};
