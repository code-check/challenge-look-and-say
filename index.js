"use strict";

function lookAndSay(n) {
  let array = n.toString().split("");
  let ret = [];
  let count = 0;
  let current = "0";
  array.forEach(n => {
    if (n === current) {
      count++;
    } else {
      if (count > 0) {
        ret.push(count.toString());
        ret.push(current);
      }
      current = n;
      count = 1;
    }
  });
  if (count > 0) {
    ret.push(count.toString());
    ret.push(current);
  }
  return ret.join("");
}

let count = parseInt(process.argv[2]);
let seed = 1;
for (let i=0; i<count; i++) {
  seed = lookAndSay(seed);
  console.log((i + 1) + ": " + seed.length + ": " + seed);
}
