#!/usr/bin/node
const { argv } = process;
if (argv[2] === null) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv[2]; i++) {
    console.log('X'.repeat(argv[2]));
  }
}
