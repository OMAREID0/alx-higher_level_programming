#!/usr/bin/node
const { argv } = process;
if (argv.length > 2) {
  for (let i = 0; i < argv[2]; i++) {
    console.log('C is fun');
  }
}
