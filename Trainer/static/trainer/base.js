function AbstractTrainer(inputId, promptId, vocs){
    this.input=$(inputId);
    this.prompt=$(promptId);
    this.vocs=vocs;
    this.current_voc_index=-1;
}

AbstractTrainer.prototype.getPrompt = function(voc){
    return "Not implemented";
};

AbstractTrainer.prototype.getSolution = function(voc){
    return "Not implemented";
};

AbstractTrainer.prototype.isCorrect = function(val, voc){
    //Not implemented
    return false;
};

AbstractTrainer.prototype.gameover = function(){
    //Not implemented
};

AbstractTrainer.prototype.start = function(){
    this.next();
};

AbstractTrainer.prototype.check = function(){
    var trainer=this;   //So 'this' is always the actual trainer
    if (this.isCorrect(this.input.val(), this.current_voc)){
        this.message("correct");
        setTimeout(function(){trainer.next()}, 1000);
    }
    else{
        this.message("wrong", 1200);
        this.wrongCount+=1;
        if (this.wrongCount >= 2){
            this.input.val(this.getSolution(this.current_voc));
            setTimeout(function(){trainer.next()}, 2000);
        }
    }
};

AbstractTrainer.prototype.next = function(){
    this.current_voc_index+=1;
    this.current_voc=this.vocs[this.current_voc_index];
    if (this.current_voc === undefined){
        this.gameover();
        return
    }
    this.wrongCount=0;

    this.input.val("");
    this.prompt.html(this.getPrompt(this.current_voc));
    this.clearMsg();
};

AbstractTrainer.prototype.message = function(msg, timeout){
    //Not implemented
};

AbstractTrainer.prototype.clearMsg = function(){
    //Not implemented
};
