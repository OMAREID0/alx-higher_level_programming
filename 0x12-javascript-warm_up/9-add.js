#!/usr/bin/node
const { argv } = process;
function add (a, b) {
  return (parseInt(a) + parseInt(b));
}
const result = add(argv[2], argv[3]);
console.log(result);
