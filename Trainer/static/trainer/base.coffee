class AbstractResult
  constructor: () ->


class AbstractInputWidget
  constructor: () ->
  setResult: (result) ->
  getInput: () ->
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
  constructor: (@trainer, @vocs, @input, @notifier, promptId) ->
    @current_voc=null
    @current_voc_index=0
    @wrong_count=0
    @prompt=$(promptId)

  check: () ->
  next: () ->
  start: () ->
    @next()


class SimpleController extends AbstractController
  constructor: (trainer, vocs, input, notifier, promptId) ->
    super(trainer, vocs, input, notifier, promptId)
    @current_voc=null
    @next_voc_index=0
    @wrong_count=0

  check: () ->
    this_=this
    if @trainer.isCorrect(@current_voc, @input.getInput())
      @notifier.message("correct", 1500)
      @input.setResult(@trainer.getSolution(@current_voc))
      code=-> this_.next()
      setTimeout(code, 1500)
    else
      @notifier.message("wrong", 2000)
      @wrong_count+=1
      @input.clear()
      if (@wrong_count >= 2)
        @input.setResult(@trainer.getSolution(@current_voc))
        code=-> this_.next()
        setTimeout(code, 2000)

  next: () ->
    @current_voc=@vocs[@next_voc_index]
    if (@current_voc is undefined)
      alert("Well done!")
      return
    @next_voc_index+=1
    @prompt.html(@trainer.getPrompt(@current_voc))
    @input.clear()
    @wrong_count=0

  start: () ->
    @next_voc_index=0
    @next()
