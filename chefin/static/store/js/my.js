function decrementValue(obj) {
  var parent = obj.closest('.input-group');
  var input = parent.querySelector('input[type=number]');
  var value = parseInt(input.value, 10);
  value = isNaN(value) ? 1 : value;
  value = value < 2 ? 1 : value - 1;
  input.value = value;
}

function incrementValue(obj) {
  var parent = obj.closest('.input-group');
  var input = parent.querySelector('input[type=number]');
  var value = parseInt(input.value, 10);
  value = isNaN(value) ? 1 : value;
  value++;
  input.value = value;
}
