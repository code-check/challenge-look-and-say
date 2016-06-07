"use strict";

var assert = require("chai").assert;
var codecheck = require("codecheck");
var fs = require("fs");

describe("test", () => {
  var app = codecheck.consoleApp(process.env.APP_COMMAND);

  it("8 -> 1", function() {
    return app.run(8).spread(function(code, stdOut) {
      assert.equal(code, 0);
      assert.equal(stdOut.length, 1);
      assert.equal(stdOut[0], "1113213211");
    });
  });

  it("20 -> ...", function() {
    return app.run(20).spread(function(code, stdOut) {
      assert.equal(code, 0);
      assert.equal(stdOut.length, 1);
      assert.equal(stdOut[0], "11131221131211132221232112111312111213111213211231132132211211131221131211221321123113213221123113112221131112311332211211131221131211132211121312211231131112311211232221121321132132211331121321231231121113112221121321133112132112312321123113112221121113122113121113123112112322111213211322211312113211");
    });
  });

  it("answer.md", function() {
    var text = fs.readFileSync("./answer.md", "utf-8");
    assert.equal(text.split("\n")[0], "I don't know");
  });
});
