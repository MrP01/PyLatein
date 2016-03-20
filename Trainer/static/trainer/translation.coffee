class Result extends AbstractResult
    constructor: (@translation) ->


class InputWidget extends AbstractInputWidget
    constructor: (inputId) ->
        @translation=$(inputId)

    setResult: (result) ->
        @translation.val(result.translation)
    getInput: () ->
        return new Result(@translation.val())
    isSkip: () ->
        return (@translation.val() in ["?"])
    clear: () ->
        @translation.val("")


class Trainer extends AbstractTrainer
    getPrompt: (voc) ->
        if (voc.model == "Vokabel.noun")
                return voc.fields.sg1+", "+voc.fields.sg2+" ["+voc.fields.genus+"] "+voc.fields.declination
        else if (voc.model == "Vokabel.verb")
                return voc.fields.present_sg1+", "+voc.fields.present_sg2+", "+voc.fields.infinitive+", "+voc.fields.perfect_sg1+" "+voc.fields.conjugation
        else if (voc.model == "Vokabel.adjective")
                return voc.fields.pos_sg1m+"/"+voc.fields.pos_sg1f+"/"+voc.fields.pos_sg1n+", "+voc.fields.pos_sg2m+" "+voc.fields.declination

    getSolution: (voc) ->
        return new Result(voc.fields.translation)

    isCorrect: (voc, result) ->
        result.translation=$.trim(result.translation).toLowerCase()
        for trans in @getSolution(voc).translation.split(",")
            trans=$.trim(trans).toLowerCase()
            if (trans == result.translation)
                return true
        return false
