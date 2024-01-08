#!/usr/bin/node

const myNum = Number(process.argv[2]);

console.log(
  myNum ? 'My number: ' + myNum : 'Not a number'
);
