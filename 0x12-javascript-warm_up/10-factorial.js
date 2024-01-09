#!/usr/bin/node

function factorial (x) {
  if (!x || x <= 1) {
    return 1;
  }
  return x * factorial(x - 1);
}

const result = factorial(parseInt(process.argv[2]));
console.log(result);
