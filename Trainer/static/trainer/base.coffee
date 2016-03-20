class AbstractResult
    constructor: () ->


class AbstractInputWidget
    constructor: () ->
    setResult: (result) ->
    getInput: () ->
    isSkip: () ->
    clear: () ->


class AbstractTrainer
    constructor: () ->
    getPrompt: (voc) ->
    getSolution: (voc) ->
    isCorrect: (voc, result) ->


class SlidingNotifier
    constructor: (correct_id, wrong_id) ->
        @correct=$(correct_id)
        @wrong=$(wrong_id)

    message: (type, timeout) ->
        this_=this
        if (type == "correct")
            @correct.slideDown(400)
            code=() -> this_.correct.slideUp(500)
        else if (type == "wrong")
            @wrong.slideDown(400)
            code=() -> this_.wrong.slideUp(500)

        if timeout
            setTimeout(code, timeout)

    clearMessage: () ->
        @correct.slideUp(500)
        @wrong.slideUp(500)


class AbstractController
    constructor: (@trainer, @input, @notifier, promptId) ->
        @current_voc=null
        @prompt=$(promptId)

    skip: () ->
    check: () ->
    next: () ->
    start: () ->
        @next()


class BaseController extends AbstractController
    constructor: (trainer, input, notifier, promptId) ->
        super(trainer, input, notifier, promptId)
        @current_voc=null
        @wrong_count=0

    check: () ->
        this_=this
        if @input.isSkip()
            @skip()
            return  #this is required, otherwise it would return the return-value of skip()
        else if @trainer.isCorrect(@current_voc, @input.getInput())
            @notifier.message("correct", 1500)
            @input.setResult(@trainer.getSolution(@current_voc))
            setTimeout((-> this_.next()), 1500)
            return "correct"
        else
            @notifier.message("wrong", 2000)
            @wrong_count+=1
            @input.clear()
            if (@wrong_count >= 2)
                @input.setResult(@trainer.getSolution(@current_voc))
                setTimeout((-> this_.next()), 2000)
                return "wrong"

    skip: () ->
        this_=this
        @input.setResult(@trainer.getSolution(@current_voc))
        @notifier.message("wrong", 1500)
        setTimeout((-> this_.next()), 1500)

    next: () ->
        @current_voc=@getNext()
        if @current_voc is undefined
            alert("Well done!")
            return
        @prompt.html(@trainer.getPrompt(@current_voc))
        @input.clear()
        @wrong_count=0

    getNext: () ->
        return undefined

class SimpleController extends BaseController
    constructor: (@vocs, trainer, input, notifier, promptId) ->
        super(trainer, input, notifier, promptId)

    getNext: () ->
        @vocs.splice(0, 1)
        return @vocs[0]

    start: () ->
        @vocs=shuffle(@vocs)
        @next()

class BoxController extends BaseController
    constructor: (vocs, trainer, input, notifier, promptId) ->
        super(trainer, input, notifier, promptId)
        @current_box=0
        @boxes=[
            shuffle(vocs),
            [], [], [],
        ]

    check: () ->
        result=super()
        if result
            @boxes[@current_box].splice(0, 1) #remove first element
            if result == "correct"
                @boxes[@current_box+1].push(@current_voc)
            else if result == "wrong"
                @boxes[0].push(@current_voc)

    skip: () ->
        super()
        @boxes[@current_box].splice(0, 1)
        @boxes[0].push(@current_voc)

    getNext: () ->
        voc=@boxes[@current_box][0] #always the first element in list
        if voc is undefined
            for box in [0..@current_box+1]
                if @boxes[box].length > 0
                    @current_box=box
                    voc=@boxes[@current_box][0]
                    break
        @alertBoxes()
        return voc

    alertBoxes: () ->
        alert(
            "Box 1: "+@boxes[0].length+"\n"+
            "Box 2: "+@boxes[1].length+"\n"+
            "Box 3: "+@boxes[2].length+"\n"+
            "Box 4: "+@boxes[3].length+"\n"
        )

shuffle = (array) ->
    counter = array.length
    while (counter > 0)
        index = Math.floor(Math.random() * counter)
        counter=counter-1
        temp = array[counter]
        array[counter] = array[index]
        array[index] = temp
    return array
