#!/usr/bin/node

const squareSize = parseInt(process.argv[2]);

if (squareSize) {
  for (let i = 0; i < squareSize; i++) {
    let line = '';
    for (let j = 0; j < squareSize; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
