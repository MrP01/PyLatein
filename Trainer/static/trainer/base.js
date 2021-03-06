// Generated by CoffeeScript 1.9.3
var AbstractController, AbstractInputWidget, AbstractResult, AbstractTrainer, BaseController, BoxController, SimpleController, SlidingNotifier, shuffle,
  extend = function(child, parent) { for (var key in parent) { if (hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; },
  hasProp = {}.hasOwnProperty;

AbstractResult = (function() {
  function AbstractResult() {}

  return AbstractResult;

})();

AbstractInputWidget = (function() {
  function AbstractInputWidget() {}

  AbstractInputWidget.prototype.setResult = function(result) {};

  AbstractInputWidget.prototype.getInput = function() {};

  AbstractInputWidget.prototype.isSkip = function() {};

  AbstractInputWidget.prototype.clear = function() {};

  return AbstractInputWidget;

})();

AbstractTrainer = (function() {
  function AbstractTrainer() {}

  AbstractTrainer.prototype.getPrompt = function(voc) {};

  AbstractTrainer.prototype.getSolution = function(voc) {};

  AbstractTrainer.prototype.isCorrect = function(voc, result) {};

  return AbstractTrainer;

})();

SlidingNotifier = (function() {
  function SlidingNotifier(correct_id, wrong_id) {
    this.correct = $(correct_id);
    this.wrong = $(wrong_id);
  }

  SlidingNotifier.prototype.message = function(type, timeout) {
    var code, this_;
    this_ = this;
    if (type === "correct") {
      this.correct.slideDown(400);
      code = function() {
        return this_.correct.slideUp(500);
      };
    } else if (type === "wrong") {
      this.wrong.slideDown(400);
      code = function() {
        return this_.wrong.slideUp(500);
      };
    }
    if (timeout) {
      return setTimeout(code, timeout);
    }
  };

  SlidingNotifier.prototype.clearMessage = function() {
    this.correct.slideUp(500);
    return this.wrong.slideUp(500);
  };

  return SlidingNotifier;

})();

AbstractController = (function() {
  function AbstractController(trainer1, input1, notifier1, promptId) {
    this.trainer = trainer1;
    this.input = input1;
    this.notifier = notifier1;
    this.current_voc = null;
    this.prompt = $(promptId);
  }

  AbstractController.prototype.skip = function() {};

  AbstractController.prototype.check = function() {};

  AbstractController.prototype.next = function() {};

  AbstractController.prototype.start = function() {
    return this.next();
  };

  return AbstractController;

})();

BaseController = (function(superClass) {
  extend(BaseController, superClass);

  function BaseController(trainer, input, notifier, promptId) {
    BaseController.__super__.constructor.call(this, trainer, input, notifier, promptId);
    this.current_voc = null;
    this.wrong_count = 0;
  }

  BaseController.prototype.check = function() {
    var this_;
    this_ = this;
    if (this.input.isSkip()) {
      this.skip();
    } else if (this.trainer.isCorrect(this.current_voc, this.input.getInput())) {
      this.notifier.message("correct", 1500);
      this.input.setResult(this.trainer.getSolution(this.current_voc));
      setTimeout((function() {
        return this_.next();
      }), 1500);
      return "correct";
    } else {
      this.notifier.message("wrong", 2000);
      this.wrong_count += 1;
      this.input.clear();
      if (this.wrong_count >= 2) {
        this.input.setResult(this.trainer.getSolution(this.current_voc));
        setTimeout((function() {
          return this_.next();
        }), 2000);
        return "wrong";
      }
    }
  };

  BaseController.prototype.skip = function() {
    var this_;
    this_ = this;
    this.input.setResult(this.trainer.getSolution(this.current_voc));
    this.notifier.message("wrong", 1500);
    return setTimeout((function() {
      return this_.next();
    }), 1500);
  };

  BaseController.prototype.next = function() {
    this.current_voc = this.getNext();
    if (this.current_voc === void 0) {
      alert("Well done!");
      return;
    }
    this.prompt.html(this.trainer.getPrompt(this.current_voc));
    this.input.clear();
    return this.wrong_count = 0;
  };

  BaseController.prototype.getNext = function() {
    return void 0;
  };

  return BaseController;

})(AbstractController);

SimpleController = (function(superClass) {
  extend(SimpleController, superClass);

  function SimpleController(vocs1, trainer, input, notifier, promptId) {
    this.vocs = vocs1;
    SimpleController.__super__.constructor.call(this, trainer, input, notifier, promptId);
  }

  SimpleController.prototype.getNext = function() {
    this.vocs.splice(0, 1);
    return this.vocs[0];
  };

  SimpleController.prototype.start = function() {
    this.vocs = shuffle(this.vocs);
    return this.next();
  };

  return SimpleController;

})(BaseController);

BoxController = (function(superClass) {
  extend(BoxController, superClass);

  function BoxController(vocs, trainer, input, notifier, promptId) {
    BoxController.__super__.constructor.call(this, trainer, input, notifier, promptId);
    this.current_box = 0;
    this.boxes = [shuffle(vocs), [], [], []];
  }

  BoxController.prototype.check = function() {
    var result;
    result = BoxController.__super__.check.call(this);
    if (result) {
      this.boxes[this.current_box].splice(0, 1);
      if (result === "correct") {
        return this.boxes[this.current_box + 1].push(this.current_voc);
      } else if (result === "wrong") {
        return this.boxes[0].push(this.current_voc);
      }
    }
  };

  BoxController.prototype.skip = function() {
    BoxController.__super__.skip.call(this);
    this.boxes[this.current_box].splice(0, 1);
    return this.boxes[0].push(this.current_voc);
  };

  BoxController.prototype.getNext = function() {
    var box, i, ref, voc;
    voc = this.boxes[this.current_box][0];
    if (voc === void 0) {
      for (box = i = 0, ref = this.current_box + 1; 0 <= ref ? i <= ref : i >= ref; box = 0 <= ref ? ++i : --i) {
        if (this.boxes[box].length > 0) {
          this.current_box = box;
          voc = this.boxes[this.current_box][0];
          break;
        }
      }
    }
    this.alertBoxes();
    return voc;
  };

  BoxController.prototype.alertBoxes = function() {
    return alert("Box 1: " + this.boxes[0].length + "\n" + "Box 2: " + this.boxes[1].length + "\n" + "Box 3: " + this.boxes[2].length + "\n" + "Box 4: " + this.boxes[3].length + "\n");
  };

  return BoxController;

})(BaseController);

shuffle = function(array) {
  var counter, index, temp;
  counter = array.length;
  while (counter > 0) {
    index = Math.floor(Math.random() * counter);
    counter = counter - 1;
    temp = array[counter];
    array[counter] = array[index];
    array[index] = temp;
  }
  return array;
};

//# sourceMappingURL=base.js.map
