#!/usr/bin/node
exports.esrever = function (list) {
  for (let i = 0; i < parseInt(list.length / 2); i++) {
    const temp = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = temp;
  }

  return list;
};
