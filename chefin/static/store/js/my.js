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


function removeItem(btn) {
  // Находим родительскую строку элемента
  var row = btn.parentNode.parentNode;
  // Удаляем строку из таблицы
  row.parentNode.removeChild(row);
}


 // Получаем все элементы с классом "quantity-input"
    const quantityInputs = document.querySelectorAll('.quantity-input');

    // Добавляем обработчик события "input" к каждому элементу
    quantityInputs.forEach(input => {
        input.addEventListener('input', updateTotalPrice);
    });

    function updateTotalPrice() {
        const quantity = parseInt(this.value); // Получаем текущее значение количества
        const price = parseInt(this.dataset.price); // Получаем цену товара
        const totalPriceElement = this.closest('.row').querySelector('.total-price'); // Находим элемент для общей стоимости

        const totalPrice = price * quantity; // Вычисляем общую стоимость

        totalPriceElement.textContent = totalPrice.toFixed(2); // Обновляем значение общей стоимости на странице
    }