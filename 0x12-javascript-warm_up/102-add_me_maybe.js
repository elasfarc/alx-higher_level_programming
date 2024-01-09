#!/usr/bin/node

function addMeMaybe (number, fn) {
  fn(++number);
}

module.exports = { addMeMaybe };
