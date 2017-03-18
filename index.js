
var binding = require('bindings')(`electron-celt-${process.arch}`);

exports.CeltEncoder = binding.CeltEncoder;

