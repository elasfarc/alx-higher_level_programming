#!/usr/bin/node

function intAddition (a, b) {
  return parseInt(a) + parseInt(b);
}

const addition = intAddition(process.argv[2], process.argv[3]);
console.log(addition);
