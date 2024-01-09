#!/usr/bin/node

const getSecondBiggest = (nums) => nums.length <= 1
  ? 0
  : [...nums].sort((a, b) => b - a)[1];

const secondBiggest = getSecondBiggest(process.argv.slice(2));

console.log(secondBiggest);
