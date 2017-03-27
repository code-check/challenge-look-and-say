"use strict";

const assert = require("chai").assert;
const codecheck = require("codecheck");
var fs = require("fs");

describe("secret test", () => {
  var app = codecheck.consoleApp(process.env.APP_COMMAND);

  it("8 -> ...", function() {
    return app.codecheck(8).then( result => {
      assert.equal(result.code, 0);
      assert.equal(result.stdout.length, 1);
      assert.equal(result.stdout[0], "1113213211");
    });
  });

  it("20 -> ...", function() {
    return app.codecheck(20).then( result => {
      assert.equal(result.code, 0);
      assert.equal(result.stdout.length, 1);
      assert.equal(result.stdout[0], "11131221131211132221232112111312111213111213211231132132211211131221131211221321123113213221123113112221131112311332211211131221131211132211121312211231131112311211232221121321132132211331121321231231121113112221121321133112132112312321123113112221121113122113121113123112112322111213211322211312113211");
    });
  });

  it("The initial 500 digit of 10000th number is ...", function() {
    var text = fs.readFileSync("./longOutput.txt", "utf-8");
    var answer = text.split(/\r?\n/)[0];
    assert.equal(answer, "13211321322113311213212312311211131122211213211331121321123123211231131122211211131221131112311332211213211321223112111311222112132113213221123123211231132132211231131122211311123113322112111312211312111322111213122112311311123112112322211213211321322113312211223113112221121113122113111231133221121321132132211331121321232221123123211231132132211231131122211331121321232221123113112221131112311332111213122112311311123112112322211211131221131211132221232112111312211322111312211213211312111322211231");
  });
});
