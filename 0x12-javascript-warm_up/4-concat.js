#!/usr/bin/node
const { argv } = process;
if (argv.length > 3) {
  console.log(argv[2] + ' is ' + argv[3]);
} else {
  console.log('No argument');
}
