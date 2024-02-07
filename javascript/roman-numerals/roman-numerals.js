/** Roman Numerals exercise. */

const romanMap = new Map([
  [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], 
  [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], 
  [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']
]);

export const toRoman = (number) => {
  let result = '';
  while (number > 0) {
    for (const [num, roman] of romanMap) {
      if (number >= num) {
        result += roman;
        number -= num;
        break;
      }
    }
  }
  return result;
};
