#!/usr/bin/node

function callMeMoby (counter, fn) {
  while (counter > 0) {
    counter--;
    fn();
  }
}

module.exports = { callMeMoby };
